# user = { 'id': 123, 'name': 'Tom' }

# print(user['id'])
# print(user['name'])

# print('email' in user)

# print(user.keys())

# print(user.values())

# list = list(user.keys())

# print(list)

# print(list.count('id'))

# user['email'] = 'test@gmail.com'

# print(user)


#############################################################


def get_users(users):
  for key, val in users.items():
    print(f'Name = {key} and Email = {val}')


user_emails = {}

while True:
  name = input('Enter name of user: ')
  email = input('Enter email of user: ')

  user_emails[name] = email

  another = input('add another? (y/n): ')
  if another == 'y':
    continue
  else:
    break

get_users(user_emails)