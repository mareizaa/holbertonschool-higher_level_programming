#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""
from sys import argv

from sqlalchemy import engine
from relationship_state import Base, State
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state_c = State(name="California")
    state_c.cities = [City(name="San Francisco")]

    session.add(state_c)
    session.commit()
    session.close()
