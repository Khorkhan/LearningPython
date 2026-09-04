# Basic Operators

number = 1 + 2 * 3 / 4.0
remainder = 11 % 3
squared = 7 ** 2
cubed = 2 ** 3

print(number)
print(remainder)
print(squared)
print(cubed)

# Using Operators with Strings

helloworld = "hello" + " " + "world"
lotsofhello = "hello" * 10

print(helloworld)
print(lotsofhello)

# Using Operators with Lists

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

# Excercise

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d object" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")