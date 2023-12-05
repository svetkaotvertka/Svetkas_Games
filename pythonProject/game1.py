import random

while True:
    user_action = input("Чем сходишь? Камнем, ножницами или бумагой? : ")

    possible_action = ["Камень", "Ножницы", "Бумага"]
    computer = random.choice(possible_action)

    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer}.\n")

    if user_action == computer:
        print(f"Оба пользователя выбрали {user_action}. Ничья!")
    elif user_action == "Камень":
        if computer == "Ножницы":
            print("Камень бьт ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень. Вы проиграли")
    elif user_action == "Бумага":
        if computer == "Камень":
            print("Бумага оборачивает Камень! Вы победили!")
        else:
            print("Ножницы режут бумагу!. Вы проиграли")
    elif user_action == "Ножницы":
        if computer == "Бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы!. Вы проиграли")
    play_again = ""
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break
