import random


def uzytkownik():
    """Zwróć poprawną wartość do odpowiedzi.

    :rtype: str
    :return: value provided by user from [1] za dużo [2] Za mało [3] Wygrałeś!
    """
    odpowiedzi = ["1", "2", "3"]
    while True:
        odpowiedz = input()
        if odpowiedz in odpowiedzi:
            break
        print("Odpowiedź nieprawidłowa. Wybierz [1] za dużo | [2] Za mało | [3] Wygrałeś!")
    return odpowiedz


def menu():
    print("Pomyśl liczbę od 0 do 1000, a ja zgadnę w max. 10 próbach")
    print("Wybierz [1] za dużo | [2] Za mało | [3] Wygrałeś!")
    print("Wciśnij Enter, aby zacząć!")
    input()
    min_liczba = 0
    max_liczba = 1000
    odpowiedz = ""
    while odpowiedz != "3":
        for i in range(10):
            guess = int((max_liczba - min_liczba) / 2 + min_liczba)
            print(f"Zgaduję, że to: {guess}")
            odpowiedz = uzytkownik()
            if odpowiedz == "1":
                max_liczba = guess
            elif odpowiedz == "2":
                min_liczba = guess
            elif odpowiedz == "3":
                break
        else:
            print("Czy Ty aby nie oszukujesz?", "\n")
            return menu()
    print("Wygrałem!")


if __name__ == '__main__':
    menu()
