texto = input("Informe um texo: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável.
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()  # Adiciona uma quebra de linha.
print("Executa no final do Loop")

# Exemplo utilizandoa função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
