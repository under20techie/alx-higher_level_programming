#!/usr/bin/python3
"""
Script that lists only the first State objects from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City


def state_city_fetch():
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
            .outerjoin(City.state)
            .order_by(City.id)
            .all()
        )

    # Print result
    for state in result:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")

    # close session
    session.commit()
    session.close()


if __name__ == '__main__':
    state_city_fetch()
