# Fatiamento de strings é uma técnica utilizada para retornar substrings(partes da string origial),
# informando inicio(start), fim(stop) e passo (step): [start stop[,step]].

nome = "Guilherme Arthur de Carvalho"

nome[0]
print("1º -", nome[0])

nome[:9]
print("2º -", nome[:9])

nome[10:]
print("3º -", nome[10:])

nome[10:16]
print("4º -", nome[10:16])

nome[10:16:2]
print("5º -", nome[10:16:2])

nome[:]
print("6º -", nome[:])

nome[::-1]
print("7º -", nome[::-1])
