import random


def hangman():
    print("здарова, ублюдок, будем в висилицу катать?")

    wordlist = ["хуйло", "пидорас", "уёбок", "гнида", "петух", "наркоман"]
    secret = random.choice(wordlist)
    guesses = "ауоыиэяюёе"
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end="")
            else:
                print("_", end="")
                missed += 1
                if missed == 0:
                    print("\nТы выиграл!")
                    break
                guess = input("\nНапиши букву, пидор")
                guesses += guess

                if guess not in secret:
                    turns -= 1
                    print("\nха-ха неудачник, не угадал!")
                    print("\nОсталось попыток:", turns)
                    if turns < 5:
                        print("\n   |   ")
                    if turns < 4:
                        print("     0   ")
                    if turns < 3:
                        print(r"    /|\  ")
                    if turns < 2:
                        print("     |   ")
                    if turns < 1:
                        print(r"     /\  ")
                    if turns == 0:
                        print("\n\nЭто слово:", secret)
    ans = "да"
    while ans == "да":
        hangman()
        print("Пидраок, хочешь ли ты продолжить? да|нет")
