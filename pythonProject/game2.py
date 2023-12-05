import random

guesses_made = 0
name = input("Привет! \nКак тебя зовут?\n")

number = random.randint(1, 30)
print("Отлично, {0} , я загадал число между 1 и 30. Сможешь угадать?" .format(name))
while guesses_made < 6:
    guess = int(input("введите число"))
    guesses_made += 1
    if guess < number:
        print("твое число меньше того, что я загадал!")
    if guess > number:
        print("Твое число больше того, что я загадал")
    if guess == number:
        break
if guess == number:
        print("Пиздос, {0}! Ты угадал, сучка! Использовав всего {1} опыток!".format(name, guesses_made))
else:
        print("А вот и наебался! Я загадал число {0}".format(number))
