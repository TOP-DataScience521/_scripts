class Person:
    def __init__(
            person_self,
            last_name,
            first_name,
            patr_name,
    ):
        person_self.last_name = last_name
        person_self.first_name = first_name
        person_self.patr_name = patr_name


class Student(Person):
    def __init__(
            student_self,
            last_name,
            first_name,
            patr_name, 
            year,
    ):
        # Person.__init__(student_self, last_name, first_name, patr_name)
        super().__init__(last_name, first_name, patr_name)
        student_self.year = year


class Teacher(Person):
    def __init__(
            teacher_self,
            last_name,
            first_name,
            patr_name,
            courses,
    ):
        super().__init__(last_name, first_name, patr_name)
        teacher_self.courses = courses


st1 = Student('Иванов', 'Иван', 'Иванович', 5)

# >>> st1.__dict__
# {'last_name': 'Иванов', 'first_name': 'Иван', 'patr_name': 'Иванович', 'year': 5}

t1 = Teacher('Петров', 'Пётр', 'Петрович', ['общая физика', 'лабораторный практикум по общей физике'])

# >>> t1.__dict__
# {'last_name': 'Петров', 'first_name': 'Пётр', 'patr_name': 'Петрович', 'courses': ['общая физика', 'лабораторный практикум по общей физике']}

