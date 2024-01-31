def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "STOP! Dzielenie przez 0 jest niedozwolone"

print("PROSTY KALKULATOR")

while True:
    print("\nOperacja:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Operacja nr (1/2/3/4/5): ")

    if wybor == '5':
        print("Koniec programu.")
        break

    if wybor not in ('1', '2', '3', '4'):
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        continue

    liczba1 = float(input("Pierwsza liczba: "))
    liczba2 = float(input("Druga liczba: "))

    if wybor == '1':
        print(f"Wynik: {dodawanie(liczba1, liczba2)}")
    elif wybor == '2':
        print(f"Wynik: {odejmowanie(liczba1, liczba2)}")
    elif wybor == '3':
        print(f"Wynik: {mnozenie(liczba1, liczba2)}")
    elif wybor == '4':
        print(f"Wynik: {dzielenie(liczba1, liczba2)}")

