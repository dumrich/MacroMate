import mechanicalsoup

#Initialize the browser object
browser = mechanicalsoup.Browser()

#URL of the webpage with the nutritional data
url = "https://www.absecom.psu.edu/menus/user-pages/nutrition-label.cfm?mid=56080019"

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
#Print the extracted data
for key, value in nutrition_facts.items():
    data[key] = value
    
print(data)
    

