class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def _average_1(self,):
        return round(sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())), 1)
    
    def __lt__(self, other):
        if self._average_1() >= other._average_1():
            return f'{self.name} {self.surname} лучше чем {other.name} {other.surname}'
        else:
            return f'{other.name} {other.surname} лучше чем {self.name} {self.surname}'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self._average_1()}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.courses_attached = []
        self.grades = {}

    def _average_2(self):
        return round(sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())), 1)
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self._average_2()}\n'
    
    def __lt__(self, other):
        if self._average_2() >= other._average_2():
            return f'{self.name} {self.surname} лучше чем {other.name} {other.surname}'
        else:
            return f'{other.name} {other.surname} лучше чем {self.name} {self.surname}'
        
        

class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'
    
student_1 = Student('Анна', 'Балакирев', 'ж')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Генадий', 'Букин', 'м')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Анна', 'Федорова')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Жорик', 'Вортанов')
reviewer_2.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Python', 10)

lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Иван', 'Ургант')
lecturer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 8)
student_2.rate_hw(lecturer_2, 'Git', 10)

print(student_1)
print(student_2)
print(student_1 < student_2)
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 < lecturer_2)
print(reviewer_1)
print(reviewer_2)


def average_rating(students, course):
    sum_rating = 0
    count_students = 0
    for student in students:
        if course in student.grades:
            sum_rating += sum(student.grades[course])
            count_students += len(student.grades[course])
    if count_students != 0:
        res = round(sum_rating / count_students, 1)
        result = f'Средняя оценка студентов по курсу {course}: {res}'
        return result
    else:
        return f'На {course} нет оценок'
    
print(average_rating([student_1, student_2], 'Python'))

def average_rating_2(lecturers, course):
    sum_rating = 0
    count_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_rating += sum(lecturer.grades[course])
            count_lecturers += len(lecturer.grades[course])
    if count_lecturers != 0:
        res = round(sum_rating / count_lecturers, 1)
        result = f'Средняя оценка лекторов по курсу {course}: {res}'
        return result
    else:
        return f'На {course} нет оценок'
    
print(average_rating_2([lecturer_1, lecturer_2], 'Python'))