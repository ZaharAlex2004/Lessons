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
