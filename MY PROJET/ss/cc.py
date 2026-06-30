print("Hello, World!")

# 1) Variables
name = "Mohammed"
age = 30
print(f"My name is {name} and I am {age} years old")

# 2) Read the name from the user
name = input("Enter your name: ")
print("Hello", name)

# 3) Read the age from the user
age = int(input("Enter your age: "))

# 4) If/else condition
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# 5) For loop
for i in range(3):
    print("This is the number:", i)

# 6) Function
def greet(user_name):
    print("Hello", user_name)

greet(name)

# 7) While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# 8) List
fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0])

# 9) Dictionary
person = {"name": "Ali", "age": 25}
print(person["name"])

# 10) Boolean
is_student = True
print(is_student)