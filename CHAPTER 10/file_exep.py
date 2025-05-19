from pathlib import Path
import json

print("Exercise 10.1")

path=Path("reading_from_a_file/read.txt")
contents=path.read_text()
print(contents)

lines=contents.splitlines()

for line in lines:
    print(line)

print("")
#############################################
print("Exercise 10.2")

path=Path("reading_from_a_file/read.txt")
contents=path.read_text()

for line in contents.splitlines():
    print(line.replace('Python', 'Java'))

print("")
#############################################
print("Exercise 10.3")

path=Path("reading_from_a_file/read.txt")
contents=path.read_text()

for line in contents.splitlines():
    print(line.replace('Python', 'Java'))

print("")
############################################
print("Exercise 10.4")

name_input=input("Enter your name: \t")

path = Path('guess.txt')
path.write_text(name_input)

print("")
############################################
print("Exercise 10.5")

name_input=input("Enter your name (quit to exit): \t")
path = Path('guess_book.txt')
total_input=""
active=True
while active:
    name_input=input("Enter another name (quit to exit): \t")
    if name_input!="quit":
        total_input+=f"{name_input}\n"
    else:
        active=False    

path.write_text(total_input)

print("")
############################################
print("Exercise 10.6")

try:
    number_1=float(input("Enter a number\t"))
    number_2=float(input("Enter another number\t"))
    print(number_1+number_2)
except ValueError:
    print("You didn't enter numbers")

print("")
############################################
print("Exercise 10.7")
answer=0
while True:
    first_number = input("Enter number: ")
    if first_number == 'q':
        break
    try:
        answer += float(first_number)
    except ValueError:
        print("you didn't add number")
    print(answer)

print("")
############################################
print("Exercise 10.8")
cat_names=""
path=Path("storing_data/cats.txt")
cat_names+="Garfield\n"
cat_names+="Freya\n"
cat_names+="Maya"
path.write_text(cat_names)

dog_names=""
path=Path("storing_data/dogs.txt")
dog_names+="Spot\n"
dog_names+="Max\n"
dog_names+="Donner"
path.write_text(dog_names)

path1=Path("storing_data/cats1.txt")
try:
    contents=path1.read_text()
    for line in contents.splitlines():
        print(line)
except FileNotFoundError:
    print("No such file: cats1.txt")

path2=Path("storing_data/dogs1.txt")
try:
    contents=path2.read_text()
    for line in contents.splitlines():
        print(line)
except FileNotFoundError:
    print("No such file: dogs1.txt")

print("")
############################################
print("Exercise 10.9")

path1=Path("storing_data/cats1.txt")
try:
    contents=path1.read_text()
    for line in contents.splitlines():
        print(line)
except FileNotFoundError:
    pass

path2=Path("storing_data/dogs1.txt")
try:
    contents=path2.read_text()
    for line in contents.splitlines():
        print(line)
except FileNotFoundError:
    pass

print("")
#############################################
print("Exercise 10.13")

name=input("Enter name\t")
surname=input("Enter surname\t")
age=input("Enter age\t")

person={
    "name":name,
    "surname":surname,
    "age":age
}

path3=Path("storing_data/person.json")
contents=json.dumps(person)
path3.write_text(contents)

path3=Path("storing_data/person.json")
contents=path3.read_text()
person1=json.loads(contents)

for key, value in person1.items():
    print(f"Key: {key}, Value: {value}")

print(f"name: {person1['name']}")
print(f"surname: {person1['surname']}")
print(f"age: {person1['age']}")
