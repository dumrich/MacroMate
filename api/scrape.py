import mechanicalsoup
import json

browser = mechanicalsoup.StatefulBrowser()

class Food:
    def __init__(self, name, nut_dict):
        self._entree = name
        self._nutrition = nut_dict

    # Getters
    @property
    def entree(self):
        return self._entree

    @property
    def nutrition(self):
        return self._nutrition

    # Setters
    @entree.setter
    def entree(self, name):
        if isinstance(name, str):
            self._entree = name
        else:
            raise TypeError("Entree must be a string.")

    @nutrition.setter
    def nutrition(self, nut_dict):
        if isinstance(nut_dict, dict):
            self._nutrition = nut_dict
        else:
            raise TypeError("Nutrition must be a dictionary.")

    def __str__(self):
        # Create a string representation of the food item and its nutrition facts
        nutrition_info = ", ".join([f"{key}: {value}" for key, value in self._nutrition.items()])
        return f"{self._entree} ({nutrition_info})"
    
    __repr__ = __str__


class Menu:
    def __init__(self, name):
        self.menus = []
        self.name = "".join(name.split(" "))

    def add_menu(self, menu):
        self.menus.append(menu)


    def __str__(self):
        return (f"Breakfast: {self.menus[0]}"
                f"Lunch: {self.menus[1]}"
                f"Dinner: {self.menus[2]}")
        
    __repr__ = __str__


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
    dining_halls = {"east": "11",
                    "north": "17",
                    "south": "13",
                    "west": "16",
                    "pollock": "14"}

    meals = ["Breakfast", "Lunch", "Dinner"]

    response_data = {}

    for hall in dining_halls:
        browser.select_form('#frmMenuFilters')
        browser["selCampus"] = dining_halls[hall]

        response = browser.submit_selected()

        response_data[hall] = [] 
        for meal in meals:
            browser.select_form('#frmMenuFilters')
            browser["selMeal"] = meal 

            response = browser.submit_selected()
            soup = response.soup

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
        
        
def main():
    # Get menu links
    menus = get_menu_links()
    
    overall = []
    for hall, pages in menus.items():
        m = Menu(hall)
        
        for i, page in enumerate(pages):
            food_links = get_food_links(page)
            foods = {}
           
            for food in food_links:
                nut_data = nutrition(food["url"])  # Call nutrition function for each food item
                food_item = Food(food["name"], nut_data)
                foods[food["name"]] = food_item

            m.add_menu(foods)
        overall.append(m)
    return overall


data = main()
for d in data:
    with open(d.name, "w") as json_file:
        json.dump(str(d), json_file, indent=4)
