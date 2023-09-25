from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='postgres',
        password='11111111',
        port=5432,
    )
)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f'This is {self.id} student {self.name}. Age: {self.age}'

    def __repr__(self):
        return f'This is {self.id} student {self.name}. Age: {self.age}'


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return f'This is {self.id} subject {self.name}'

    def __repr__(self):
        return f'This is {self.id} subject {self.name}'


class Student_Subject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    student = relationship('Student', backref='student_subjects')
    subject = relationship('Subject', backref='student_subjects')

    def __str__(self):
        return f'Subject - {self.subject_id} for {self.student_id} student'

    def __repr__(self):
        return f'Subject - {self.subject_id} for {self.student_id} student'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.query(Student_Subject).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.commit()

student1 = Student(name='Bohdan Hryshckeno', age=21)
student2 = Student(name='Irina Hryshckeno', age=27)
student3 = Student(name='Natalia Hryshckeno', age=50)
student4 = Student(name='Anatoliy Hryshckeno', age=56)


subject1 = Subject(name='Math')
subject2 = Subject(name='English')
subject3 = Subject(name='Biology')
subject4 = Subject(name='History')

student_subject1 = Student_Subject(student=student1, subject=subject1)
student_subject2 = Student_Subject(student=student1, subject=subject2)
student_subject3 = Student_Subject(student=student1, subject=subject3)
student_subject4 = Student_Subject(student=student2, subject=subject1)
student_subject5 = Student_Subject(student=student3, subject=subject4)
student_subject6 = Student_Subject(student=student4, subject=subject4)

session.add_all(
    [student1, student2, student3, student4,
     subject1, subject2, subject3, subject4]
    )

session.commit()

english_visitors = session.query(Student)\
    .join(Student_Subject, Student_Subject.student_id == Student.id)\
    .join(Subject, Student_Subject.subject_id == Subject.id)\
    .filter(Subject.name == 'English')\
    .all()

for student in english_visitors:
    print(student.name)
