from data_create import name_data, surname_data, phone_data, description_data

fields = ["Фамилия", "Имя", "Телефон", "Описание"]


def print_full_data(data: list):
    for person in data:
        for k, v in person.items():
            print(f"{k}: {v}")
        print()


def print_short_data(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        ind = 1
        print("\nТекущие контакты в файле", filename)
        for i in f:
            surname, name, phone, descr = i.split(",")
            print(f"{ind}.", surname, name, phone, descr, end="")
            ind += 1
        return ind - 1


def read_txt(filename: str):
    data = []
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            if line == "\n":
                continue
            record = [i.strip() for i in line.split(",")]
            data.append(dict(zip(fields, record)))
    return data


def add_user(filename: str):
    with open(filename, "a", encoding="utf-8") as phb:
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        description = description_data()
        print(surname, name, phone, description, sep=",", end="\n", file=phb)


def find_by(filename: str, data: str):
    with open(filename, "r", encoding="utf-8") as phb:
        search_list = phb.readlines()
        for i in search_list:
            if data in i:
                for k, v in dict(zip(fields, i.strip().split(","))).items():
                    print(f"{k}: {v.strip()}", end="\n")
                print()


def edit_info(filename: str):
    print_short_data(filename)
    with open(filename, "r+", encoding="utf-8") as file:
        current_list = file.readlines()
        selected = validate_index(len(current_list))
        current_list[selected] = (
            f"{surname_data()},{name_data()},{phone_data()},{description_data()}\n"
        )
        file.seek(0)
        file.writelines(current_list[: selected + 1])


def copy_to_file(filename: str, new_filename: str):
    print_short_data(filename)
    with open(filename, "r", encoding="utf-8") as file:
        current_list = file.readlines()
        user_ind = validate_index(len(current_list))
        user_to_move = current_list[user_ind]
        with open(new_filename, "a", encoding="utf-8") as phout:
            phout.write(user_to_move)
            phout.seek(0)
            print_full_data(read_txt(new_filename))
        return user_ind


def remove_data(filename: str, ind=None):
    length = print_short_data(filename)
    if ind is None:
        ind = validate_index(length)
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        data = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(data[:ind])
        f.writelines(data[ind + 1 :])
    print_short_data(filename)


def move_to_file(filename: str, new_filename: str):
    remove_data(filename, ind=copy_to_file(filename, new_filename))


def validate_index(length):
    selected = int(input("Введите номер контакта из списка: ")) - 1
    while selected < 0 or length <= selected:
        print("Ошибка ввода. Введите корректный номер")
        selected = int(input("Введите номер абонента из списка: ")) - 1
    return selected
