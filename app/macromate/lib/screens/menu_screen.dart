import 'package:flutter/material.dart';

class UserInputScreen extends StatefulWidget {
  const UserInputScreen({super.key});

  @override
  State<UserInputScreen> createState() => _UserInputScreenState();
}

class _UserInputScreenState extends State<UserInputScreen> {
  // List of available goals
  final List<String> _genders = ['Male', 'Female'];
  final List<String> _activityLevels = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Super Activate'];
  final List<String> _goals = ['Maintain', 'Bulk', 'Cut'];
  final List<String> _timeFrames = ['Short (1-2 months)', 'Medium (3-5 months)', 'Long (6+ months)'];

  // Variables for age, height, weight
  double _age = 25; //Defualt age
  double _height = 70; // Default height in in
  double _weight = 150;  // Default weight in pounds

  // Variables to store dropdowns
  String _selectedGender = 'Male';
  String _selectedActivityLevel = 'Sedentary';
  String _selectedGoal = 'Lose Weight';
  String _selectedTimeFrame = 'Short (1-2 months)';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Adjust Height, Weight & Goals'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Age Slider
            Text('Age: ${_age.toInt()} years old', style: const TextStyle(fontSize: 16)),
            Slider(
              value: _age,
              min: 1, // Minimum age
              max: 99, // Maximum age
              divisions: 98, // Number of steps
              label: _age.toInt().toString(),
              onChanged: (double value) {
                setState(() {
                  _age = value;
                });
              },
            ),

            // Height Slider
            Text('Height: ${_height.toInt()} inches', style: const TextStyle(fontSize: 16)),
            Slider(
              value: _height,
              min: 20, // Minimum height in inches
              max: 100, // Maximum height in inches
              divisions: 80, // Number of steps
              label: _height.toInt().toString(),
              onChanged: (double value) {
                setState(() {
                  _height = value;
                });
              },
            ),

            const SizedBox(height: 16),

            //Weight Slider
            Text('Weight: ${_weight.toInt()} pounds', style: const TextStyle(fontSize: 16)),
            Slider(
              value: _weight,
              min: 30, // Minimum height in pounds
              max: 400, // Maximum height in pounds
              divisions: 370, // Number of steps
              label: _weight.toInt().toString(),
              onChanged: (double value) {
                setState(() {
                  _weight = value;
                });
              },
            ),
            
            const SizedBox(height: 16),

            // Gender Dropdown with Vertical Line Divider
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Expanded(
                  flex: 4,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text('Gender:', style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
                const SizedBox(width: 20),
                Expanded(
                  flex: 6,
                  child: DropdownButton<String>(
                    value: _selectedGender,
                    items: _genders.map((String gender) {
                      return DropdownMenuItem<String>(
                        value: gender,
                        child: Text(gender),
                      );
                    }).toList(),
                    onChanged: (String? newValue) {
                      setState(() {
                        _selectedGender = newValue!;
                      });
                    },
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // Activity Level Dropdown with Vertical Line Divider
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Expanded(
                  flex: 4,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text('Activity Level:', style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
                const SizedBox(width: 20),
                Expanded(
                  flex: 6,
                  child: DropdownButton<String>(
                    value: _selectedActivityLevel,
                    items: _activityLevels.map((String activityLevel) {
                      return DropdownMenuItem<String>(
                        value: activityLevel,
                        child: Text(activityLevel),
                      );
                    }).toList(),
                    onChanged: (String? newValue) {
                      setState(() {
                        _selectedActivityLevel = newValue!;
                      });
                    },
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // Goal Dropdown with Vertical Line Divider
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Expanded(
                  flex: 4,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text('Goal:', style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
                const SizedBox(width: 20),
                Expanded(
                  flex: 6,
                  child: DropdownButton<String>(
                    value: _selectedGoal,
                    items: _goals.map((String goal) {
                      return DropdownMenuItem<String>(
                        value: goal,
                        child: Text(goal),
                      );
                    }).toList(),
                    onChanged: (String? newValue) {
                      setState(() {
                        _selectedGoal = newValue!;
                      });
                    },
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // Timeframe Dropdown with Vertical Line Divider
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Expanded(
                  flex: 4,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text('Timeframe:', style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
                const SizedBox(width: 20),
                Expanded(
                  flex: 6,
                  child: DropdownButton<String>(
                    value: _selectedTimeFrame,
                    items: _timeFrames.map((String timeFrame) {
                      return DropdownMenuItem<String>(
                        value: timeFrame,
                        child: Text(timeFrame),
                      );
                    }).toList(),
                    onChanged: (String? newValue) {
                      setState(() {
                        _selectedTimeFrame = newValue!;
                      });
                    },
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}