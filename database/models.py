from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    group_id = Column('group_id', ForeignKey('group.id', ondelete='CASCADE'))
    grade = relationship('Grade', backref='students', passive_deletes=True)


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    student = relationship('Student', backref='groups', passive_deletes=True)


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), nullable=False)
    discipline = relationship('Discipline', backref='teachers', passive_deletes=True)


class Discipline(Base):
    __tablename__ = 'discipline'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    teachers_id = Column('teachers_id', ForeignKey('teacher.id', ondelete='CASCADE'))
    grade = relationship('Grade', backref='disciplines', passive_deletes=True)


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(DateTime, default=func.now())
    student_id = Column('student_id', ForeignKey('student.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', ForeignKey('discipline.id', ondelete='CASCADE'))