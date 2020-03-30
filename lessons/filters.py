grades = ['A', 'B', 'F', 'C', 'A', 'F']

filtered_grades = []

def remove_fails(grade):
  return grade != 'F'

# using for loop
for grade in grades:
  if grade != 'F':
    filtered_grades.append(grade)

print(filtered_grades)

# using filters
filtered_grades = filter(remove_fails, grades)
print(list(filtered_grades))

# using comprehension
filtered_grades = [ grade for grade in grades if grade != 'F' ]
print(filtered_grades)
