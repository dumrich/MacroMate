import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()

class Food:
    def __init__(self, name, nut_dict):
        self.entree = name
        self.nutrition = nut_dict  
    
    def __str__(self):
        #Create a string representation of the food item and its nutrition facts
        nutrition_info = ", ".join([f"{key}: {value}" for key, value in self.nutrition.items()])
        return f"{self.entree} ({nutrition_info})"
    
    __repr__ = __str__


class Menu:
    def __init__(self, breakfast=None, lunch=None, dinner=None):
        self.breakfast = breakfast if breakfast else []
        self.lunch = lunch if lunch else []
        self.dinner = dinner if dinner else []

    def __str__(self):
        #Create a string representation of the menu
        breakfast_items = "\n".join([str(food) for food in self.breakfast])
        lunch_items = "\n".join([str(food) for food in self.lunch])
        dinner_items = "\n".join([str(food) for food in self.dinner])
        return (f"Breakfast:\n{breakfast_items}\n\n"
                f"Lunch:\n{lunch_items}\n\n"
                f"Dinner:\n{dinner_items}")
        
    __repr__ = __str__


class DiningHall(Menu):
    def __init__(self, name, breakfast=None, lunch=None, dinner=None):
        super().__init__(breakfast, lunch, dinner)
        self.name = name  # Store the name of the dining hall
    
    def __str__(self):
        # Create a string representation of the dining hall and its menu
        return f"{self.name} Dining Hall:\n{super().__str__()}"


# menu
#   B L D
# dinning hall
#   one of the dining halls with each breakfast lunch and dinner
# food 
    #nutrition 





#Gets nutriton of every food item 
def nutrition(link):
    url = link 

    #Request the page
    page = browser.get(url)
    soup = page.soup  # Use .soup to access the parsed HTML

    #Extract nutritional data
    nutrition_facts = {}

    #Find all <b> tags and search for the relevant text
    b_tags = soup.find_all('b')

    for b_tag in b_tags:
        #Check the text and extract data accordingly
        if 'Serving Size:' in b_tag.text:
            nutrition_facts['Serving Size'] = b_tag.next_sibling.strip()
        elif 'Calories:' in b_tag.text:
            nutrition_facts['Calories'] = b_tag.next_sibling.strip()
        elif 'Calories from Fat:' in b_tag.text:
            nutrition_facts['Calories from Fat'] = b_tag.next_sibling.strip()
        elif 'Total Fat' in b_tag.text:
            nutrition_facts['Total Fat'] = b_tag.next_sibling.strip()
        elif 'Sat Fat' in b_tag.text:
            nutrition_facts['Sat Fat'] = b_tag.next_sibling.strip()
        elif 'Total Carb' in b_tag.text:
            nutrition_facts['Total Carb'] = b_tag.next_sibling.strip()
        elif 'Dietary Fiber' in b_tag.text:
            nutrition_facts['Dietary Fiber'] = b_tag.next_sibling.strip()
        elif 'Trans Fat' in b_tag.text:
            nutrition_facts['Trans Fat'] = b_tag.next_sibling.strip()
        elif 'Sugars' in b_tag.text:
            nutrition_facts['Sugars'] = b_tag.next_sibling.strip()
        elif 'Cholesterol' in b_tag.text:
            nutrition_facts['Cholesterol'] = b_tag.next_sibling.strip()
        elif 'Sodium' in b_tag.text:
            nutrition_facts['Sodium'] = b_tag.next_sibling.strip()
        elif 'Protein' in b_tag.text:
            nutrition_facts['Protein'] = b_tag.next_sibling.strip()

    data = {}
    
    #extracted data
    for key, value in nutrition_facts.items():
        data[key] = value
        
    return(data)


#Get menu data from each day 
def get_menu_links():
    url = 'https://www.absecom.psu.edu/menus/user-pages/daily-menu.cfm'

    main_page = browser.open(url)

    # List of form options
    dining_halls = {"East Food District Findlay": "11",
                    "North Food District Warnock": "17",
                    "South Food District Redifer": "13",
                    "West Food District Waring": "16",
                    "Pollock Dining Commons": "14"}

    meals = ["Breakfast", "Lunch", "Dinner"]

    response_data = {}

    for hall in dining_halls:
        browser.select_form('#frmMenuFilters')
        browser["selCampus"] = dining_halls[hall]

        response = browser.submit_selected()

        for meal in meals:
            browser.select_form('#frmMenuFilters')
            browser["selMeal"] = meal 

            response = browser.submit_selected()
            soup = response.soup

            response_data[hall] = [] 
            response_data[hall].append(soup)
            
    return response_data
            

#Get tags and each food link 
def get_food_links(page):
    menu_divs = page.find_all("div", class_="menu-items")
    food_items = []

    #Iterate through each divider to extract menu items
    for div in menu_divs:
        
        #Find all <a> tags within the div (the menu items)
        item_links = div.find_all("a", href=True)
        
        for item in item_links:
            item_text = item.get_text(strip=True)
            item_href = 'https://www.absecom.psu.edu/menus/user-pages/' + item["href"]
            
            #Find indicators 
            indicators = div.find_all("img", alt=True)
            indicator_labels = [img["alt"] for img in indicators]
            
            food_items.append({
                "name": item_text,
                "url": item_href,
                "indicators": indicator_labels
            })            
            
            return food_items
            # return (f"Menu Item: {item_text} \n   Indicators: {', '.join(indicator_labels)} \n   URL: {item_href}")
        
        
verbose=True

def main():
    # Get menu links
    menus = get_menu_links()

    for hall, pages in menus.items():
        for page in pages:
            food_links = get_food_links(page)
            
            for food in food_links:
                nut_data = nutrition(food["url"])  # Call nutrition function for each food item
                food_item = Food(food["name"], nut_data)
                print(food_item)  # Print or store the Food object as needed

main()

verbose = True