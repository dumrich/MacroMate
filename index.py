import streamlit as st
from openai import OpenAI

client = OpenAI( api_key=)



# def get_maintenance_calories(age, height, weight, gender, activity_level):
#     prompt = f"""
#     Calculate the estimated maintenance calories based on the following details:
#     - Age: {age} years
#     - Height: {height} in
#     - Weight: {weight} lb
#     - Gender: {gender}
#     - Activity Level: {activity_level}
#     Use the Mifflin-St Jeor equation for the calculation and provide a numeric result.
#     """

#     # Use the 'chat' endpoint with the newer API
#     response = client.chat.completions.create(
#         model="gpt-4",  # You can use 'gpt-4' if you have access
#         messages=[
#             {"role": "system", "content": "You are a calculator that only outputs integers."},
#             {"role": "user", "content": prompt},
#         ]
#     )

#     # The response is now accessed through 'choices[0].message.content' as an attribute
#     return response.choices[0].message.content.strip()

def get_maintenance_calories(age, height_in_inches, weight_in_pounds, gender, activity_level):
    # Convert weight from pounds to kilograms and height from inches to centimeters
    weight_kg = weight_in_pounds * 0.453592
    height_cm = height_in_inches * 2.54
    
    # Calculate BMR using the Mifflin-St Jeor equation
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender == "Female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Adjust BMR based on activity level
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

def get_bulk_or_cut_calories(maintenance_calories, goal, timeframe):
    # Define bulk and cut percentages based on goal
    if goal == "Bulk":
        calorie_adjustment = 0.15  # Increase by 15% for bulking
    elif goal == "Cut":
        calorie_adjustment = -0.15  # Decrease by 15% for cutting

    # Adjust calories for bulk or cut
    adjustment = maintenance_calories * calorie_adjustment

    # Further adjust based on the timeframe
    # For example, a shorter timeframe may require a more aggressive adjustment
    if timeframe == "Short (1-2 months)":
        adjustment *= 1.2  # 20% more aggressive
    elif timeframe == "Medium (3-5 months)":
        adjustment *= 1.0  # Normal adjustment
    elif timeframe == "Long (6+ months)":
        adjustment *= 0.8  # Less aggressive

    return round(maintenance_calories + adjustment, 2)


# Title
st.title("Macro Mate")
main_logo = "newmacrologo.png"
sidebar_logo = st.logo(main_logo, size="large", link=None, icon_image=None)


# Details
st.sidebar.title("Details :clipboard:")
age = st.sidebar.slider("Age", min_value=1, max_value=99, value=1)
height = st.sidebar.slider("Height (in)", min_value=1, max_value=100, value=1)
weight = st.sidebar.slider("Weight (lb)", min_value=1, max_value=400, value=1)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])
goal = st.sidebar.selectbox("Goal", ["Maintain", "Bulk", "Cut"])
timeframe = st.sidebar.selectbox("Timeframe", ["Short (1-2 months)", "Medium (3-5 months)", "Long (6+ months)"])


if st.sidebar.button("Calculate Calories"):
    maintenance_calories = get_maintenance_calories(age, height, weight, gender, activity_level)
    
    if goal == "Maintain":
        result = maintenance_calories
        st.write(f"Estimated Maintenance Calories: {result} kcal/day")
    else:
        bulk_cut_calories = get_bulk_or_cut_calories(maintenance_calories, goal, timeframe)
        if goal == "Bulk":
            st.write(f"Estimated Bulking Calories: {bulk_cut_calories} kcal/day over {timeframe}")
        elif goal == "Cut":
            st.write(f"Estimated Cutting Calories: {bulk_cut_calories} kcal/day over {timeframe}")

# Goals
st.sidebar.title("Goals :chart_with_upwards_trend:")
strength  = st.sidebar.checkbox("Strength")
bodybuilding = st.sidebar.checkbox("Bodybuilding")
bulking = st.sidebar.checkbox("Bulking")
cutting = st.sidebar.checkbox("Cutting")

# Diet
st.sidebar.title("Dietary Choices :carrot:")
st.sidebar.header("Meals", divider = "blue")
breakfast = st.sidebar.checkbox("Breakfast")
lunch = st.sidebar.checkbox("Lunch")
dinner = st.sidebar.checkbox("Dinner")

st.sidebar.header("Allergies/Dietary Restrictions", divider="blue")
vegan = st.sidebar.checkbox("Vegan")
veg = st.sidebar.checkbox("Vegitarian")
monkey = st.sidebar.checkbox("Monkey")


st.write("## Main Section")
st.write("This section can be filled with additional features later.")

