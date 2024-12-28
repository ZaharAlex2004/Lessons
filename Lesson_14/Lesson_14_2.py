import Lesson_14 as ls

st1 = ls.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = ls.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = ls.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

print(gr.find_student('Jobs'))
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student
