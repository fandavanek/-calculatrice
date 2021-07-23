a = input("zadej první číslo: ")
b = input("zadej znak (+ - * (/ deleno s desetinim číslem //deleno bez desetiného čísla)):  ")
c = input("zadej druhý číslo: ")
a = int(a)
c = int(c)
if b == "+":
    print(a + c)
elif b == "-":
    b = print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
elif b == "//":
    print(a // c)
o = input("vypneš napsáním textu vypnout: ")
