votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

total = votos_brancos + votos_nulos + votos_validos

perc_brancos = (votos_brancos * 100) / total
perc_nulos = (votos_nulos * 100) / total
perc_validos = (votos_validos * 100) / total

print(f"Total de eleitores: {total}")
print(f"Percentual de votos brancos: {perc_brancos:.2f}%")
print(f"Percentual de votos nulos: {perc_nulos:.2f}%")
print(f"Percentual de votos válidos: {perc_validos:.2f}%")
