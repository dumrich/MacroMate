import 'package:flutter/foundation.dart';

class UserInputState extends ChangeNotifier {

  // List of available dropdown items
  final List<String> _genders = ['Male', 'Female'];
  final List<String> _activityLevels = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Super Activate'];
  final List<String> _goals = ['Maintain', 'Bulk', 'Cut'];
  final List<String> _timeFrames = ['Short (1-2 months)', 'Medium (3-5 months)', 'Long (6+ months)'];
  final List<String> _menus = ['east', 'pollock', 'west', 'north', 'south'];


  // Variables for age, height, weight, and other user inputs
  double _age = 25;
  double _height = 70;
  double _weight = 150;
  String _selectedGender = 'Male';
  String _selectedActivityLevel = 'Sedentary';
  String _selectedGoal = 'Maintain';
  String _selectedTimeFrame = 'Short (1-2 months)';
  String _selectedMenu = 'east';

  // Getters
  double get age => _age;
  double get height => _height;
  double get weight => _weight;
  String get selectedGender => _selectedGender;
  String get selectedActivityLevel => _selectedActivityLevel;
  String get selectedGoal => _selectedGoal;
  String get selectedTimeFrame => _selectedTimeFrame;
  String get selectedMenu => _selectedMenu;

  List<String> get genders => _genders;
  List<String> get activityLevels => _activityLevels;
  List<String> get goals => _goals;
  List<String> get timeFrames => _timeFrames;
  List<String> get menus => _menus;

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

  void setMenu(String newMenu) {
    _selectedMenu = newMenu;
    notifyListeners();
  }

  // Function to calculate daily caloric needs using Mifflin-St Jeor equation
  double calculateCalories() {
    // Convert weight to kg and height to cm
    double weightKg = _weight * 0.453592;
    double heightCm = _height * 2.54;

    // Calculate BMR (Basal Metabolic Rate)
    double bmr;
    if (_selectedGender == 'Male') {
      bmr = 10 * weightKg + 6.25 * heightCm - 5 * _age + 5;
    } else {
      bmr = 10 * weightKg + 6.25 * heightCm - 5 * _age - 161;
    }

    // Apply activity multiplier based on the selected activity level
    double activityMultiplier = 1.2; // Default for Sedentary
    if (_selectedActivityLevel == 'Lightly Active') {
      activityMultiplier = 1.375;
    } else if (_selectedActivityLevel == 'Moderately Active') {
      activityMultiplier = 1.55;
    } else if (_selectedActivityLevel == 'Very Active') {
      activityMultiplier = 1.725;
    } else if (_selectedActivityLevel == 'Super Active') {
      activityMultiplier = 1.9;
    }

    // Calculate TDEE (Total Daily Energy Expenditure)
    return bmr * activityMultiplier;
  }

  // Function to calculate macronutrient distribution based on calories
  Map<String, String> calculateMacronutrients() {
    double totalCalories = calculateCalories();

    // Calculate macronutrients
    double carbsGrams = (totalCalories * 0.5) / 4;   // Carbs: 50% of calories, 4 calories per gram
    double proteinGrams = (totalCalories * 0.2) / 4; // Protein: 20% of calories, 4 calories per gram
    double fatGrams = (totalCalories * 0.3) / 9;     // Fat: 30% of calories, 9 calories per gram

    return {
      'calories': totalCalories.toString(),
      'carbohydrates': carbsGrams.toString(),
      'proteins': proteinGrams.toString(),
      'fats': fatGrams.toString(),
      'menu_id': selectedMenu
    };
  }
}
