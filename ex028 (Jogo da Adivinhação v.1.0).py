# tempo = int(input("Quanto tempo tem o seu carro? "))
# # print('Carro novo' if tempo <= 3 else 'Carro velho')
# if tempo <= 3:
#     print("O seu carro ainda é novo!")
# else:
#     print("O seu carro já está em uma idade mais avançada!")
# print("Fimal")

# ------------------------

# nome = str(input('Qual é o seu nome?')).strip().lower().capitalize()
# if nome == 'Felipe':
#     print('Nome extremamente Based, irmão!')
# # else:
# #     print('Nome de beta totalmente escalifado!')
# print(f'Força e Honra meu amigo {nome}!')

# ------------------------

# n1 = float(input("Digite sua primeira nota: "))
# n2 = float(input("Digite sua segunda nota: "))
# if (n1 + n2) / 2 >= 7:
#     print(f"Sua nota foi {(n1 + n2) / 2} Você passou no semestre!")
# else:
#     print(f"Sua nota foi {(n1 + n2) / 2} Você reprovou no semestre!")
# print("Continue na pegada!")

# ------------------------
import time
import random
import colorama
from colorama import Back
colorama.init()

print("---=---" * 11)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar qual se trata...")
print("---=---" * 11)
aleatorio = random.randint(0,5)
meu_numero = int(input("Em que número eu pensei? R= "))
print(Back.LIGHTBLUE_EX + "PROCESSANDO..." + Back.RESET)
time.sleep(1)
if meu_numero == aleatorio:
    print("PARABÉNS! Você conseguiu acertar!")
else:
    print(f"Infelizmente pensei no {aleatorio}. Você PERDEU! \n Tente novamente.")
