altura_parede = float(input("Digite a altura da parede: "))
largura_parede = float(input("Digite a largura da parede: "))
altura_azulejo = float(input("Digite a altura do azulejo: "))
largura_azulejo = float(input("Digite a largura do azulejo: "))

area_parede = altura_parede * largura_parede
area_azulejo = altura_azulejo * largura_azulejo

quantidade = area_parede / area_azulejo

print(f"Quantidade de azulejos necessários: {quantidade:.0f}")
