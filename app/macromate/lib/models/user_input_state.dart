import 'package:flutter/foundation.dart';

class UserInputState extends ChangeNotifier {

  // List of available dropdown items
  final List<String> _genders = ['Male', 'Female'];
  final List<String> _activityLevels = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Super Activate'];
  final List<String> _goals = ['Maintain', 'Bulk', 'Cut'];
  final List<String> _timeFrames = ['Short (1-2 months)', 'Medium (3-5 months)', 'Long (6+ months)'];

  // Variables for age, height, weight, and other user inputs
  double _age = 25;
  double _height = 70;
  double _weight = 150;
  String _selectedGender = 'Male';
  String _selectedActivityLevel = 'Sedentary';
  String _selectedGoal = 'Maintain';
  String _selectedTimeFrame = 'Short (1-2 months)';

  // Getters
  double get age => _age;
  double get height => _height;
  double get weight => _weight;
  String get selectedGender => _selectedGender;
  String get selectedActivityLevel => _selectedActivityLevel;
  String get selectedGoal => _selectedGoal;
  String get selectedTimeFrame => _selectedTimeFrame;

  List<String> get genders => _genders;
  List<String> get activityLevels => _activityLevels;
  List<String> get goals => _goals;
  List<String> get timeFrames => _timeFrames;

  // Setters with notifyListeners to notify the UI of state changes
  void setAge(double newAge) {
    _age = newAge;
    notifyListeners();
  }

  void setHeight(double newHeight) {
    _height = newHeight;
    notifyListeners();
  }

  void setWeight(double newWeight) {
    _weight = newWeight;
    notifyListeners();
  }

  void setGender(String newGender) {
    _selectedGender = newGender;
    notifyListeners();
  }

  void setActivityLevel(String newActivityLevel) {
    _selectedActivityLevel = newActivityLevel;
    notifyListeners();
  }

  void setGoal(String newGoal) {
    _selectedGoal = newGoal;
    notifyListeners();
  }

  void setTimeFrame(String newTimeFrame) {
    _selectedTimeFrame = newTimeFrame;
    notifyListeners();
  }
}
