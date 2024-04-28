#Задание № 1. Наследование

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Задание № 2. Атрибуты и взаимодействие классов.

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_from_students = {}

    def av_grade_lecture(self):
        for i in self.grades_from_students.values():
            av_grade_lec = sum(i) / len(i)
        return av_grade_lec


#Задание № 3. Полиморфизм и магические методы
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(self.av_grade_lecture(), 1)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_reviewer(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.completed_courses = 'Введение в програмирование'

    def av_grade_homework(self):
        for i in self.grades.values():
            av_grade = sum(i) / len(i)
        return av_grade


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {round(self.av_grade_homework(), 1)} \nКурсы в процессе изучения: {', '.join(new_list)} \nЗавершенные курсы: {self.completed_courses}')


    def rate_to_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'



some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
print(f'У проверяющих он должен выводить информацию в следующем виде:\n{some_reviewer}')

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Git']
new_list = some_student.courses_in_progress + some_student.finished_courses

some_student.rate_to_lecturer(some_lecturer, 'Python', 2)
some_student.rate_to_lecturer(some_lecturer, 'Python', 10)
some_student.rate_to_lecturer(some_lecturer, 'Python', 9.8)
print(f'У лекторов\n{some_lecturer}')

some_reviewer.rate_reviewer(some_student, 'Python', 2)
some_reviewer.rate_reviewer(some_student, 'Python', 10)
some_reviewer.rate_reviewer(some_student, 'Python', 9.8)

print(f'А у студентов так:\n{some_student}')

chemist = Mentor('Dmitriy', 'Mendeleev')
poet = Mentor('Aleksandr', 'Puskin')

lec1 = Lecturer('Дмитрий', 'Иванов')
lec1.courses_attached += ['Python']

lec2 = Lecturer('Захар', 'Малахов')
lec2.courses_attached += ['Python']


stud1 = Student('Анастасия', 'Климанова', 'female')
stud1.courses_in_progress += ['Python']
stud1.finished_courses += ['Git']
stud1.rate_to_lecturer(lec1, 'Python', 8)
stud1.rate_to_lecturer(lec1, 'Python', 9)


stud2 = Student('Михаил', 'Звягинцев', 'male')
stud2.courses_in_progress += ['Python']
stud2.finished_courses += ['Git']
stud2.rate_to_lecturer(lec1, 'Python', 10)
stud2.rate_to_lecturer(lec2, 'Python', 9)


rev1 = Reviewer('Екатерина', 'Соколова')
rev1.courses_attached += ['Python']
rev1.rate_reviewer(stud1, 'Python', 10)
rev1.rate_reviewer(stud2, 'Python', 9)
print(rev1)

rev2 = Reviewer('Антон', 'Орлов')
rev2.courses_attached += ['Python']
rev2.rate_reviewer(stud1, 'Python', 2)
rev2.rate_reviewer(stud2, 'Python', 9)
print(rev2)

print(lec1)
print(lec2)
print(stud1)
print(stud2)
print(stud1.av_grade_homework() < stud2.av_grade_homework()) #True
print(stud1.av_grade_homework() > stud2.av_grade_homework()) #False
print(stud1.av_grade_homework() == stud2.av_grade_homework())  #False
print(lec1.av_grade_lecture() < lec2.av_grade_lecture()) #False
print(lec1.av_grade_lecture() > lec2.av_grade_lecture()) #False
print(lec1.av_grade_lecture() == lec2.av_grade_lecture()) #True

list_students = [some_student, stud1, stud2]
list_lectures = [some_lecturer, lec1, lec2]
def av_all_grades_student(list_students, course):
    sum = 0
    count = 0
    for student in list_students:
        if student.courses_in_progress == [course]:
            sum += student.av_grade_homework()
            count += 1
    return round(sum/count, 1)

def av_all_grades_lecturer(list_lecturer, course):
    sum = 0
    count = 0
    for lecturer in list_lectures:
        if lecturer.courses_attached == [course]:
            sum += lecturer.av_grade_lecture()
            count += 1
    return round(sum/count, 1)

print(f'Средняя оценка для всех студентов по курсу {"Python"}: {av_all_grades_student(list_students, "Python")}')
print(f'Средняя оценка для всех лекторов по курсу {"Python"}: {av_all_grades_lecturer(list_lectures, "Python")}')