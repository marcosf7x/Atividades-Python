import colorama
from colorama import Fore
colorama.init()

velocidade = int(input("Qual a velocidade atual do carro? "))
if velocidade <= 80:
    print(Fore.YELLOW + "Tenha um bom dia! Viaje com segurança." + Fore.RESET)
else:
    print(Fore.RED + "Velocidade acima do valor permitido para a rodovia (80 km/h) \n Você acaba de ser multado em R$ 300,00!" + Fore.RESET)
    print(Fore.YELLOW + "Tenha um bom dia! Viaje com segurança." + Fore.RESET)
    print(f"Sua velocidade registrada foi de {Fore.GREEN + velocidade + Fore.RESET}")