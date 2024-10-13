from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./dining_halls.db"

# Create the SQLite engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Define the base model for SQLAlchemy
Base = declarative_base()

# Create a SessionLocal class for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Define associations for many-to-many relationships
food_allergen_association = Table(
    'food_allergen_association',
    Base.metadata,
    Column('food_id', Integer, ForeignKey('foods.id')),
    Column('allergen_id', Integer, ForeignKey('allergens.id'))
)

food_dietary_association = Table(
    'food_dietary_association',
    Base.metadata,
    Column('food_id', Integer, ForeignKey('foods.id')),
    Column('dietary_id', Integer, ForeignKey('dietary_restrictions.id'))
)

#Models
class DiningHall(Base):
    __tablename__ = 'dining_halls'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    # Relationship with Menu
    menus = relationship("Menu", back_populates="dining_hall")

class Menu(Base):
    __tablename__ = 'menus'
    
    id = Column(Integer, primary_key=True, index=True)
    menu_type = Column(String, nullable=False) #Breakfast, Lunch, or Dinner
    dining_hall_id = Column(Integer, ForeignKey('dining_halls.id'))

    dining_hall = relationship("DiningHall", back_populates="menus")
    foods = relationship("Food", back_populates="menu", cascade="all, delete-orphan")

class Food(Base):
    __tablename__ = 'foods'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # e.g., "Scrambled Eggs", "Pancakes"
    calories = Column(Integer)
    proteins = Column(Float)
    fats = Column(Float)
    sugars = Column(Float)

    allergens = relationship("Allergen", secondary=food_allergen_association, back_populates="foods", cascade="all, delete")
    dietary_restrictions = relationship('DietaryRestriction', secondary=food_dietary_association, back_populates="foods", cascade="all, delete")

    menu_id = Column(Integer, ForeignKey('menus.id'))
    
    # Relationship with Menu
    menu = relationship("Menu", back_populates="foods")

class Allergen(Base):
    __tablename__ = 'allergens'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)  # e.g., "Milk", "Eggs", "Peanuts"
    
    # Relationship with Food through association table
    foods = relationship("Food", secondary=food_allergen_association, back_populates="allergens")

class DietaryRestriction(Base):
    __tablename__ = 'dietary_restrictions'

    id = Column(Integer, primary_key=True, index=True)
    restriction = Column(String, unique=True, nullable=False)  # e.g., "Gluten friendly", "Halal Friendly"
    
    # Relationship with Food through association table
    foods = relationship("Food", secondary=food_dietary_association, back_populates="dietary_restrictions")

# Create the tables in the database
Base.metadata.create_all(bind=engine)