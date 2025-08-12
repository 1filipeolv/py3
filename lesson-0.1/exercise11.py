nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade comprada: "))
preco = float(input("Digite o preço unitário: "))

total = quantidade * preco

print(f"Produto: {nome}")
print(f"Total: {total:.2f}")
