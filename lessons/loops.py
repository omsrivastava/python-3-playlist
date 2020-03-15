# users = ['Jack', 'Crystal', 'Moron', 'Joy', 'Stiffler', 'Jenny']

# for user in users:
#   print(user)

# for user in users[1:3]:
#   print(user)

# for user in users:
#   if user == 'Stiffler':
#     print(f'{user} - is the Admin')
#   else:
#     print(user)

'''
While Loop
'''

range = 25
age = 0

while age < range:
  if age == 0:
    age += 1
    continue

  if age % 2 == 0:
    print(age)

  age += 1