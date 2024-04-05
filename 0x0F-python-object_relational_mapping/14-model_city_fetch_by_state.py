#!/usr/bin/python3
"""
Script that lists only the first State objects from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City


def fetch_city():
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

    # Create query to database
    result = (
            session.query(State)
            .join(City)
            .order_by(City.id)
            .all()
        )

    # Print result for state, city in result:
    for state in result:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    # close session
    session.close()


if __name__ == '__main__':
    fetch_city()
