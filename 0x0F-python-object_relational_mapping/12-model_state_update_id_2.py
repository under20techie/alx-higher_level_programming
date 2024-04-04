#!/usr/bin/python3
"""
Script that lists only the first State objects from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State


def fetch_update():
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

    # Query database to in order to update old entry
    result = (
            session.query(State)
            .filter_by(id=2)
            .update({"name": "New Mexico"})
        )

    # close session
    session.commit()
    session.close()


if __name__ == '__main__':
    fetch_update()
