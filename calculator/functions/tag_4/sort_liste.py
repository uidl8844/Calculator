import locale
#locale.setlocale(locale.LC_ALL, "de_DE")

liste = [3, 8, 5, 7, 8, 9]

liste = sorted(liste, reverse = True)
#print("sortierte Liste", liste)

# buchstaben sortieen
chars = ['a', 'f','d', 'z']
chars = sorted(chars)
#print("Chars:", chars)


# Groß-und Kleinbuchstaben sortieren

charst2 = ['a','f','d','z','B']
charst2 = sorted(charst2)
print("Chars:", charst2)

charst1 = ['a','f','d','z','B']
charst1 = sorted(charst1, key=lambda c: c.lower())
print(charst1)

string = "abcdeöäü"
chars3 = sorted(string, key=locale.strxfrm)
print(chars3)

#Dicts
snacks ={'Milka': 3.30, 'Kekse': 5.20, 'Snickers': 3.50}
snacks_sorted = sorted(snacks)
print("Sortierte snacks: ", snacks_sorted)

# nach preis sortiert:
snacks_sorted = sorted(snacks, key=lambda e: snacks[e])
print(snacks_sorted)

# sortiert nach preis und preis auch mitgegeben
snacks_sorted5 = sorted(snacks.items(), key=lambda e: e[1])
print(snacks_sorted5)

cities = {
    'Köln': 1200000,
    'Moskau': 10000000,
    'Berlin': 3400000,
    'München': 1600000,
    'Paris': 3800000,
}

#cities = sorted(cities.items(), key=lambda e: e[1], reverse=True)
#print(cities)

### snacks = {
  #  1: {'name': 'Erdnüsse', 'price': 200, 'amount': 50},
  #  2: {'name': 'Milka', 'price': 400, 'amount': 20},
   # 3: {'name': 'Snickers', 'price': 100, 'amount': 10},
#}
###
#snacks = sorted(snacks.items(), key=lambda e: e['price'], reverse=True)



monty_crew = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
monty_crew = sorted(monty_crew, key=lambda f: len(f))
print(monty_crew)