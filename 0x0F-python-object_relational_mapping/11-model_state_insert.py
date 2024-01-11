#!/usr/bin/python3
"""Add the state object `Louisiana`."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Luisiana")
    session.add(new_state)
    session.commit()

    luisiana = session.query(State).filter_by(name="Luisiana").one()
    print(luisiana.id)

    session.close()
