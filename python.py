1 Número positivo ou negativo

numero=input("digite um numero:")
numero=int(numero)
valida_pos=numero>0
valida_neg=numero<0
if valida_pos:
    print("o numero é positivo")
elif valida_neg:
    print("o numero é negativo")
else:
    print("o numero é zero")

2 Maior de idade

numero=input("digite um numero:")
numero=int(numero)
valida_maior=numero>=18
valida_menor=numero<18
if valida_maior:
    print("é maior de idade")
elif valida_menor:
    print("é menor de idade")
