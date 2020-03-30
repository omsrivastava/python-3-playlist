nums = [1,2,3,4,5,6,7,8]

def square(n):
  return n * n


# using square function
# print(list(map(square, nums)))

# using lambda
print(list(map(lambda n: n * n, nums)))