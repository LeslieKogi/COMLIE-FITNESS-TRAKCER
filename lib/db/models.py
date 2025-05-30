from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    workouts = relationship("Workout", back_populates="user", cascade="all, delete-orphan")
    progress_records = relationship("Progress", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="workouts")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Workout(id={self.id}, date={self.date}, user_id={self.user_id})>"

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    muscle_group = Column(String, nullable=False)

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise", cascade="all, delete-orphan")
    progress_records = relationship("Progress", back_populates="exercise", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Exercise(id={self.id}, name='{self.name}', muscle_group='{self.muscle_group}')>"

class WorkoutExercise(Base):
    __tablename__ = 'workout_exercises'

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)  # kg

    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")

    def __repr__(self):
        return (
            f"<WorkoutExercise(id={self.id}, workout_id={self.workout_id}, "
            f"exercise_id={self.exercise_id}, sets={self.sets}, reps={self.reps}, weight={self.weight})>"
        )

class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    date = Column(Date, nullable=False)
    max_weight = Column(Integer, nullable=False)

    user = relationship("User", back_populates="progress_records")
    exercise = relationship("Exercise", back_populates="progress_records")

    __table_args__ = (
        UniqueConstraint('user_id', 'exercise_id', 'date', name='uix_user_exercise_date'),
    )

    def __repr__(self):
        return (
            f"<Progress(id={self.id}, user_id={self.user_id}, exercise_id={self.exercise_id}, "
            f"date={self.date}, max_weight={self.max_weight})>"
        )





