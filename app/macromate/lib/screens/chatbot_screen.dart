import 'package:flutter/material.dart';

class ChatbotScreen extends StatelessWidget {
  const ChatbotScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home Screen'),
        leading: IconButton(
          icon: Icon(Icons.input),
          onPressed: () {
            Navigator.pushNamed(context, '/user_input');
          },
        ),
      ),
      body: const Center(
        child: Text(
          'Not implemented',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}