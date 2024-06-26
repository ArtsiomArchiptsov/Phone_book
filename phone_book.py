import csv, os, sys

# Меню пользователя(возможно изменится)

def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Заполнить данные о пользователе\n"              # write_users(file_name)
        "2. Вывести информацию о пользователях на экран\n"  # read_users(file_name)
        "3. Поиск абонемента в справочнике\n"               # find_users(file_name)
        "4. Удаление файла\n"                               # del_users(file_name)              
        "5. Удаление абонента по фамилии\n"                 # del_users(file_name)
        "6. Форматирование данных абонента\n"               # format_users_date(file_name)
        "7. Закончить работу"
    )
    choice = int(input())
    return choice

# Основная программа

def work_with_phonebook():
    file_name = "phone_book.csv"
    choice=show_menu()
    while (choice!=7):
        
        if choice==1:
            
            write_users(file_name) # Заполнить данные о пользователе
            
            print("Продолжить работу? Да/Нет")
            answer1 = input()
            
            if answer1.lower() == 'да':
                pass
            elif answer1.lower() == 'нет':
                choice=show_menu()
                
        elif choice==2:
            
            read_users(file_name)  # Вывести информацию о пользователях на экран
            
            print("Продолжить работу? Да/Нет")
            answer2 = input()
            
            if answer2.lower() == 'да':
                pass
            elif answer2.lower() == 'нет':
                choice=show_menu()
                
        elif choice==3:
            
            find_users(file_name) # Поиск абонемента в справочнике
            
            print("Продолжить работу? Да/Нет")
            answer3 = input()
            
            if answer3.lower() == 'да':
                pass
            elif answer3.lower() == 'нет':
                choice=show_menu()
                
        elif choice==4:
            
            deleting_file(file_name) # Удаление файла
            
            print("Продолжить работу? Да/Нет")
            answer4 = input()
            
            if answer4.lower() == 'да':
                pass
            elif answer4.lower() == 'нет':
                choice=show_menu()
                
        elif choice==5:
            
            del_users(file_name)   # Удаление абонента по фамилии
            
            print("Продолжить работу? Да/Нет")
            answer5 = input()
            
            if answer5.lower() == 'да':
                pass
            elif answer5.lower() == 'нет':
                choice=show_menu()  
            
        elif choice==6:
            
            format_users_date(file_name)    # Редактирование данных пользователя  
            
            print("Продолжить работу? Да/Нет")
            answer6 = input()
            
            if answer6.lower() == 'да':
                pass
            elif answer6.lower() == 'нет':
                choice=show_menu() 
                
        elif choice==7:
            
            sys.exit()


# Заполнение данных пользователя в список
def user_data():
    print("Введите Ваше имя")
    name = input().title()
    print("Введите Вашу фамилию")
    surname = input().title()
    print("Введите номер Вашего телефона")
    phone = input().title()
    print("Введите Ваш адрес")
    address = input().title()
    return name, surname, phone, address


# Сохраняем данные о пользователе в файл
def write_users(file_name):
    with open(file_name, "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name", "Surname", "Phone", "Address"]
        
        # Проверяем пустой ли файл
        if csvfile.tell() == 0:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        # Запрашиваем данные у пользователя
        name, surname, phone, address = user_data()
        # Записываем данные в файл
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(
            {"Name": name, "Surname": surname, "Phone": phone, "Address": address}
        )
        print(f"Данные успешно записаны в файл {file_name}")

# Выводим информацию о пользователе из файла
def read_users(file_name):
    # открываем файл для чтения
    with open(file_name, "r", newline="", encoding="utf-8") as csvfile_object:
        reader = csv.DictReader(csvfile_object)
        # считываем каждую строку в файле и выводим на экран
        for row in reader:
            print(row["Name"], row["Surname"], row["Phone"], row["Address"])
            
# Поиск пользователя по его даным(имя, фамилия, номер телефона, адрес) 
def find_users(file_name):
    # открываем файл для чтения
    with open(file_name, "r", newline="", encoding="utf-8") as csvfile_object:
        reader = csv.DictReader(csvfile_object)
        # Ввод данных для поиска
        print("Введите данные для поиска.")
        subscriber = input().title()
        # считываем каждую строку в файле и выводим на экран
        for row in reader:
            if subscriber == row["Name"] or subscriber == row["Surname"] or subscriber == row["Phone"] or subscriber == row["Address"]:                
                print(row["Name"], row["Surname"], row["Phone"], row["Address"])
                
# Удаление файла
def deleting_file(file_name):    
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Файл {file_name} успешно удален")
    else:
        print(f"Файл {file_name} не существует")

# Удаленение информации о пользователе
def del_users(file_name):
    rows = []  # список для хранения строк файла

    with open(file_name, "r", newline="", encoding="utf-8") as csvfile_object:
        reader = csv.DictReader(csvfile_object)
        
        print("Введите фамилию абонемента, которого нужно удалить: ")
        subscriber_del = input().title()

        for row in reader:
            if row["Surname"] != subscriber_del: # предполагаемое поле с номером строки в файле                 
                rows.append(row)

    # записываем новые данные в файл без удаленной строки  
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile_object:
        fieldnames = reader.fieldnames  
        writer = csv.DictWriter(csvfile_object, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
                
# Редактирование данных пользователя        

def format_users_date(file_name):
    # Создаем список для хранения строк файла  
    rows = []

    # Чтение данных из файла  
    with open(file_name, "r", newline="", encoding="utf-8") as csvfile_object:
        reader = csv.DictReader(csvfile_object)

        print('Введите абонента')
        print('Фамилия:')
        subscriber_surname = input().title()
        print('Имя:')
        subscriber_name = input().title()

        # Поиск абонента  
        for row in reader:
            if subscriber_surname == row['Surname'] and subscriber_name == row['Name']:
                print(row["Name"], row["Surname"], row["Phone"], row["Address"])
        
        print("Введите данные для форматирования: ")
        subscriber_date = input().title()
        print("Введите новое значение: ")
        new_subscriber_date = input().title()

        # Второй проход для форматирования данных  
        csvfile_object.seek(0)  # Сброс указателя файла  
        next(reader)  # Пропускаем заголовок  
        for row in reader:
            if subscriber_date in row.values():
                updated_row = {key: new_subscriber_date if value == subscriber_date else value for key, value in row.items()}
                rows.append(updated_row)
            else:
                rows.append(row)

    # Запись обновленных данных в файл  
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile_object:
        fieldnames = reader.fieldnames  
        writer = csv.DictWriter(csvfile_object, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)                     


work_with_phonebook()