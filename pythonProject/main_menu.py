

def main_menu():
    print("Привет, выбери игру:")
    print("1. Камень, ножницы, бумага")
    print("2. Угадай число")
    choise = input("Введите номер игры")

    if choise == "1":
         import game1
    elif choise == "2":
         import game2
    else:
        print("Неверный выбор. Попробуй еще раз.")
        main_menu()


main_menu()