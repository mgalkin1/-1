grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = [sum(grade) / len(grade) for grade in grades]
print(average_grades)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = sorted(students)

print(students2)
print()
grade_student = zip(students2, average_grades)
print("Cредний балл студента: ", dict(grade_student))
