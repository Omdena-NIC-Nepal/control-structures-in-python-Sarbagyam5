# Task 1: while loop
def test_while_loop_even_numbers(number):
  number = 0
  while number <= 20:
      print(number)
      number+=number

def test_for_loop_skip_divisible_by_3():
  for num in range(1, 16):
          if num%3 ==0:
              continue
          print(num)
 

def test_number_classification():
  number = int(input("Enter a number: "))
  if(number>0):
    print("Positive")
  elif(number<0):
    print("negative")
  else:
    print("zero")

def test_multiplication_table():
  for i in range(1, 6):
    for j in range(1, 6):
      print(f"{i} x {j} = {i * j}", end="\t")  
    print()
    
