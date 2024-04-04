#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State 


def state_fetch_all():
    """Func where we fetch states from database """

    username, passwd, db = sys.argv[1:]

    # create connect to database
    engine = create_engine(f'mysql+mysqldb://{username}:{passwd}@localhost/{db}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session for transaction
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create query to database
    result = session.query(State).order_by(State.id).all()

    # Print result
    for state in result:
        print(f"{state.id}: {state.name}")

    # close session
    session.close()


if __name__ == '__main__':
    state_fetch_all()
