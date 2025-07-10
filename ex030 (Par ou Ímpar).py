import colorama
from colorama import Fore
colorama.init()

numero = int(input("Me diga um número qualquer: "))
resto = numero % 2
if resto == 0:
    print(Fore.BLUE + f"O número {numero} é PAR" + Fore.RESET)
else:
    print(Fore.RED + f"O número {numero} é ÍMPAR" + Fore.RESET)