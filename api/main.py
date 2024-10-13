from sqlalchemy.orm import Session
import models
from models import SessionLocal, DiningHall, Menu, Food, Allergen, DietaryRestriction
from fastapi import FastAPI, Request, Depends
import openai, os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = "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"

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# 
# @app.post("/dining_halls/")
# def create_dining_hall(name: str, db: Session = Depends(get_db)):
#     new_hall = DiningHall(name=name)
#     db.add(new_hall)
#     db.commit()
#     db.refresh(new_hall)
#     return new_hall
# 
# @app.get("/dining_halls/")
# def get_dining_halls(db: Session = Depends(get_db)):
#     return db.query(DiningHall).all()
# 
# @app.post("/menus/")
# def create_menu(menu_type: str, dining_hall_id: int, db: Session = Depends(get_db)):
#     new_menu = Menu(menu_type=menu_type, dining_hall_id=dining_hall_id)
#     db.add(new_menu)
#     db.commit()
#     db.refresh(new_menu)
#     return new_menu
# 
# @app.get("/dining_halls/{dining_hall_id}/menus")
# def get_menus_for_dining_hall(dining_hall_id: int, db: Session = Depends(get_db)):
#     return db.query(Menu).filter(Menu.dining_hall_id == dining_hall_id).all()
# 
# @app.post("/foods/")
# def create_food(name: str, calories: int, proteins: float, fats: float, sugars: float, menu_id: int, db: Session = Depends(get_db)):
#     new_food = Food(name=name, calories=calories, proteins=proteins, fats=fats, sugars=sugars, menu_id=menu_id)
#     db.add(new_food)
#     db.commit()
#     db.refresh(new_food)
#     return new_food
# 
# @app.get("/menus/{menu_id}/foods")
# def get_foods_for_menu(menu_id: int, db: Session = Depends(get_db)):
#     return db.query(Food).filter(Food.menu_id == menu_id).all()
# 
# @app.post("/allergens/")
# def create_allergen(name: str, db: Session = Depends(get_db)):
#     new_allergen = Allergen(name=name)
#     db.add(new_allergen)
#     db.commit()
#     db.refresh(new_allergen)
#     return new_allergen
# 
# @app.post("/foods/{food_id}/add_allergen/{allergen_id}")
# def add_allergen_to_food(food_id: int, allergen_id: int, db: Session = Depends(get_db)):
#     food_item = db.query(Food).filter(Food.id == food_id).first()
#     allergen = db.query(Allergen).filter(Allergen.id == allergen_id).first()
#     food_item.allergens.append(allergen)
#     db.commit()
#     return {"message": f"Allergen {allergen.name} added to food {food_item.name}"}
# 
# @app.post("/dietary_restrictions/")
# def create_dietary_restriction(restriction: str, db: Session = Depends(get_db)):
#     new_restriction = DietaryRestriction(restriction=restriction)
#     db.add(new_restriction)
#     db.commit()
#     db.refresh(new_restriction)
#     return new_restriction
# 
# @app.post("/foods/{food_id}/add_dietary_restriction/{dietary_id}")
# def add_dietary_restriction_to_food(food_id: int, dietary_id: int, db: Session = Depends(get_db)):
#     food_item = db.query(Food).filter(Food.id == food_id).first()
#     dietary_restriction = db.query(DietaryRestriction).filter(DietaryRestriction.id == dietary_id).first()
#     food_item.dietary_restrictions.append(dietary_restriction)
#     db.commit()
#     return {"message": f"Dietary restriction {dietary_restriction.restriction} added to food {food_item.name}"}

def queries(menu, macros, restrictions, query):
    response = openai.chat.completions.create(model="gpt-4o", temperature=0.9, top_p=0.3, messages=[
    {
      "role": "system",
      "content": f"From the following menu items (with nutrition included), list the items that I should have for breakfast, lunch, and dinner. Menu: {menu}. These are my macros: {macros}. These are my dietary restrictions: {restrictions}"
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"From the following menu items (with nutrition included), list the items that I should have for breakfast, lunch, and dinner. Make ABSOLUTELY sure that the menu items meet the macros completely. They can exceed by a maximum of 15%, but should follow the ratio somewhat accurately. You can add multiple portions of each meal if that makes it easier. Menu: {menu}. These are my macros: {macros}. These are my dietary restrictions: {restrictions}. {query}"
        }
      ]
    }])
    return response.choices[0].message.content

@app.post("/query/")
async def user_query(request: Request):
    data = await request.json()
    
    query = data.get("query")
    menu = data.get("menu_id")
    with open(menu, 'r') as json_file:
        mm = json.load(json_file)  # Load JSON data into a Python dictionary
    json_string = json.dumps(mm, indent=4)

    macros = data.get("macros")
    restrictions = data.get("restrictions")

    couples = queries(json_string, macros, restrictions, query)
    print(couples)
    
    return {"response": couples}

# @app.get("/foods/{food_id}/allergens")
# def get_food_allergens(food_id: int, db: Session = Depends(get_db)):
#     # Query the Food item with the given food_id
#     food_item = db.query(Food).filter(Food.id == food_id).first()
#     
#     # Check if the food item exists
#     if not food_item:
#         return {"error": "Food item not found"}
#     
#     # Get the allergens associated with the food item
#     allergens = [allergen.name for allergen in food_item.allergens]
#     
#     return {"allergens": allergens}
# 
# @app.get("/foods/{food_id}/dietary_restrictions")
# def get_food_dietary_restrictions(food_id: int, db: Session = Depends(get_db)):
#     # Query the Food item with the given food_id
#     food_item = db.query(Food).filter(Food.id == food_id).first()
#     
#     # Check if the food item exists
#     if not food_item:
#         return {"error": "Food item not found"}
#     
#     # Get the dietary_restrictions associated with the food item
#     dietary_restrictions = [dietary_restriction.restriction for dietary_restriction in food_item.dietary_restrictions]
#     
#     return {"dietary_restrictions": dietary_restrictions}
# 
# @app.get('/menus/{menu_id}/foods/json')
# def get_food_menu_JSON(menu_id: int, db: Session = Depends(get_db)):
#     menu = db.query(Menu).filter(Menu.id == menu_id).first()
# 
#     # Check if the menu exists
#     if not menu:
#         return {"error": "Menu not found"}
# 
#     return menu_as_json(menu)
# 
# @app.get('/dining_halls/{dining_hall_id}/menus/json')
# def get_dining_hall_food_menus_JSON(dining_hall_id: int, db: Session = Depends(get_db)):
#     dining_hall = db.query(DiningHall).filter(DiningHall.id == dining_hall_id).first()
# 
#     # Check if the menu exists
#     if not dining_hall:
#         return {"error": "Menu not found"}
#     
#     formatted_json = {dining_hall.name: {}}
# 
#     for menu in dining_hall.menus:
#         formatted_json[dining_hall.name].update(menu_as_json(menu))
# 
#     return formatted_json
# 
# #Helper method for converting Menu models into full menu ----------------------------------------
# def menu_as_json(menu: Menu):
# 
#     formatted_json = {menu.menu_type: []}
# 
#     for food in menu.foods:
# 
#         #Get allergens and dietary restrictions for each good
#         allergens = [allergen.name for allergen in food.allergens]
#         dietary_restrictions = [dietary_restriction.restriction for dietary_restriction in food.dietary_restrictions]
# 
#         food_info = {
#             'name': food.name,
#             'calories': food.calories,
#             'proteins': food.proteins,
#             'fats': food.fats,
#             'sugars': food.sugars,
#             'allergens': allergens,
#             'dietary_restrictions': dietary_restrictions
#         }
# 
#         formatted_json[menu.menu_type].append(food_info)
# 
#     return formatted_json
