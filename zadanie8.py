
# Zmienna, która trzyma informację, czy pada deszcz
pada = False
# Licznik odpowiedzi "nie"
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        pada = True  # Kończymy pętlę, gdy użytkownik odpowie "tak"
    elif odpowiedz == "nie":
        licznik_nie += 1  # Zwiększamy licznik odpowiedzi "nie"
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
        
# Po zakończeniu pętli program wypisuje liczbę odpowiedzi "nie"
print(f"Zgadłeś! Liczba odpowiedzi 'nie': {licznik_nie}")
