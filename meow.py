import json

def allpass(): #высвечивает все пароли
    with open("password.json", "r") as file:
        x = json.load(file)
        for i, v in enumerate(x, start=1):
            print(i, v)

choice4 = int(input("Показать все пароли[1] или добавить новый[2]? ")) #дает выбор
while choice4 not in [1, 2]:
    choice4 = input("Неверный ввод. Введите '1' или '2': ").lower()

if choice4 == 1:
    allpass()
else:
    name = input("Имя приложения: ")
    password = input("Пароль: ")

    def create_json():  # создание пароля
        json_data = [{
            name: password
        }]
        with open("password.json", "w") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)


    def add_to_json():
        with open("password.json", "r") as file:
            data = json.load(file)
        json_data = {
            name: password
        }
        data.append(json_data)
        with open("password.json", "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    add_to_json()

if choice4 == 2:
    choice = input("Показать все пароли?[y/n] ") #просмотр всех паролей
    while choice not in ['y', 'n']:
     choice = input("Неверный ввод. Введите 'y' или 'n': ").lower()
    if choice == 'y':
        allpass()

def delete_number(): #функция удаления пароля
    with open("password.json", "r") as file:
        x = json.load(file)
        y = int(input("Что вы хотите убрать?[выберите число] "))
        while y > len(x) or y < 0:
            y = int(input("Этого числа нет в списке. Выберите другое число. ").lower())
        for i, v in enumerate(x, start=1):
            if y == i:
                del x[i - 1]
        with open('password.json', 'w') as outfile:
            json.dump(x, outfile, ensure_ascii=False, indent=2)
        allpass()
    que()

def que(): #функция для вопроса и повторения функции удаления пароля
    choice3 =input("Хотите удалить что-то ещё?[y/n] ")
    while choice3 not in ['y', 'n']:
        choice3 = input("Неверный ввод. Введите 'y' или 'n': ").lower()
    if choice3 == 'y':
        delete_number()

choice2 = input("Хотите удалить пароли?[y/n] ") #удаление пароля
while choice2 not in ['y', 'n']:
    choice2 = input("Неверный ввод. Введите 'y' или 'n': ").lower()

if choice2 == 'y':
    delete_number()

choice5 = input("Сохранить данные перед окончанием?[y/n] ") #exit
while choice5 not in ['y', 'n']:
    choice5 = input("Неверный ввод. Введите 'y' или 'n': ").lower()

if choice5 == 'n':
    with open("password.json", "r") as file:
        x = json.load(file)
    y = len(x)
    for i, v in enumerate(x, start=1):
        if y == i:
            del x[i - 1]
    with open('password.json', 'w') as outfile:
        json.dump(x, outfile, ensure_ascii=False, indent=2)

