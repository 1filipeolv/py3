n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))

opcao = int(input("1 Média ponderada, com pesos 2 e 3 respectivamente \n2. " 
"Quadrado da soma dos 2 números \n3. Cubo do menor número.3. Escolha uma opção "))

if opcao == 1:
    media = (n1 * 2 + n2 *3) / 5
    print(f"A média é {media}")
elif opcao == 2:
    quadrado = (n1 + n2) ** 2
    print(f"O quadrado da soma é {quadrado}")
elif opcao == 3 :
    if n1 > n2:
        cubo = n2 ** 3
    else:
        cubo = n1 ** 3
    print(f"O cubo do menor numero é {cubo}")
else:
    print("Opção inválida")