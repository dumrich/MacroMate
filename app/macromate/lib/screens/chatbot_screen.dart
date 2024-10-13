import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../models/user_input_state.dart';

class ChatbotScreen extends StatefulWidget {
  const ChatbotScreen({super.key});

  @override
  State<ChatbotScreen> createState() => _ChatbotScreenState();
}

class _ChatbotScreenState extends State<ChatbotScreen> {
  var result = 'Generate a meal plan by pressing the bottom-right button!';

  @override
  Widget build(BuildContext context) {
    var userInputState = Provider.of<UserInputState>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Meal Plan Generator'),
        leading: IconButton(
          icon: const Icon(Icons.input),
          onPressed: () {
            Navigator.pushNamed(context, '/user_input');
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        onPressed: () async {
          var postResult = 'Loading your personalized meal plan...';
          
          postResult = await makePostRequest(userInputState);

          setState(() {
            result = postResult;
          });
        }
      ),
      body: ListView(
        padding: const EdgeInsets.all(28.0),
        children: [
          Text(
            result,  // Display the huge multiline text here
            style: const TextStyle(fontSize: 22),  // Adjust font size if needed
          ),
        ],
      ),
    );
  }

  Future<String> makePostRequest(UserInputState userInputState) async {
    // The URL you are sending the POST request to
    const String url = 'http://104.39.68.161:8000/app_query/';

    // The data you want to send in the request body
    Map<String, dynamic> requestBody = userInputState.calculateMacronutrients();

    try {
      // Make the POST request
      final http.Response response = await http.post(
        Uri.parse(url),
        headers: {
          'Content-Type': 'application/json',  // Specify that the request body is JSON
        },
        body: jsonEncode(requestBody),  // Encode the map as JSON
      );

      // Check if the request was successful (status code 200-299)
      if (response.statusCode == 200) {
        Map<String, dynamic> responseData = jsonDecode(response.body);

        // Check if "response" key exists and return its value
        if (responseData.containsKey('response')) {
          return responseData['response'];  // Return the value of the "response" key
        } else {
          return 'Response key not found in the response';
        }
      } else {
        // If the request failed
        return 'Failed with status code: ${response.statusCode}';
      }
    } catch (error) {
      // Handle any errors that occur during the request
      return 'Error: $error';
    }
  }
}