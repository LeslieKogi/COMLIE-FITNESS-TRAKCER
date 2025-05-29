from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Workout, Exercise, WorkoutExercise, Progress

engine = create_engine('sqlite:///comile.db')
Session = sessionmaker(bind=engine)
session = Session()

def explore():
    print("Welcome to COMILE debug mode.")
    print("Examples:")
    print("- session.query(User).all()")
    print("- session.query(Workout).filter_by(user_id=1).first()")
    print("- user = session.query(User).get(1)")

    while True:
        try:
            command = input(">>> ")
            if command.lower() in ('exit', 'quit'):
                break
            result = eval(command)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    explore()