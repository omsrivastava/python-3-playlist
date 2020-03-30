def cough_dec(func):
  
  def wrapper_func():
    # code defore function
    print('*cough*')
    func()
    # code after function
    print('*cough*')
  
  return wrapper_func


@cough_dec
def question():
  print('can you please give me a discount on that?')

@cough_dec
def answer():
  print("It's just 50p you cheapskate")


question()
answer()