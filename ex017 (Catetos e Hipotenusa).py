import math
from math import hypot

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
print(f"A hipotenusa vai medir: {math.hypot(oposto, adjacente):.2f}")
# print(f"A hipotenusa vai medir: {math.sqrt(oposto * oposto + adjacente * adjacente)}")
# Resolução matemática:
# co = float(input("Valor do Oposto: "))
# ca = float(input("Valor do Adjacente: "))
# hip = (co ** 2 + ca ** 2) ** (1/2)
# print(f"A soma do oposto {co} e do adjacente {ca} é a hipotenusa: {hip:.2f}")