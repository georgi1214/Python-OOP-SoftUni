from projectMultipleInheritance.person import Person
from projectMultipleInheritance.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."