from sqlalchemy import func, desc

from conf.db_connection import session
from conf.models import Grade, Teacher, Student, Group, Subject


def select_01():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    SELECT
        students.id,
        students.fullname,
        ROUND(AVG(grades.grade), 2) AS average_grade
    FROM students
    LEFT JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(
        Student.id,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ) \
        .select_from(Student) \
        .join(Grade) \
        .group_by(Student.id) \
        .order_by(desc('average_grade')) \
        .limit(5).all()
    return result


def select_02(subject_id=1):  # сюди аргументом передати id предмету
    # Знайти студента із найвищим середнім балом з певного предмета.
    """
    SELECT
        students.id,
        students.fullname,
        ROUND(AVG(grades.grade), 2) AS average_grade
    FROM grades
    JOIN students ON students.id = grades.student_id
    WHERE grades.subject_id = 1 -- it's the number of subject you want to have grades for
    GROUP BY students.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(
        Student.id,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .filter(Grade.subjects_id == subject_id) \
        .group_by(Student.id) \
        .order_by(desc('average_grade')) \
        .limit(1).all()
    return result


def select_03(subject_id=1):  # сюди аргументом передати id предмету
    # Знайти середній бал у групах з певного предмета.
    """
    SELECT
        groups.id,
        groups.name,
        ROUND(AVG(grades.grade), 2) AS average_grade
    FROM groups
    JOIN students ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    WHERE grades.subject_id = 1 -- it's the number of subject you want to have grades for
    GROUP BY groups.id, groups.name
    ORDER BY average_grade DESC;
    """
    result = session.query(
        Group.id,
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ) \
        .select_from(Group) \
        .join(Student) \
        .join(Grade) \
        .filter(Grade.subjects_id == 1) \
        .group_by(Group.id, Group.name) \
        .order_by(desc('average_grade')) \
        .all()
    return result


def select_04():
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    """
    SELECT
        ROUND(AVG(grades.grade), 2) AS average_grade
    FROM grades;
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ) \
        .select_from(Grade) \
        .all()
    return result


def select_05(teacher_id=2):  # сюди аргументом передати id предмету
    #  Знайти які курси читає певний викладач.
    """
    SELECT
        subjects.id,
        subjects.name
    FROM subjects
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.id = 1; -- ID of teacher you need
    """
    result = session.query(
        Subject.id,
        Subject.name
    ) \
        .select_from(Subject) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .all()
    return result


def select_06(group_id=1):  # сюди аргументом передати id групи
    # Знайти список студентів у певній групі.
    """
    SELECT
        students.id,
        students.fullname
    FROM students
    JOIN groups ON students.group_id = groups.id
    WHERE groups.id = 1;
    """
    result = session.query(
        Student.id,
        Student.fullname
    ) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .all()
    return result


def select_07(group_id=1, subject_id=1):  # сюди аргументом передати id групи та id предмету
    # Знайти оцінки студентів у окремій групі з певного предмета.
    """
    SELECT
        groups.id,
        students.fullname,
        subjects.name,
        grades.grade
    FROM grades
    JOIN students ON students.id = grades.student_id
    JOIN subjects ON subjects.id = grades.subject_id
    JOIN groups ON students.group_id = groups.id
    WHERE
        groups.id = 1 -- enter id of group you need
        AND subjects.id = 3; -- enter id of subject you need
    """
    result = session.query(
        Group.id,
        Student.fullname,
        Subject.name,
        Grade.grade
    ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Subject) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .filter(Subject.id == subject_id) \
        .all()
    return result


def select_08(teacher_id=3):  # сюди аргументом передати id викладача
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    SELECT
        teachers.id,
        teachers.fullname,
        subjects.name,
        ROUND(AVG(grades.grade), 2)
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.id = 1
    GROUP BY teachers.id, teachers.fullname, subjects.name;
    """
    result = session.query(
        Teacher.id,
        Teacher.fullname,
        Subject.name,
        func.round(func.avg(Grade.grade), 2)
    ) \
        .select_from(Grade) \
        .join(Subject) \
        .join(Teacher) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.id, Teacher.fullname, Subject.name) \
        .all()
    return result


def select_09(student_id=1):  # сюди аргументом передати id студента
    # Знайти список курсів, які відвідує певний студент.
    """
        SELECT
        students.id,
        students.fullname,
        subjects.name
    FROM grades
    JOIN students ON grades.student_id = students.id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.id = 1 -- enter desired student id
    GROUP BY
        subjects.name,
        students.fullname,
        students.id;
    """
    result = session.query(
        Student.id,
        Student.fullname,
        Subject.name
    ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Subject) \
        .filter(Student.id == student_id) \
        .group_by(Subject.name, Student.fullname, Student.id) \
        .all()
    return result


def select_10(student_id=1, teacher_id=2):  # сюди аргументом передати id студента та id викладача
    # Список курсів, які певному студенту читає певний викладач.
    """
    SELECT DISTINCT
        students.id,
        students.fullname,
        teachers.fullname,
        subjects.name
    FROM grades
    JOIN students ON students.id = grades.student_id
    JOIN subjects ON subjects.id = grades.subject_id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE
        grades.student_id = 1 -- enter desired student id
        AND teachers.id = 1; -- enter desired teacher id
    """
    result = session.query(
        Student.id,
        Student.fullname,
        Teacher.fullname,
        Subject.name
    ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Subject) \
        .join(Teacher) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .all()
    return result


if __name__ == '__main__':
    print(select_01())
    print(select_02(1))
    print(select_03(1))
    print(select_04())
    print(select_05(2))
    print(select_06(1))
    print(select_07(1, 3))
    print(select_08(3))
    print(select_09(1))
    print(select_10(24, 2))
