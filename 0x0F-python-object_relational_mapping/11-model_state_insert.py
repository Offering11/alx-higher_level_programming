#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""

import sys
import logging
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get database credentials from command line arguments
DB_USER = sys.argv[1]
DB_PASSWORD = sys.argv[2]
DB_NAME = sys.argv[3]

# Create engine
engine = create_engine(f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@localhost:3306/{DB_NAME}')

# Create all tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create new state
state_name = 'Louisiana'
new_state = State(name=state_name)

# Add new state to session
session.add(new_state)

# Query for new state
new_state_instance = session.query(State).filter_by(name=state_name).first()

# Print new state ID
logging.info(f'New state {state_name} ID: {new_state_instance.id}')

# Commit changes
session.commit()
