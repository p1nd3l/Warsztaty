import random


def guess_number():
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("To nie jest liczba!")
    return result


def guess_comparsion():
    computer_pick = random.randint(1, 100)
    user_pick = guess_number()
    while computer_pick != user_pick:
        if computer_pick > user_pick:
            print("To small")
        else:
            print("To big!")
        user_pick = guess_number()
    print("You Win!")


if __name__ == '__main__':
    guess_comparsion()
