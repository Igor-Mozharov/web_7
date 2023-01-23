from select import select

from database.connect_db import session
from database.models import Student, Teacher, Group, Discipline, Grade
from sqlalchemy.orm import joinedload
from sqlalchemy import func, desc


def first():                                        #Найти 5 студентов с наибольшим средним баллом по всем предметам
    res = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade)\
    .join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5)
    for r in res:
        print(r)


def second():                                          #Найти студента с наивысшим средним баллом по определенному предмету
    res = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Student).join(Grade).join(Discipline).group_by(Discipline.name).order_by(desc('avg_grade'))
    for r in res:
        print(r)

def third():                                               #Найти средний балл в группах по определенному предмету
    res = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade).label('avg_grade'), 2)).select_from(Discipline)\
        .join(Grade).join(Student).join(Group).group_by(Group.name, Discipline.name).order_by(Group.name)
    for r in res:
        print(r)


def fourth():                                                 #Найти средний балл на потоке (по всей таблице оценок)
    res = session.query(func.avg(Grade.grade).label('avg_grade')).select_from(Grade)
    for r in res:
        print(r)

def fifth():                                         #Найти какие курсы читает определенный преподаватель
    res =  session.query(Teacher.fullname, Discipline.name).select_from(Teacher).join(Discipline).order_by(desc(Teacher.fullname))
    for r in res:
        print(r)


def sixth():                                           #Найти список студентов в определенной группе.
    res = session.query(Group.name, Student.fullname).select_from(Student).join(Group).group_by(Group.name, Student.fullname)\
    .order_by(Group.name)
    for r in res:
        print(r)


def seventh():                                          #Найти оценки студентов в отдельной группе по определенному предмету
    res = session.query(Student.fullname, Group.name, Discipline.name, Grade.grade).select_from(Group).join(Student).join(Grade)\
    .join(Discipline).order_by(desc(Grade.grade))
    for r in res:
        print(r)

def eighth():                                           #Найти средний балл, который ставит определенный преподаватель по своим предметам.
    res = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade).label('avg_grade'), 2)).select_from(Teacher).join(Discipline)\
    .join(Grade).group_by(Teacher.fullname, Discipline.name).order_by(Teacher.fullname)
    for r in res:
        print(r)

def ninth():                                            #Найти список курсов, которые посещает определенный студент
    res = session.query(Student.fullname, Discipline.name).select_from(Student).join(Grade).join(Discipline)\
    .group_by(Student.fullname, Discipline.name).order_by(Student.fullname)
    for r in res:
        print(r)


def tenth():                                            #Список курсов, которые определенному студенту читает определенный преподаватель
    res = session.query(Teacher.fullname, Discipline.name, Student.fullname).select_from(Teacher).join(Discipline).join(Grade)\
    .join(Student).group_by(Discipline.name, Student.fullname, Teacher.fullname).order_by(desc(Teacher.fullname))
    for r in res:
        print(r)

if __name__ == '__main__':
    first()
    second()
    third()
    fourth()
    fifth()
    sixth()
    seventh()
    eighth()
    ninth()
    tenth()