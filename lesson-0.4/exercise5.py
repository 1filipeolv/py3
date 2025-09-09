times = []
print("Digite os nomes dos times de futebol (digite 'fim' para encerrar):")
while True:
    time = input()
    if time.lower() == 'fim':
        break
    times.append(time)

print("Times digitados:")
for time in times:
    print(time)