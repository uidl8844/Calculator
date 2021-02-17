# Herkömliche Schreibweise einer Funktion:

def summe(a,b):
    return a+b+b

    print("Summe:", summe(3,3))

# Lambda Scheibweise: (Referenzen auf Lamba Funktionen sollten
# micht Variablen zugewiesen werden. Flake E731 Fehler
summe_lambda = lambda a, b: a+ b
print("Lambda Summe:", summe_lambda(4,4))


#Aufgabe: Lambda Funktion schreiben, die eine Kreisfläche beschreibt
# (Parameter: r)
Kreisflaeche = Lamba r: math.pi * r**2

# Lambda direkt ausführen
print("Kreisfläche direkt ausgeführt: ", lambda r: math.pi * r**2,(5))
