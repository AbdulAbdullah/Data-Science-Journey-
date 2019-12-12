class Student:

    perc_raise = 1.6

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        self.grade = int(self.grade * 2)

class Dumb(Student):

    perc_raise = 1.10

Std_1 = Dumb('Abdul', 'Abdullah', '60')
print(Std_1.grade)
Std_2 = Dumb('Aisha', 'Aliyu', '90')
