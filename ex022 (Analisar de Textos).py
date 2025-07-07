# frase = "Curso em Vídeo Python"
# x = frase.title()
# print(x)

# nome = input("Digite o seu nome e sobrenome: ")
# x1 = len(nome)
# print(nome, x1)
# x = nome.strip()
# x2 = len(x)
# print(nome, x2)

# frase = 'Curso em Vídeo Python'
# print('-'.join(frase.split()))

nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando o seu nome...")
# p_nome = nome.split()
print(f"Esse é o seu nome em letras maiúsculas: {nome.upper()} \n Esse é o seu nome em letras minúsculas: {nome.lower()} \n Ele possui essa quantidade de letras: {len(nome.replace(" ",""))} \n Seu primeiro nome possui essa quantidade de letras: {nome.find(' ')}")
# print(f"Seu primeiro nome é {p_nome[0]} e ele possui essa quantidade de letras: {len(p_nome[0])}")