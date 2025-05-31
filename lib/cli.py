#!/usr/bin/env python3
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db.models import Base, User, Workout, Exercise, WorkoutExercise, Progress


# Database setup
engine = create_engine('sqlite:///comlie.db')  
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """COMLIE Fitness Tracker CLI"""
    pass

# -------------------- USER COMMANDS --------------------

@cli.command()
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    """Add a new user with NAME and EMAIL."""
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    try:
        session.commit()
        click.echo(f"User '{name}' added.")
    except:
        session.rollback()
        click.echo("Email must be unique.")
    finally:
        session.close()

@cli.command()
def list_users():
    """List all users."""
    session = Session()
    users = session.query(User).all()
    for user in users:
        click.echo(user)
    session.close()

@cli.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    """Delete user by ID."""
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        click.echo(f"Deleted user {user_id}.")
    else:
        click.echo("User not found.")
    session.close()

# -------------------- EXERCISE COMMANDS --------------------

@cli.command()
@click.argument('name')
@click.argument('muscle_group')
def add_exercise(name, muscle_group):
    """Add an exercise with NAME and MUSCLE_GROUP."""
    session = Session()
    exercise = Exercise(name=name, muscle_group=muscle_group)
    session.add(exercise)
    session.commit()
    click.echo(f"Exercise '{name}' added.")
    session.close()

@cli.command()
def list_exercises():
    """List all exercises."""
    session = Session()
    exercises = session.query(Exercise).all()
    for exercise in exercises:
        click.echo(exercise)
    session.close()

# -------------------- WORKOUT COMMANDS --------------------

@cli.command()
@click.argument('user_id', type=int)
@click.argument('date')
def log_workout(user_id, date):
    """Log a workout for USER_ID on DATE (YYYY-MM-DD)."""
    session = Session()
    try:
        workout_date = datetime.strptime(date, "%Y-%m-%d").date()
        workout = Workout(user_id=user_id, date=workout_date)
        session.add(workout)
        session.commit()
        click.echo(f"Workout logged for user {user_id} on {date}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Failed to log workout: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('user_id', type=int)
def list_workouts(user_id):
    """List all workouts for a user."""
    session = Session()
    workouts = session.query(Workout).filter_by(user_id=user_id).all()
    for workout in workouts:
        click.echo(workout)
    session.close()

# -------------------- WORKOUT_EXERCISE COMMANDS --------------------

@cli.command()
@click.argument('workout_id', type=int)
@click.argument('exercise_id', type=int)
@click.argument('sets', type=int)
@click.argument('reps', type=int)
@click.argument('weight', type=int)
def add_to_workout(workout_id, exercise_id, sets, reps, weight):
    """Add an exercise to a workout."""
    session = Session()
    we = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        sets=sets,
        reps=reps,
        weight=weight
    )
    session.add(we)
    session.commit()
    click.echo(f"Added exercise {exercise_id} to workout {workout_id}.")
    session.close()

# -------------------- PROGRESS COMMANDS --------------------

@cli.command()
@click.argument('user_id', type=int)
@click.argument('exercise_id', type=int)
@click.argument('date')
@click.argument('max_weight', type=int)
def record_progress(user_id, exercise_id, date, max_weight):
    """Record or update PR for a user and exercise."""
    session = Session()
    try:
        pr_date = datetime.strptime(date, "%Y-%m-%d").date()
        existing = session.query(Progress).filter_by(
            user_id=user_id,
            exercise_id=exercise_id,
            date=pr_date
        ).first()

        if existing:
            if max_weight > existing.max_weight:
                existing.max_weight = max_weight
                click.echo("Updated existing PR with new max weight.")
            else:
                click.echo("Existing PR is higher or equal. No update.")
        else:
            new_pr = Progress(
                user_id=user_id,
                exercise_id=exercise_id,
                date=pr_date,
                max_weight=max_weight
            )
            session.add(new_pr)
            click.echo("New PR recorded.")
        session.commit()
    except Exception as e:
        session.rollback()
        click.echo(f"Error: {e}")
    finally:
        session.close()

@cli.command()
@click.argument('user_id', type=int)
def view_progress(user_id):
    """View all progress records for a user."""
    session = Session()
    records = session.query(Progress).filter_by(user_id=user_id).all()
    for record in records:
        click.echo(record)
    session.close()

# -------------------- INIT DB COMMAND --------------------

@cli.command()
def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(engine)
    click.echo("Database initialized.")


if __name__ == "__main__":
    cli()
