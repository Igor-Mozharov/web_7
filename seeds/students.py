from faker import Faker
from database.connect_db import session
from database.models import Student
from random import randint

fake = Faker()


def create_students():
    for _ in range(40):
        student = Student(
            fullname=fake.name(),
            group_id=randint(1, 3)
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()