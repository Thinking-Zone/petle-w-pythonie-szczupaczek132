import random

def czy_pada():
    return random.choice([True, False]) 

def zgadnij_pogode():
    print("Zgadnij, czy pada deszcz.")
    
    while True:
        odpowiedz = input("Czy pada? (tak/nie): ").strip().lower()  
        if odpowiedz not in ['tak', 'nie']:
            print("Proszę odpowiedzieć 'tak' lub 'nie'.")
            continue
        
        pada = czy_pada()  

        if (odpowiedz == 'tak' and pada) or (odpowiedz == 'nie' and not pada):
            print("Brawo! Zgadłeś/aś!")
            break  
        else:
            print("Niestety, spróbuj ponownie.")
