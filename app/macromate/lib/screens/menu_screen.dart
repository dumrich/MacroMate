import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/user_input_state.dart';

class UserInputScreen extends StatelessWidget {
  const UserInputScreen({super.key});

  @override
  Widget build(BuildContext context) {
    var userInputState = Provider.of<UserInputState>(context);
    var colorScheme = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Adjust Biometrics and Goals'),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context); // Go back to Home Screen
          },
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Age Slider
            Text('Age: ${userInputState.age.toInt()} years old', style: const TextStyle(fontSize: 16)),
            Slider(
              inactiveColor: colorScheme.secondary,
              value: userInputState.age,
              min: 1, // Minimum age
              max: 99, // Maximum age
              divisions: 98, // Number of steps
              label: userInputState.age.toInt().toString(),
              onChanged: (double age) {
                userInputState.setAge(age);
              },
            ),

            // Height Slider
            Text('Height: ${userInputState.height.toInt()} inches', style: const TextStyle(fontSize: 16)),
            Slider(
              inactiveColor: colorScheme.secondary,
              value: userInputState.height,
              min: 20, // Minimum height in inches
              max: 100, // Maximum height in inches
              divisions: 80, // Number of steps
              label: userInputState.height.toInt().toString(),
              onChanged: (double height) {
                userInputState.setHeight(height);
              },
            ),

            const SizedBox(height: 16),

            //Weight Slider
            Text('Weight: ${userInputState.weight.toInt()} pounds', style: const TextStyle(fontSize: 16)),
            Slider(
              inactiveColor: colorScheme.secondary,
              value: userInputState.weight,
              min: 30, // Minimum height in pounds
              max: 400, // Maximum height in pounds
              divisions: 370, // Number of steps
              label: userInputState.weight.toInt().toString(),
              onChanged: (double weight) {
                userInputState.setWeight(weight);
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
                    value: userInputState.selectedGender,
                    items: userInputState.genders.map((String gender) {
                      return DropdownMenuItem<String>(
                        value: gender,
                        child: Text(gender),
                      );
                    }).toList(),
                    onChanged: (String? gender) {
                      userInputState.setGender(gender!);
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
                    value: userInputState.selectedActivityLevel,
                    items: userInputState.activityLevels.map((String activityLevel) {
                      return DropdownMenuItem<String>(
                        value: activityLevel,
                        child: Text(activityLevel),
                      );
                    }).toList(),
                    onChanged: (String? activityLevel) {
                      userInputState.setActivityLevel(activityLevel!);
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
                    value: userInputState.selectedGoal,
                    items: userInputState.goals.map((String goal) {
                      return DropdownMenuItem<String>(
                        value: goal,
                        child: Text(goal),
                      );
                    }).toList(),
                    onChanged: (String? goal) {
                      userInputState.setGoal(goal!);
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
                    value: userInputState.selectedTimeFrame,
                    items: userInputState.timeFrames.map((String timeFrame) {
                      return DropdownMenuItem<String>(
                        value: timeFrame,
                        child: Text(timeFrame),
                      );
                    }).toList(),
                    onChanged: (String? timeFrame) {
                      userInputState.setTimeFrame(timeFrame!);
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