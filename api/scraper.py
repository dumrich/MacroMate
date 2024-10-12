import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
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
        
print()

