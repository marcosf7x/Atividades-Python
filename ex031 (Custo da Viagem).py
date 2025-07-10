distancia = int(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {float(distancia)}Km")
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da sua viagem será de R$ {preco:.2f}")