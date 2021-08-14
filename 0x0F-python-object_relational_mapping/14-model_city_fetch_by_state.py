#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv

from sqlalchemy import engine
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    obj = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for i, j in obj:
        print("{}: ({}) {}".format(j.name, i.id, i.name))

    session.close()
