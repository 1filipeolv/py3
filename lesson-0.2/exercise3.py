estatura1 = float(input('Digite a estatura da 1a pessoa: '))
estatura2 = float(input('Digite a estatura da 2a pessoa: '))
estatura3 = float(input('Digite a estatura da 3a pessoa: '))

if estatura1 >= estatura2 and estatura1 >= estatura3:
    maior = estatura1
    if estatura2 >= estatura3:
        meio = estatura2
        menor = estatura3
    else:
        meio = estatura3
        menor = estatura2
elif estatura2 >= estatura1 and estatura2 >= estatura3:
    maior = estatura2
    if estatura1 >= estatura3:
        meio = estatura1
        menor = estatura3
    else:
        meio = estatura3
        menor = estatura1
else:
    maior = estatura3
    if estatura1 >= estatura2:
        meio = estatura1
        menor = estatura2
    else:
        meio = estatura2
        menor = estatura1

print(f'Estaturas em ordem decrescente: {maior}, {meio}, {menor}')
