import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

import conf.db_connection
from conf.models import Teacher, Student, Subject, Group, Grade

fake = Faker('uk-UA')


def insert_teachers():
    for _ in range(3):
        teacher = Teacher(
            fullname=fake.name()
        )
        conf.db_connection.session.add(teacher)


def insert_groups():
    for _ in range(3):
        group = Group(name=fake.word())
        conf.db_connection.session.add(group)


def insert_students():
    groups = conf.db_connection.session.query(Group).all()

    for _ in range(30):
        group = random.choice(groups)
        student = Student(
            fullname=fake.name(),
            group_id=group.id
        )
        conf.db_connection.session.add(student)


def insert_subjects():
    teachers = conf.db_connection.session.query(Teacher).all()

    for _ in range(5):
        teacher = random.choice(teachers)
        subject = Subject(
            name=fake.word(),
            teacher_id=teacher.id
        )
        conf.db_connection.session.add(subject)


def insert_grades():
    students = conf.db_connection.session.query(Student).all()
    subjects = conf.db_connection.session.query(Subject).all()

    for _ in range(20):
        student = random.choice(students)
        subject = random.choice(subjects)
        grade = Grade(
            grade=random.randint(1, 100),
            grade_date=fake.date_between(start_date='-5y'),
            student=student,
            discipline=subject
        )
        conf.db_connection.session.add(grade)


if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        insert_students()
        insert_subjects()
        insert_grades()
        conf.db_connection.session.commit()
    except SQLAlchemyError as e:
        print(e)
        conf.db_connection.session.rollback()
    finally:
        conf.db_connection.session.close()
