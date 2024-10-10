#10-1
#open the txt file
f = open('learning_python.txt')
#assign a variable to the contents of the file
file_contents = f.read()
#print the variable
print(file_contents)
#10-2
altrd = file_contents.replace('python', 'C')
print(altrd)
#10-3
name = input("What's your name? ")
print(name)
f = open("guest.txt", "w")
f.write(name)
f.close()
#10-4
while True:
    name = input("What's your name?: ")
    with open('guest_book.txt', 'a') as guest_book:
        guest_book.write(f"{name}\n")
    print(f"Hello, {name}!")
#10-5
while True:
    reason = input("Why do you like programming? ")
    with open('reasons.txt', 'a') as file:
        file.write(reason)
#10-6
#using try and except to handle the error
def add(num1, num2):
    return num1 + num2
try:
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    print(num1 + num2)
except ValueError:
    print("Error! Only numbers can be input. Please Try Again!")
#10-7
def add(num1, num2):
    return num1 + num2
while True:    
    try:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        print(num1 + num2)
    except ValueError:
        print("Error! Only numbers can be input. Please Try Again!")
