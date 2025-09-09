valores = []
for i in range(10):  
    num = int(input(f"Digite o valor inteiro {i+1}: "))
    valores.append(num)

print("Valores armazenados:")
for valor in valores:
    print(valor)

print("Valores pares:")
for valor in valores:
    if valor % 2 == 0:
        print(valor)