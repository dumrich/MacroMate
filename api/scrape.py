import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.absecom.psu.edu/menus/user-pages/daily-menu.cfm")

# Get the current page
page = browser.get_current_page()
menu_divs = page.find_all("div", class_="menu-items")



#Iterate through each divider to extract menu items
for div in menu_divs:
    
    #Find all <a> tags within the div (the menu items)
    item_links = div.find_all("a", href=True)
    
    for item in item_links:
        item_text = item.get_text(strip=True)
        item_href = item["href"]
        
        #Find indicators 
        indicators = div.find_all("img", alt=True)
        indicator_labels = [img["alt"] for img in indicators]
        
        print(f"Menu Item: {item_text} \n   Indicators: {', '.join(indicator_labels)} \n   URL: {item_href}")


browser.close()

verbose=True

