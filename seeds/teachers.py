from faker import Faker
from database.connect_db import session
from database.models import Teacher

fake = Faker()


def create_teachers():
    for _ in range(4):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()