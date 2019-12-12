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

Std_1 = Student('Abdul', 'Abdullah', '60')
Std_2 = Student('Aisha', 'Aliyu', '90')



print(Std_1.grade)
Std_1.apply_raise()
print(Std_1.grade)
print(Std_2.grade)
Std_2.apply_raise()
print(Std_2.grade)
#print(Std_1.fullname())
#print(Std_2.fullname())