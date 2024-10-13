import streamlit as st
import matplotlib.pyplot as plt
import requests

API_URL = ""

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

for message in st.session_state["conversation"]:
    st.write(message)

user_input = st.text_input("You:", "")

def query_llm_api(user_input):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "query": user_input,
        
    }
    
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("response", "Error: No response received")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
if user_input:
    # Add the user's input to the conversation history
    st.session_state["conversation"].append(f"You: {user_input}")
    
    # Get the LLM's response
    llm_response = query_llm_api(user_input)
    
    # Add the LLM's response to the conversation history
    st.session_state["conversation"].append(f"Bot: {llm_response}")
    
    # Clear the input field after submission
    st.text_input("You:", value="", key="input_clear")

# Function to calculate maintenance calories with weight in pounds and height in inches
def get_maintenance_calories(age, height_in_inches, weight_in_pounds, gender, activity_level):
    weight_kg = weight_in_pounds * 0.453592
    height_cm = height_in_inches * 2.54
    
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == "Female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    if activity_level == "Sedentary":
        maintenance_calories = bmr * 1.2
    elif activity_level == "Lightly active":
        maintenance_calories = bmr * 1.375
    elif activity_level == "Moderately active":
        maintenance_calories = bmr * 1.55
    elif activity_level == "Very active":
        maintenance_calories = bmr * 1.725
    elif activity_level == "Super active":
        maintenance_calories = bmr * 1.9

    return round(maintenance_calories, 2)

# Function to adjust calories for bulk/cut
def get_bulk_or_cut_calories(maintenance_calories, goal, timeframe):
    if goal == "Bulk":
        calorie_adjustment = 0.15
    elif goal == "Cut":
        calorie_adjustment = -0.15

    adjustment = maintenance_calories * calorie_adjustment

    if timeframe == "Short (1-2 months)":
        adjustment *= 1.2
    elif timeframe == "Medium (3-5 months)":
        adjustment *= 1.0
    elif timeframe == "Long (6+ months)":
        adjustment *= 0.8

    return round(maintenance_calories + adjustment, 2)

# Sidebar for user input
st.sidebar.header("Enter your details")
age = st.sidebar.slider("Age", 1, 99, 25)
height = st.sidebar.slider("Height (inches)", 20, 100, 70)
weight = st.sidebar.slider("Weight (pounds)", 30, 400, 150)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])
goal = st.sidebar.selectbox("Goal", ["Maintain", "Bulk", "Cut"])
timeframe = st.sidebar.selectbox("Timeframe", ["Short (1-2 months)", "Medium (3-5 months)", "Long (6+ months)"])

# Calculate maintenance calories
if st.sidebar.button("Calculate Calories"):
    maintenance_calories = get_maintenance_calories(age, height, weight, gender, activity_level)
    
    if goal == "Maintain":
        result = maintenance_calories
    else:
        result = get_bulk_or_cut_calories(maintenance_calories, goal, timeframe)
    
    st.write(f"Estimated Calories: {result} kcal/day")

    # Set default grams for macronutrients based on typical distribution
    default_carbs_g = (0.5 * result) / 4  # 50% of calories from carbs
    default_proteins_g = (0.25 * result) / 4  # 25% of calories from proteins
    default_fats_g = (0.20 * result) / 9  # 20% of calories from fats

    # Calories from each macronutrient
    carbs_calories = default_carbs_g * 4
    proteins_calories = default_proteins_g * 4
    fats_calories = default_fats_g * 9
    vitamins_calories = result - (carbs_calories + proteins_calories + fats_calories)

    # Check if total calories are exceeded
    if vitamins_calories < 0:
        st.error("The total calorie intake from macronutrients exceeds the calculated total calories.")
    else:
        # Pie chart
        labels = ['Carbohydrates', 'Proteins', 'Fats', 'Vitamins/Minerals']
        sizes = [default_carbs_g, default_proteins_g, default_fats_g, vitamins_calories / 4]  # Convert vitamin calories to grams
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
        explode = (0.1, 0, 0, 0)  # Slightly explode the carbs slice

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, startangle=90, 
               autopct=lambda p: f'{int(p / 100 * sum(sizes))} g' if p > 0 else '')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig)
