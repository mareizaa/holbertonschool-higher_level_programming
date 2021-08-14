#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv

from sqlalchemy import engine
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    letter = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for state in letter:
        print("{}: {}".format(state.id, state.name))

    session.close()
