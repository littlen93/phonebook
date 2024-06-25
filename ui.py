from logger import (
    print_full_data,
    read_txt,
    add_user,
    find_by,
    edit_info,
    copy_to_file,
    move_to_file,
    remove_data,
)


def work_with_phonebook():

    choice = show_menu()
    filename = "phon.txt"

    while choice != 0:
        phb_list = read_txt(filename)
        if choice == 1:
            print_full_data(phb_list)
        elif choice == 2:
            add_user(filename)
        elif choice == 3:
            phone = input("Введите номер/имя/фамилию: ")
            find_by(filename, phone)
        elif choice == 4:
            edit_info(filename)
        elif choice == 5:
            new_filename = input("Введине название файла для копирования: ") + ".txt"
            copy_to_file(filename, new_filename)
            print("Информация об абоненте успешно скопирована в файл", new_filename)
        elif choice == 6:
            new_filename = input("Введине название файла для перемещения: ") + ".txt"
            move_to_file(filename, new_filename)
            print("Информация об абоненте успещно перемещена в файл", new_filename)
        elif choice == 7:
            remove_data(filename)
            print("Информация о  контакте удалена")

        choice = show_menu()


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь сравочник\n"
        "2. Добавить абонента в справочник\n"
        "3. Найти абонента\n"
        "4. Изменить данные\n"
        "5. Скопировать контакт в другой файл\n"
        "6. Переместить контакт в другой файл\n"
        "7. Удалить контакт\n"
        "0. Закончить работу"
    )
    choice = int(input())
    return choice
