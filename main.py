a = input("zadej první číslo: ")
b = input("zadej druhý číslo: ")
c = input("zadej znak (+ - * (/ deleno s desetinim číslem //deleno bez desetiného čísla)):  ")
a = int(a)
b = int(b)
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "//":
    print(a // b)
else:
    print("nesaprávný text")
