class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        Human.__init__(self, gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise ValueError("Максимальное количество студентов")


    def delete_student(self, last_name):
        deleting_ln = self.find_student(last_name)
        if deleting_ln:
            self.group.remove(deleting_ln)

    def find_student(self, last_name):
        for std in self.group:
            if last_name in std.last_name:
                return std
        return None

    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f'Number: {self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 23, 'Mary', 'Logeons', 'AN143')
st4 = Student('Male', 26, 'Michael', 'Koval', 'AN145')
st5 = Student('Male', 27, 'Peter', 'Petrenko', 'AN144')
st6 = Student('Female', 25, 'Olga', 'Koval', 'AN141')
st7 = Student('Male', 24, 'Albert', 'Tayshtain', 'AN143')
st8 = Student('Male', 25, 'George', 'Smith', 'AN143')
st9 = Student('Female', 25, 'Alice', 'Sping', 'AN142')
st10 = Student('Male', 25, 'Alex', 'Nikon', 'AN143')
st11 = Student('Male', 25, 'Bogdan', 'Luvr', 'AN144')  # Если добавить ещё 11-го студента
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)

print(gr)
try:
    gr.add_student(st11)
except ValueError as e:
    print(e)

print(str(gr.find_student('Jobs')))
print(isinstance(gr.find_student('Jobs'), Student))
print(gr.find_student('Jobs2'))

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
# Удаляем одного студента
gr.delete_student('Taylor')

# Добавляем ещё одного студента
gr.add_student(st11)
print(f'\n{gr}')
