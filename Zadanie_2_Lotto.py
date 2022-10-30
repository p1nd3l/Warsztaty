import random


def liczba():
    # Pętla while sprawdza, czy wprowadzony typ danych jest liczbą. Po czym zwraca liczbę.
    while True:
        try:
            number = int(input("Podaj liczby do lotto w zakresie 1-49: "))
            break
        except ValueError:
            print("To nie jest liczba!")
    return number


def liczby():
    # Jeżeli liczba jest int, to dodaj ją do listy. Jeżeli oczywiście znajduje się w zakresie 1 - 49 i nie powtarza się.
    numbers = []
    lista_liczb = [*range(1, 50)]
    while len(numbers) < 6:
        number = liczba()
        if number not in numbers and 0 < number <= 49:
            numbers.append(number)
        elif number in numbers:
            print("Wybierz inną liczbę! Powtarza się.")
        else:
            print("Liczba poza zakresem!")
    return numbers


def losowanie_gracz():
    # Posortowanie liczb od największej do najmniejszej.
    numbers = liczby()
    posortowane = sorted(numbers)
    return posortowane


def losowanie_komp():
    # Komputer losuje 6 liczb za pomocą metody shuffle.
    comp_choice = []
    for i in range(1, 50):
        comp_choice.append(i)
    random.shuffle(comp_choice)
    return comp_choice[:6]


def lotto():
    # Porównanie liczb gracza i losów komputera:
    player_numbers = losowanie_gracz()
    print(f"Twoje liczby lotto: {player_numbers}")
    computer_numbers = losowanie_komp()
    print(f"Liczby totolotka to: {computer_numbers}")
    trafien = 0
    for number in player_numbers:
        if number in computer_numbers:
            trafien += 1
    if trafien == 6:
        print("Wspaniale! 6 trafień. Może warto pomyśleć o prawdziwym totolotku")
    elif trafien == 5:
        print("Brawo! 5 trafień! ")
    elif trafien == 4:
        print("4 trafienia. No to już ładnie")
    elif trafien == 3:
        print("3 - zawsze coś. Zawsze coś.")
    elif trafien == 2:
        print("2 trafienia")
    elif trafien == 1:
        print("1 trafienie")
    else:
        print("Oooops! Zero trafień.")


if __name__ == '__main__':
    lotto()
