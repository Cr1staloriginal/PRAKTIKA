# Задание 1
authors = {
    "Пушкин": "Русский поэт, драматург и прозаик. Один из самых авторитетных литературных деятелей первой трети XIX века",
    "Толстой": "Один из наиболее известных русских писателей и мыслителей, один из величпйших писателей-романистов мира",
    "Бунин": "Русский писатель, поэт и переводчик, лауреат Нобелевской премии по литературе 1933 года"}

surname = input("Введите фамилию атвора: ")
if surname in authors:
    print("Биография:", authors[surname])
else:
    print("Автор не найден, Вы хотите добавить его?")
    answer = input()
    if answer == "Да":
        biography = input("Введите биографию автора: ")
        authors[surname] = biography
    else:
        print("Получено")

# Задание 2
student_card = {"номер": "324", "фамилия": "Иванов"}

print("Добро пожаловать!")
print(student_card)

main = "Что вам нужно? 1 - Взять книгу, 2 - Вернуть книгу, 3 - Выйти из библиотеки"
action = input(main)
while action != "3":
    if action == "1":
        book = input("Введите название книги: ")
        student_card["долг"] = book
        print(student_card)
    elif action == "2":
        if "долг" in student_card:
            del student_card["долг"]
        else:
            print("Книг нет")
        print(student_card)
    action = input(main)

print("Ждём вас: ")
print(student_card)

# Задание 3
def application():
    contestans = dict()
    name = input("Введите фамилию участника (0 - завершить)")
    while name != "0":
        poem = input("Введите название произведения")
        contestans[name] = poem
        name = input("Введите фамилию участника (0 - завершить)")
    return contestans

def get_artists(poem):
    artists = list()
    for name in contestans.keys():
        if contestans[name] == poem:
            artists.append(name)
    artists.sort()
    return artists

contestans = application()
contestans.set(contestans.values())

print("Программа концерта")
for poem in poems:
    print(poem + ":", ",".join(get_artists(poem)))

# Задание 4
def make_reader_card():
    numbers = input("Введите номера прочитанных книг через пробел: ").split()
    card = set(map(int, numbers))
    return card

def print_book(data):
    numbers = list(data)
    numbers.sort()
    count = 1
    for number in numbers:
        if number in books:
            print(count, "-", books[number])
            count +=1

books = {114: "Пиковая дама. Пушкин",
         830: "Гарри Потер. Роулинг",
         508: "Тарас Бульба. Гоголь",
         922: "Остров сокровищ. Стивинсон",
         152: "Властелин колец. Толкин",
         252: "Три мушкитёра. Дюма",
         749: "Руслан и Людмила. Пушкин",
         240: "Гамлет. Щекспир"}
print("Первый читатель")
reader_1 = make_reader_card()
print("Второй читатель")
reader_2 = make_reader_card()

print("Рекомендации для первого читателя:")
print_book(reader_2.difference(reader_1))
print("Рекомендации для второго читателя:")
print_book(reader_1.difference(reader_2))

# Задание 5
text = input("Введите текст: ")
words = text.split()

counts = dict()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

best_word = ""
best_count = 0
for word in counts.keys():
    if counts[word] > best_count:
        best_count = counts[word]
        best_word = word

print(best_word)

# Задание 6
souvenirs = {
    "футболки": ["I love Pushkin!", "Это время - трудновато для пера", "Здоровы и нормальны только заурядные люди"],
    "браслеты": ["Читайте, завидуйте, я - гражданин!", "Гой ты, Русь моя родная!"],
    "сумки": ["С портретом Чехова", "С цитатой гоголя", "С пером"]
}

prices = {"1": 1500, "2": 300, "3": 600}

print("Ассортимент магазина:")
for kind in souvenirs.keys():
    print(kind)
    for item in souvenirs[kind]:
        print("-", item)

print("Что желаете? 1-футболка, 2-браслет, 3-сумка")
choice = input(">>> ")
if choice in prices:
    print("К оплате:", prices[choice], "рублей")
else:
    print("Такого товара нет")