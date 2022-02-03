class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating:.1f}\n' \
              f'Курсы в процессе обучения: {str(*self.courses_in_progress)}\n' \
              f'Завершенные курсы: {str(*self.finished_courses)}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating:.1f}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
            res =f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}'
            return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_lecturer_1 = Lecturer('Max', 'Vasilev')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Ivan', 'Orlov')
best_lecturer_2.courses_attached += ['Git']

best_lecturer_3 = Lecturer('Igor', 'Zaycev')
best_lecturer_3.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Nikita', 'Volkov')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ken', 'Block', 'your_gender')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Alex', 'Smirnov', 'your_gender')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 5)

student_1.rate_hw(best_lecturer_1, 'Python', 6)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Git', 10)
student_2.rate_hw(best_lecturer_2, 'Git', 9)
student_2.rate_hw(best_lecturer_2, 'Git', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 3)
student_3.rate_hw(best_lecturer_3, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 8)

cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)

cool_reviewer_2.rate_hw(student_2, 'Git', 10)
cool_reviewer_2.rate_hw(student_2, 'Git', 10)
cool_reviewer_2.rate_hw(student_2, 'Git', 10)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)


print(f'Перечень студентов:\n{student_1}\n\n{student_2}\n\n{student_3}')
print()

print(f'Перечень лекторов:\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()

print(f'Перечень рецензентов:\n{cool_reviewer_1}\n\n{cool_reviewer_2}')
print()

print(f'Результат сравнения по средним оценкам за ДЗ,студентов : '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print(f'Результат сравнения  по средним оценкам за лекции, лекторов: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} \
{best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

student_list = [student_1, student_2, student_3]

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
    all_sum = 0
    all_count = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            all_sum += stud.average_rating
            all_count += 1
    average_for_all = all_sum / all_count
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    all_sum = 0
    all_count = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            all_sum += lect.average_rating
            all_count += 1
    average_for_all = all_sum / all_count
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python'):.1f}")
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rating(student_list, 'Git'):.1f}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python'):.1f}")
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {lecturer_rating(lecturer_list, 'Git'):.1f}")