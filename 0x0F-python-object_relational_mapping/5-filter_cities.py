#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
import logging

logging.basicConfig(level=logging.INFO)

def get_cities_from_state(user, password, db_name, state_name):
    """Gets all cities from a given state from the database hbtn_0e_0_usa

    Args:
        user (str): The user name for the database.
        password (str): The password for the database.
        db_name (str): The name of the database.
        state_name (str): The name of the state.

    Returns:
        list: A list of cities from the given state.
    """
    try:
        db = MySQLdb.connect(host="localhost", user=user,
                             passwd=password, db=db_name, port=3306)
        cur = db.cursor()
        cur.execute("""SELECT cities.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id
                    WHERE states.name=%s""", (state_name,))
        rows = cur.fetchall()
        cities = list(row[0] for row in rows)
        logging.info('Successfully retrieved cities from state.')
        return cities
    except Exception as e:
        logging.error('Error retrieving cities from state: %s', e)
    finally:
        cur.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        logging.error('Invalid number of arguments.')
        exit(1)
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    cities = get_cities_from_state(user, password, db_name, state_name)
    print(*cities, sep=", ")
