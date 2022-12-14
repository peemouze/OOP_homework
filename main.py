class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        avg = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return avg

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_grades()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_grades() < other.avg_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def avg_grades(self):
        avg = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return avg


    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grades()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avg_grades() < other.avg_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Math']
#
# best_lecturer = Lecturer('Alex', 'Wang')
# best_lecturer.courses_attached += ['Math']
# best_lecturer.courses_attached += ['Python']
#
# cool_reviewer = Reviewer('Some', 'Buddy')
# cool_reviewer.courses_attached += ['Python']
#
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# cool_reviewer.rate_hw(best_student, 'Python', 10)
#
# best_student.rate_lecturer(best_lecturer, 'Math', 9)
# best_student.rate_lecturer(best_lecturer, 'Python', 6)
#
# print(best_student.grades)
# print(best_lecturer.grades)

some_lecturer = Lecturer('Alex', 'Wang')
some_lecturer.courses_attached += ['Math']
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_student = Student('Jack', 'Milner', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Math']
some_student.finished_courses += ['Git']
some_student.rate_lecturer(some_lecturer, 'Math', 9)
some_student.rate_lecturer(some_lecturer, '', 6)

some_reviewer = Reviewer('Ted', 'Jones')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Math']
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Math', 4)

print(f'Ревьюер\n{some_reviewer}')
print(f'Лектор\n{some_lecturer}')
print(f'Студент\n{some_student}')

some_lecturer2 = Lecturer('Michelle', 'Young')
some_lecturer2.courses_attached += ['Math']
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Git']

some_student2 = Student('Robert', 'Henderson', 'male')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Math']
some_student2.finished_courses += ['Git']
some_student2.rate_lecturer(some_lecturer2, 'Math', 5)
some_student2.rate_lecturer(some_lecturer2, '', 9)

some_reviewer2 = Reviewer('Paul', 'Gordon')
some_reviewer2.courses_attached += ['Python']
some_reviewer2.courses_attached += ['Math']
some_reviewer2.rate_hw(some_student2, 'Python', 5)
some_reviewer2.rate_hw(some_student2, 'Math', 4)

print(f'Ревьюер\n{some_reviewer2}')
print(f'Лектор\n{some_lecturer2}')
print(f'Студент\n{some_student2}')

print(some_student < some_student2)
print(some_lecturer < some_lecturer2)
