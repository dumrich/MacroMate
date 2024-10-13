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
      child: MyApp(),
    ),
  );
}

final blackColorScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: Colors.grey.shade600,
    onPrimary: Colors.white,
    primaryContainer: Colors.black,
    secondary: Colors.grey.shade400,
    onSecondary: Colors.white,
    secondaryContainer: Colors.grey.shade700,
    surface: Colors.grey.shade900,
    onSurface: Colors.white,
    error: Colors.redAccent,
    onError: Colors.white,
  );

final lightColorScheme = ColorScheme(
  brightness: Brightness.light,
  primary: Colors.grey.shade300,
  onPrimary: Colors.black,
  primaryContainer: Colors.white,
  secondary: Colors.grey.shade500,
  onSecondary: Colors.black,
  secondaryContainer: Colors.grey.shade200,
  surface: Colors.grey.shade800,
  onSurface: Colors.black,
  error: Colors.red.shade400,
  onError: Colors.white,
);

class MyApp extends StatelessWidget {
  MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: blackColorScheme,
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