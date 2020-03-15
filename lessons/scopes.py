name = 'Steve'

def print_name():
  global name
  name = 'Jannifer'
  print('Name inside the function: ', name)


print_name()

print('Name outside the function: ', name)