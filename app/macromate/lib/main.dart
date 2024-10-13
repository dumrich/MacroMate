import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'screens/menu_screen.dart';
import 'screens/chatbot_screen.dart';
import 'models/user_input_state.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize the user input state
  final userInputState = UserInputState();

  runApp(
    ChangeNotifierProvider(
      create: (_) => userInputState, // Provide the UserInputState to the widget tree
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.grey),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => const ChatbotScreen(),
        '/user_input': (context) => const UserInputScreen(),
      },
    );
  }
}