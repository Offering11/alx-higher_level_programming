#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""
import sys
import logging
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)

def get_state_id(username, password, db_name, state_name):
    """Gets the state id from the database

    Args:
        username (str): The username to connect to the database.
        password (str): The password to connect to the database.
        db_name (str): The name of the database.
        state_name (str): The name of the state to search for.

    Returns:
        int: The id of the state if found, otherwise None.
    """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == state_name)
    try:
        return instance[0].id
    except IndexError:
        logging.warning(f'State "{state_name}" not found in database.')
        return None

if __name__ == "__main__":
    state_id = get_state_id(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    if state_id:
        print(state_id)
    else:
        print("Not found")
