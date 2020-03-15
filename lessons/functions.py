# def greet(name, time):
#   print(f'Good {time} {name}, how are you?')


# name = input('Enter your name: ')
# time = input('Enter the time of the day: ')

# greet(name, time)

def area(radius):
  return 3.142 * radius ** 2

def vol(area, length):
  print(area * length)


radius = int(input('Enter the radius: '))
length = int(input('Enter the length: '))

area_calc = area(radius)

vol(area_calc, length)