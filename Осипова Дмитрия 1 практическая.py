# Задание 1
games = list()
game = input("Введите настольную игру (0 - конец ввода): ")
while game != "0":
    if game in games:
        print("Эта игра уже записана")
    else:
        games.append(game)
        games.sort()
    game = input("Введите настольную игру (0 - конец ввода): ")
print(games)

# Задание 2
marks = list(map(int, input("Введите оценки через пробел: ").split()))
print(marks)

stable = True
for i in range(1, len(marks)):
    if marks[i] < marks[i - 1]:
        stable = False
        break
if stable:
    print("Стабильная успеваемость")
else:
    print("Стабильной успеваемости нет")

# Задание 3
def print_students(students):
    students.sort()
    for i in range(len(students)):
        print(str(i + 1) + ".", students[i])
        
my_students = ["Абрикосов", "Воробъв", "Лисицин", "Олейкин", "Щукина"]
print_students(my_students)
new_students = input("Введите фамилию нового ученика: ")
my_students.append(new_students)
print_students(my_students)

# Задание 4
times = list(map(int, input("Введите время тестов (мс) через пробел: ").split()))

for i in range(1, len(times)):
    if times[i] > times[i - 1]:
        print("Тест №" + str(i + 1) + ":", times[i], "мс")

# Задание 5
items = input("Введите элементы через пробел: ").split()
result = items[::2]
print("".join(result))

# Задание 6
from random import randint

surnames = input("Введите фамилии учеников через пробел: ")
students = surnames.split()
amount = len(students)

numbers =list()
for students in students:
    numbers.append(randint(1, amount))
    
print("Распределение вариантов контрольной работы")
for i in range(amount):
    print(students[i], "-", numbers[i])

# Задание 7
marks = list(map(int, input("Введите оценки через пробел: ").split()))
print(marks)

good = 0
for mark in marks:
    if mark in [5,4,3]:
        good += 1
        
progress = good / len(mark) * 100
print("Успеваемость:", str(round(progress)) + "%")

# Задание 8
marks = list(map(int, input("Введите оценки через пробел: ").split()))

fives = 0
for mark in marks:
    if mark == 5:
        fives += 1
        
percent = fives / len(marks) * 100
print("Получено пятёрок (%) -", round(percent))

# Задание 9
surname = input("Введите фамилию преподавателя: ")
position = input("введите должность: ")

groups = input("Введите количество студентов в группах через пробел: ")
groups = list(map(int, groups.split()))

mentor = [surname, position, groups]
print(mentor)