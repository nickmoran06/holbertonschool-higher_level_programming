#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    FirstState = session.query(State).first()
    if FirstState is not None:
        print("{}: {}".format(FirstState.id, FirstState.name))
    else:
        print("Nothing")

    session.close()
