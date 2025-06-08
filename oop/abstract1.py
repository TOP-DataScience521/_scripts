from abc import ABC, abstractmethod
from decimal import Decimal as dec
from random import randrange as rr


class Person(ABC):
    def __init__(
            self,
            last_name,
            first_name,
            patr_name
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    @abstractmethod
    def __str__(self):
        pass


class Employee(Person):
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            position,
            income
    ):
        super().__init__(last_name, first_name, patr_name)
        self.position = position
        self.income = dec(str(income))
    
    @abstractmethod
    def calc_month_income(self, *args):
        pass


class Teacher(Employee):
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            position,
            income,
            degree='',
            is_professor=False
    ):
        super().__init__(last_name, first_name, patr_name, position, income)
        self.degree = degree
        self.professor = is_professor
    
    def calc_month_income(self, *args):
        income = rr(355, 628) * 100
        self.income = income
        return income


class Administrator(Employee):
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            position,
            income,
            head,
            subordinates=None
    ):
        super().__init__(last_name, first_name, patr_name, position, income)
        self.head = head
        if subordinates is None:
            subordinates = []
        self.subordinates = subordinates
    
    def calc_month_income(self, *args):
        income = rr(168, 329) * 100
        self.income = income
        return income


class Student(Person):
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
            student_id,
            semester=1
    ):
        super().__init__(last_name, first_name, patr_name)
        self.id = student_id
        self.semester = semester
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patr_name}: {self.id}'

