from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Exercise, Workout, Progress, WorkoutExercise
from datetime import date

# Connects the engine to the database
engine = create_engine('sqlite:///comlie.db')
Session = sessionmaker(bind=engine)

def seed_data():
    session = Session()

    # Removing all the rows and tables b4 we seed the data
    session.query(WorkoutExercise).delete()
    session.query(Progress).delete()
    session.query(Workout).delete()
    session.query(Exercise).delete()
    session.query(User).delete()

    # Add users to the table
    users = [
        User(name="Alice Anderson", email="alice@example.com"),
        User(name="Bob Builder", email="bob@example.com"),
        User(name="Nonnie Sankara",email="nonnie@gmail.com")
    ]

    # Add exercisesto the table
    exercises = [
        Exercise(name="Squat", muscle_group="Legs"),
        Exercise(name="Bench Press", muscle_group="Chest"),
        Exercise(name="Deadlift", muscle_group="Back"),
        Exercise(name="Overhead Press", muscle_group="Shoulders")
    ]
    
    session.add_all(users + exercises)
    session.commit()
    # Add workouts after committing users to have valid user IDs
    workouts = [
        Workout(date=date(2025, 5, 28), user_id=users[0].id),  
        Workout(date=date(2025, 4, 23), user_id=users[1].id),
        Workout(date=date(2024, 4, 15), user_id=users[2].id)
    ]

    session.add_all(workouts)
    session.commit()

    #Adding progress 
    progress=[
        Progress(user_id=users[0].id, exercise_id=exercises[2].id, date=date(2025,3,20), max_weight=30),
        Progress(user_id=users[1].id, exercise_id=exercises[3].id, date=date(2025,4,22), max_weight=40)
    ]
    

    #Adding Workout Exercise
    workout_exercises=[
        WorkoutExercise(workout_id=workouts[0].id,exercise_id=exercises[3].id, sets=4, reps=5, weight=50),
        WorkoutExercise(workout_id=workouts[1].id,exercise_id=exercises[2].id, sets=6, reps=4, weight=30)
    ]
    session.add_all(progress + workout_exercises)
    session.commit()

    session.close()
    print(" Database seeded with sample data.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    seed_data()