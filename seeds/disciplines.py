from faker import Faker
from database.connect_db import session
from database.models import Discipline
from random import  randint

fake = Faker()

def create_disciplines():
    for _ in range(7):
        discipline = Discipline(
            name=fake.localized_ean8(),
            teachers_id=randint(1, 4)
        )
        session.add(discipline)
    session.commit()


if __name__ == '__main__':
    create_disciplines()