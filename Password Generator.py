#Password Generator!
import random
import string


def restart():

    passord = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6)).lower()
    passord_list = [letter for letter in passord]
    print("Debug passord", passord)

    while True:
            guess = input("Gjett passordet med 6 ting eller skriv quit for å gi opp: ").lower()
            if guess == 'quit':
                 print("Imagia å gi opp, taper ass.")
                 break
            elif guess == passord:
                print("Du gjettet passordet gratulerer 🥂🥂")
                break
            elif:
                riktig_pososjon = sum(a == b for a, b in zip(guess, passord))
                print(f"❌Feil prøv igjen {riktig_pososjon} ting i riktig possisjon")
while True:
     restart()
     again = input("Vil du starte et nytt spill?: (yes/no)")
     if again != "yes":
        print("Taper fr, hadde")
        break