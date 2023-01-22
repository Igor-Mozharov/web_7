from faker import Faker
from database.connect_db import session
from database.models import Group

fake = Faker()

def create_groups():
    for _ in range(3):
        group = Group(
            name=fake.random_digit_not_null()
        )
        session.add(group)
    session.commit()


if __name__ == '__main__':
    create_groups()