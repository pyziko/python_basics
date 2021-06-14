def my_function(*students):
    print("The tallest student is " + students[2])


my_function("James", "Ella", "Jackson")

print("\n**********\n")

def my_function(*argv):
  print(argv)

my_function('Hello', 'World!')


def multi_func(num1, num2):
    return num1 * num2


print(multi_func(5, num2=67))

print("\n**********\n")


def is_true(a):
    return a


result = is_true(6 < 3)
print("The result is", result)

print("\n**********\n")


def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers


print(get_odd_func([1, 2, 3, 4, 5, 6]))

print("\n**********\n")


def get_even_func(numbers):
    odd_numbers = [num for num in numbers if not num % 2]
    return odd_numbers


print(get_even_func([1, 2, 3, 4, 5, 6]))

print("\n**********\n")


def double_list(numbers):
    return 2 * numbers


numbers = [1, 2, 3]
print(double_list(numbers))

print("\n****GLOBAL SCOPE FROM METHOD******\n")

num = 100
own_num = 15


def input_number():
    global own_num
    own_num = 50
    result = int(input("Enter a number: ")) * own_num
    return result


print(input_number())


for num in range(5, 9):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break