#!/usr/bin/python3
"""
Script that lists only the first State objects from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City


def fetch_state():
    """Func where we fetch states from database """

    username, passwd, db = sys.argv[1:]

    # create connect to database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{passwd}@localhost/{db}',
            pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    # create session for transaction
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new entries to session
    state = State(name="California")
    city = City(name="San Francisco", state=state)
    session.add_all([state, city])

    # commit and close session
    session.commit()
    session.close()


if __name__ == '__main__':
    fetch_state()
