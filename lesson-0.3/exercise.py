letra = input("Digite uma letra: ").lower()

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"A letra '{letra}' é uma vogal.")
    case _:
        print("Por favor, digite apenas uma letra.")
