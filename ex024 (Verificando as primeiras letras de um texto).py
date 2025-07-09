cidade = str(input("Em que cidade você nasceu? ")).strip().lower().title()
# cidade_2 = cidade.strip().lower().title()
analise = "Santo" in cidade
# print(f"Esse foi o nome da cidade que você digitou: {cidade} o seu número de caracteres {len(cidade)}")
print(f"{analise} e a quantidade de caracteres atualizado {len(cidade)} e o nome atualizado {cidade}")
# print("analise")