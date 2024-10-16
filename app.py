import streamlit as st
import matplotlib.pyplot as plt
import requests


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



def get_nutrients():
    maintenance_calories = get_maintenance_calories(age, height, weight, gender, activity_level)
    
    if goal == "Maintain":
        result = maintenance_calories
    else:
        result = get_bulk_or_cut_calories(maintenance_calories, goal, timeframe)
    
    default_carbs_g = (0.5 * result) / 5  # 50% of calories from carbs
    default_proteins_g = (0.25 * result) / 6  # 25% of calories from proteins
    default_fats_g = (0.20 * result) / 9  # 20% of calories from fats

    dict = {"carbohydrates": default_carbs_g, "proteins": default_proteins_g, "fats": default_fats_g}

    return dict
    
    

# Calculate maintenance calories


# Diet
st.sidebar.title("Dietary Choices :carrot:")
st.sidebar.header("Meals", divider = "blue")
breakfast = st.sidebar.checkbox("Breakfast")
lunch = st.sidebar.checkbox("Lunch")
dinner = st.sidebar.checkbox("Dinner")

st.sidebar.header("Allergies/Dietary Restrictions", divider="blue")
# Allergies
coconut = st.sidebar.checkbox("Coconut")
dairy = st.sidebar.checkbox("Dairy")
eggs = st.sidebar.checkbox("Eggs")
fish = st.sidebar.checkbox("Fish")
peanuts = st.sidebar.checkbox("Peanuts")
sesame = st.sidebar.checkbox("Sesame")
shellfish = st.sidebar.checkbox("Shellfish")
soy = st.sidebar.checkbox("Soy")
tree_nuts = st.sidebar.checkbox("Tree Nuts")
wheat_gluten = st.sidebar.checkbox("Wheat/Gluten")


halal_friendly = st.sidebar.checkbox("Halal Friendly")
gluten_friendly = st.sidebar.checkbox("Gluten Friendly")
meatless = st.sidebar.checkbox("Meatless")
contains_pork = st.sidebar.checkbox("Contains Pork")
vegan = st.sidebar.checkbox("Vegan") 

diningHall = st.sidebar.selectbox("Hall", ["east", "west", "north", "south", "pollock"])

restrictions = {
    "coconut": coconut,
    "dairy": dairy,
    "eggs": eggs,
    "fish": fish,
    "peanuts": peanuts,
    "sesame": sesame,
    "shellfish": shellfish,
    "soy": soy,
    "tree_nuts": tree_nuts,
    "wheat_gluten": wheat_gluten,
    "halal_friendly": halal_friendly,
    "gluten_friendly": gluten_friendly,
    "meatless": meatless,
    "contains_pork": contains_pork,
    "vegan": vegan,
}





#######################################################


API_URL = "http://104.39.68.161:8000/query/"

# Function to query the API
def query_llm_api(user_input):
    headers = {"Content-Type": "application/json"}
    data = {
        "query": user_input,
        "menu_id": diningHall,  # Placeholder variable, replace with real value if needed
        "macros": get_nutrients(),  # Placeholder function, replace with real logic
        "restrictions": restrictions,
    }
    print(data)

    try:
        response = requests.post(API_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("response", "Error: No response received")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


user_input = None
# Function to handle conversation flow
def make_query(query):
    # Initialize conversation history if not already present
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = []

    # Get response from the API
    llm_response = query_llm_api(query)

    # Append user and bot messages to conversation history
    st.session_state["conversation"].append(f"You: {query}")
    st.session_state["conversation"].append(f"Bot: {llm_response}")

    # Display chat history
    for i, message in enumerate(st.session_state["conversation"]):
        if "You:" in message:
            st.markdown(f"""
            <div style='
                background-color: #f0f0f0;
                color: #000;
                padding: 15px;
                border-radius: 20px;
                margin: 10px 0;
                max-width: 70%;
                box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
                font-family: Arial, sans-serif;
                font-size: 16px;
                align-self: flex-start;
            '>
            {message}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='
                background-color: #007bff;
                color: #fff;
                padding: 15px;
                border-radius: 20px;
                margin: 10px 0;
                max-width: 70%;
                box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
                font-family: Arial, sans-serif;
                font-size: 16px;
                align-self: flex-end;
            '>
            {message}
            </div>
            """, unsafe_allow_html=True)

    # Clear the input field after submission
    user_input = st.text_input("You:", value="", key="input_clear")

# Function to generate a diet plan with a pie chart
def gen_diet(spec):
    # Placeholder function, replace with your actual calorie calculation logic
    maintenance_calories = 2000  # Example value, replace with `get_maintenance_calories()`
    
    if goal == "Maintain":
        result = maintenance_calories
    else:
        result = 2500  # Example value, replace with `get_bulk_or_cut_calories()`

    st.write(f"Estimated Calories: {result} kcal/day")

    
    default_carbs_g = (0.5 * result) / 5  # 50% of calories from carbs
    default_proteins_g = (0.25 * result) / 6  # 25% of calories from proteins
    default_fats_g = (0.20 * result) / 9  # 20% of calories from fats

    # Pie chart for macronutrient breakdown
    labels = ['Carbohydrates', 'Proteins', 'Fats']
    sizes = [default_carbs_g, default_proteins_g, default_fats_g]
    colors = ['#FF9999', '#66B2FF', '#1CAC78']
    explode = (0.1, 0, 0)  # Explode the carbs slice slightly

    fig, ax = plt.subplots(figsize=(2, 2))

    # Set both figure and axes background color
    fig.patch.set_facecolor('#0e1117')  # Set figure background color
    ax.set_facecolor('#0e1117')  # Set background color for the axes

    label_color = 'white'
    font_size = 10  # Set your desired font size

    ax.pie(sizes, explode=explode, labels=labels, colors=colors, startangle=90, 
        autopct=lambda p: f'{int(p / 100 * sum(sizes))} g' if p > 0 else '',
        textprops={'color': label_color, 'fontsize': font_size})

    st.pyplot(fig)

    # LLM Response (after generating diet plan)
    make_query(spec)

# Sidebar Button for Generating Diet
if st.sidebar.button("Generate Diet"):
    gen_diet("Generate a diet based on my dietary restrictions and macros")

# Handling user input
if user_input:
    gen_diet(user_input)
