import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

import conf.db_connection
from conf.models import Teacher, Student, TeacherStudent


fake = Faker('uk-UA')


def insert_students():
    for _ in range(30):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        conf.db_connection.session.add(student)


def insert_teachers():
    for _ in range(3):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-5y')
        )
        conf.db_connection.session.add(teacher)


def insert_relations():
    students = conf.db_connection.session.query(Student).all()
    teachers = conf.db_connection.session.query(Teacher).all()

    for student in students:
        rel = TeacherStudent(teacher_id=random.choice(teachers).id, student_id=student.id)
        conf.db_connection.session.add(rel)


if __name__ == '__main__':
    try:
        insert_students()
        insert_teachers()
        conf.db_connection.session.commit()
        insert_relations()
        conf.db_connection.session.commit()
    except SQLAlchemyError as e:
        print(e)
        conf.db_connection.session.rollback()
    finally:
        conf.db_connection.session.close()