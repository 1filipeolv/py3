salario = float(input("Digite o salário mensal atual: "))
percentual = float(input("Digite o percentual de reajuste: "))

novo_salario = salario + (salario * percentual / 100)

print(f"O novo salário é {novo_salario}")