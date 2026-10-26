# Python Data Types - Complete Reference

# 1. Numbers
age = 21              # int
price = 99.5          # float
complex_num = 3 + 4j  # complex

# 2. String
name = "Shiva"
message = 'Python is easy'

# 3. Boolean
is_student = True
is_pass = False

# 4. List - Ordered, Changable, Allows duplicate
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

# 5. Tuple - Ordered, Unchangable, Allows duplicate
coordinates = (10, 20, 30)

# 6. Set - Unordered, No duplicate
my_set = {1, 2, 2, 3, 4}  # will be {1, 2, 3, 4}
print(my_set)

# 7. Dictionary - Key : Value pair
student = {
    "name": "Shiva",
    "age": 21,
    "course": "Python"
}
print(student["name"])

# 8. NoneType
result = None

# How to check data type
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(fruits))     # <class 'list'>
print(type(student))    # <class 'dict'>

# Type Conversion
a = 10
b = float(a)   # int to float -> 10.0
c = str(a)     # int to string -> "10"
print(b, c)
