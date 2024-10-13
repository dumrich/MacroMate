import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/user_input_state.dart';

class ChatbotScreen extends StatelessWidget {
  const ChatbotScreen({super.key});

  @override
  Widget build(BuildContext context) {
    var userInputState = Provider.of<UserInputState>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Screen'),
        leading: IconButton(
          icon: const Icon(Icons.input),
          onPressed: () {
            Navigator.pushNamed(context, '/user_input');
          },
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'Age: ${userInputState.age.toInt()}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Height: ${userInputState.height.toInt()}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Weight: ${userInputState.weight.toInt()}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Gender: ${userInputState.selectedGender}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Activity Level: ${userInputState.selectedActivityLevel}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Goal: ${userInputState.selectedGoal}',
              style: const TextStyle(fontSize: 24),
            ),
            Text(
              'Time Frame: ${userInputState.selectedTimeFrame}',
              style: const TextStyle(fontSize: 24),
            ),
          ],
        ),
      ),
    );
  }
}