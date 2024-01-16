# Complex Beginner's Python Guide with Flask

from flask import Flask, render_template

app = Flask(__name__)

# Section 1: Introduction
print("Welcome to the Complex Beginner's Python Guide!")
print("This script includes Flask for a simple web application and covers advanced Python concepts.")

# Section 2: Flask Web Application
@app.route('/')
def index():
    return render_template('index.html')

# Section 3: Variables and Data Types
print("\nSection 3: Variables and Data Types\n")

name = "John"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}\nAge: {age}\nHeight: {height}\nIs Student? {is_student}")

# Section 4: User Input and Error Handling
print("\nSection 4: User Input and Error Handling\n")

try:
    user_age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
# Section 5: Loops
display_section_header(5, "Loops")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Section 6: Functions and Recursion
display_section_header(6, "Functions and Recursion")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Section 7: Lists and List Comprehensions
display_section_header(7, "Lists and List Comprehensions")
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("Original List:", numbers)
print("Squared List:", squared_numbers)

# Section 8: Exception Handling
display_section_header(8, "Exception Handling")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero.")

# Section 9: File Handling
display_section_header(9, "File Handling")
try:
    with open("example.txt", "w") as file:
        file.write("Hello, Python!")
except IOError:
    print("Error: Unable to write to the file.")

# Section 10: Classes and Object-Oriented Programming
display_section_header(10, "Classes and Object-Oriented Programming")
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()
# Section 11: Flask App Run
if __name__ == '__main__':
    app.run(debug=True)

# Conclusion
display_section_header(11, "Conclusion")
print("Congratulations! You've completed the Advanced Beginner's Python Guide.")
print("This guide covered a range of topics to help you become a more proficient Python programmer.")
