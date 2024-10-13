from sqlalchemy.orm import Session
import models
from models import SessionLocal, DiningHall, Menu, Food, Allergen, DietaryRestriction
from fastapi import FastAPI, Request,Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from models import User, SessionLocal
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPEN_AI')

# Initialize FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dining_halls/")
def create_dining_hall(name: str, db: Session = Depends(get_db)):
    new_hall = DiningHall(name=name)
    db.add(new_hall)
    db.commit()
    db.refresh(new_hall)
    return new_hall

@app.get("/dining_halls/")
def get_dining_halls(db: Session = Depends(get_db)):
    return db.query(DiningHall).all()

@app.post("/menus/")
def create_menu(menu_type: str, dining_hall_id: int, db: Session = Depends(get_db)):
    new_menu = Menu(menu_type=menu_type, dining_hall_id=dining_hall_id)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu

@app.get("/dining_halls/{dining_hall_id}/menus")
def get_menus_for_dining_hall(dining_hall_id: int, db: Session = Depends(get_db)):
    return db.query(Menu).filter(Menu.dining_hall_id == dining_hall_id).all()

@app.post("/foods/")
def create_food(name: str, calories: int, proteins: float, fats: float, sugars: float, menu_id: int, db: Session = Depends(get_db)):
    new_food = Food(name=name, calories=calories, proteins=proteins, fats=fats, sugars=sugars, menu_id=menu_id)
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food

@app.get("/menus/{menu_id}/foods")
def get_foods_for_menu(menu_id: int, db: Session = Depends(get_db)):
    return db.query(Food).filter(Food.menu_id == menu_id).all()

@app.post("/allergens/")
def create_allergen(name: str, db: Session = Depends(get_db)):
    new_allergen = Allergen(name=name)
    db.add(new_allergen)
    db.commit()
    db.refresh(new_allergen)
    return new_allergen

@app.post("/foods/{food_id}/add_allergen/{allergen_id}")
def add_allergen_to_food(food_id: int, allergen_id: int, db: Session = Depends(get_db)):
    food_item = db.query(Food).filter(Food.id == food_id).first()
    allergen = db.query(Allergen).filter(Allergen.id == allergen_id).first()
    food_item.allergens.append(allergen)
    db.commit()
    return {"message": f"Allergen {allergen.name} added to food {food_item.name}"}

@app.post("/dietary_restrictions/")
def create_dietary_restriction(restriction: str, db: Session = Depends(get_db)):
    new_restriction = DietaryRestriction(restriction=restriction)
    db.add(new_restriction)
    db.commit()
    db.refresh(new_restriction)
    return new_restriction

@app.post("/foods/{food_id}/add_dietary_restriction/{dietary_id}")
def add_dietary_restriction_to_food(food_id: int, dietary_id: int, db: Session = Depends(get_db)):
    food_item = db.query(Food).filter(Food.id == food_id).first()
    dietary_restriction = db.query(DietaryRestriction).filter(DietaryRestriction.id == dietary_id).first()
    food_item.dietary_restrictions.append(dietary_restriction)
    db.commit()
    return {"message": f"Dietary restriction {dietary_restriction.restriction} added to food {food_item.name}"}

def query(menu, macros, restrictions, query):
    response = openai.chat.completion.create(model="gpt-4o", temperature=0.9, top_p=0.3
                                          messages=[
    {
      "role": "system",
      "content": f"From the following menu items (with nutrition included), list the items that I should have for breakfast, lunch, and dinner. Menu: {menu}. These are my macros: {macros}. These are my dietary restrictions: {diet}"
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{query}"
        }
      ]
    }])
    return response.choices[0].message.content

@app.post("/query/")
def user_query(request: Request):
    input = await request.json()
    
    query = data.get("name")
    menu = data.get("menu_id")
    macros = {}
    restrictions = {}
    
    return {"response": query(menu, macros, restrictions, query)}
