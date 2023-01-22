from faker import Faker
from database.connect_db import session
from database.models import Grade
from random import randint
from datetime import datetime, timedelta

fake = Faker()


def create_grades():
    count_students = 1
    count_grades = 0
    while count_students <= 40:
        if count_grades < 19:
            grade = Grade(
                grade=randint(1, 12),
                date_of=datetime.now().date() - timedelta(randint(1, 250)),
                student_id=count_students,
                discipline_id=randint(1, 7)
            )
            session.add(grade)
            count_grades += 1
        else:
            grade = Grade(
                grade=randint(1, 12),
                date_of=datetime.now().date() - timedelta(randint(1, 250)),
                student_id=count_students,
                discipline_id=randint(1, 7)
            )
            count_grades = 0
            count_students += 1

    session.commit()


if __name__ == '__main__':
    create_grades()
