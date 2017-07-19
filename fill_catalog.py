from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


# engine = create_engine('sqlite:///catalog.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Delete all the categories to avoid repetition
# session.query(Category).delete()
# session.commit()

# Delete all the items to avoid repetition
# session.query(Item).delete()
# session.commit()

# Start new entries

# Creating a new Category
category1 = Category(name="Cricket")
session.add(category1)
session.commit()

# Creating an item in the category
item1 = Item(name="Bat", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item1)
session.commit()

item1 = Item(name="Ball", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item1)
session.commit()

item2 = Item(name="Batting Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item2)
session.commit()

item3 = Item(name="Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item3)
session.commit()

item4 = Item(name="Leg Pads", description="Leg pads serve to protect the legs from impact by a hard ball or puck at high speed which could otherwise cause injuries to the lower leg.",
                     price="$7.50", size="Large", category=category1)
session.add(item4)
session.commit()

item5 = Item(name="Wicket-keeper's Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item5)
session.commit()

item6 = Item(name="Abdominal Guard", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category1)
session.add(item6)
session.commit()

category2 = Category(name="Hockey")
session.add(category2)
session.commit()

item7 = Item(name="Stick", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category2)
session.add(item7)
session.commit()

item8 = Item(name="Hockey Ball", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category2)
session.add(item8)
session.commit()

item9 = Item(name="Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category2)
session.add(item9)
session.commit()

item10 = Item(name="Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category2)
session.add(item10)
session.commit()

item11 = Item(name="Leg pads", description="Leg pads serve to protect the legs from impact by a hard ball or puck at high speed which could otherwise cause injuries to the lower leg.",
                     price="$7.50", size="Large", category=category2)
session.add(item11)
session.commit()

item12 = Item(name="Abdominal guard", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category2)
session.add(item12)
session.commit()

category3 = Category(name="Football")
session.add(category3)
session.commit()

item13 = Item(name="Soccer Cleats", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category3)
session.add(item13)
session.commit()

item14 = Item(name="Soccer Ball", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category3)
session.add(item14)
session.commit()

item15 = Item(name="Goalkeeper's Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category3)
session.add(item15)
session.commit()

item16 = Item(name="Shin Guards", description="Shin guards serve to protect the legs from impact by a hard ball or puck at high speed which could otherwise cause injuries to the lower leg.",
                     price="$7.50", size="Large", category=category3)
session.add(item16)
session.commit()

item17 = Item(name="Abdominal guard", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category3)
session.add(item17)
session.commit()

category4 = Category(name="Tennis")
session.add(category4)
session.commit()

item18 = Item(name="Tennis Racquet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category4)
session.add(item18)
session.commit()

item19 = Item(name="Tennis Ball", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category4)
session.add(item19)
session.commit()

category5 = Category(name="Baseball")
session.add(category5)
session.commit()

item20 = Item(name="Bat", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item20)
session.commit()

item21 = Item(name="Baseballs", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item21)
session.commit()

item22 = Item(name="Batting Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item22)
session.commit()

item1 = Item(name="Batter's Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item1)
session.commit()

item1 = Item(name="Leg Guards", description="Leg pads serve to protect the legs from impact by a hard ball or puck at high speed which could otherwise cause injuries to the lower leg.",
                     price="$7.50", size="Large", category=category5)
session.add(item1)
session.commit()

item1 = Item(name="Catcher's Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item1)
session.commit()

item1 = Item(name="Chest Protectors", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item1)
session.commit()

item1 = Item(name="Abdominal guard", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category5)
session.add(item1)
session.commit()

category6 = Category(name="Biking")
session.add(category6)
session.commit()

item1 = Item(name="Mountain Bike", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$500.00", size="Medium", category=category6)
session.add(item1)
session.commit()

item1 = Item(name="Road Bike", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$800.00", size="Large", category=category6)
session.add(item1)
session.commit()

item1 = Item(name="Commute Bike", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$450.00", size="Large", category=category6)
session.add(item1)
session.commit()

item1 = Item(name="Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category6)
session.add(item1)
session.commit()

item1 = Item(name="Comfy seat", description="Leg pads serve to protect the legs from impact by a hard ball or puck at high speed which could otherwise cause injuries to the lower leg.",
                     price="$8.50", size="Large", category=category6)
session.add(item1)
session.commit()

item1 = Item(name="Bike Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category6)
session.add(item1)
session.commit()


category7 = Category(name="Snowboarding")
session.add(category7)
session.commit()


item1 = Item(name="Snow Board", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category7)
session.add(item1)
session.commit()

item1 = Item(name="Winter Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category7)
session.add(item1)
session.commit()

item1 = Item(name="Helmet", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Medium", category=category7)
session.add(item1)
session.commit()

item1 = Item(name="Sun-glasses", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category7)
session.add(item1)
session.commit()


category8 = Category(name="Skiing")
session.add(category8)
session.commit()


item1 = Item(name="Snow Jacket", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category8)
session.add(item1)
session.commit()

item1 = Item(name="Jumper", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category8)
session.add(item1)
session.commit()

item1 = Item(name="Ski Gloves", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category8)
session.add(item1)
session.commit()

item1 = Item(name="Ski Poles", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category8)
session.add(item1)
session.commit()


category9 = Category(name="Volleyball")
session.add(category9)
session.commit()


item1 = Item(name="Shorts", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category9)
session.add(item1)
session.commit()

item1 = Item(name="Ball", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category9)
session.add(item1)
session.commit()

item1 = Item(name="Net", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category9)
session.add(item1)
session.commit()

item1 = Item(name="Poles", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$7.50", size="Large", category=category9)
session.add(item1)
session.commit()

category10 = Category(name="Basketball")
session.add(category10)
session.commit()

category11 = Category(name="Fencing")
session.add(category11)
session.commit()

item1 = Item(name="Sword", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$200.00", size="Large", category=category11)
session.add(item1)
session.commit()

item2 = Item(name="Plastron", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$100.00", size="Large", category=category11)
session.add(item2)
session.commit()

item3 = Item(name="Glove", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$20.00", size="Large", category=category11)
session.add(item3)
session.commit()

item4 = Item(name="Chest protector", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$150.50", size="Large", category=category11)
session.add(item4)
session.commit()

item5 = Item(name="Mask", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$175.50", size="Large", category=category11)
session.add(item5)
session.commit()

item6 = Item(name="Breeches/Knickers ", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget ligula convallis, pellentesque tortor id, aliquet dui. Vestibulum vulputate ultricies nisi. Vivamus fringilla lacinia sodales.",
                     price="$178.50", size="Large", category=category11)
session.add(item6)
session.commit()
