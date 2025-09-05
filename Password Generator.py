#Password Generator!
import random
import string

passord = ''.join(random.choice(string.ascii_letters) for _ in range(4))

print("Generate Passord", passord)

while True:
        guess1 = input("Gjett passordet med 4 bokstaver: ")

        if guess1 == passord:
            print("Du gjettet passordet gratulerer 🥂🥂")
            break
        else:
            riktig_pososjon = sum(a == b for a, b in zip(guess1, passord))
            print(f"❌Feil prøv igjen {riktig_pososjon} bokstaver i riktig possisjon")