vetor = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

print("Os números digitados foram:")
for valor in vetor:
    print(valor)