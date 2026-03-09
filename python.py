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