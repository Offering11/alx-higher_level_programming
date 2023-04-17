#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""
import sys
import logging
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)

def delete_states_with_name_containing_a(user, password, db_name):
    """Deletes all states with names containing 'a' from the database

    Args:
        user (str): Database user
        password (str): Database password
        db_name (str): Database name
    """
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for instance in session.query(State).filter(State.name.like('%a%')):
            session.delete(instance)
        session.commit()
        logging.info('States with names containing "a" were successfully deleted from the database')
    except Exception as e:
        logging.error(f'An error occurred while deleting states from the database: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        logging.error('Incorrect number of arguments provided')
    else:
        delete_states_with_name_containing_a(sys.argv[1], sys.argv[2], sys.argv[3])
