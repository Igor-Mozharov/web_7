from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    grade = relationship('Grade', backref='student', passive_deletes=True)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    student = relationship('Student', backref='group', passive_deletes=True)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    discipline = relationship('Discipline', backref='teacher', passive_deletes=True)


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    teachers_id = Column('teachers_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    grade = relationship('Grade', backref='discipline', passive_deletes=True)


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(DateTime, default=func.now())
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', ForeignKey('disciplines.id', ondelete='CASCADE'))