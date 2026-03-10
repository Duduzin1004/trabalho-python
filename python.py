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

Senha correta

senha=input("digite sua senha")
valida_senha_correta='python123'==senha
if valida_senha_correta:
    print("acesso permitido")
else:
    print("acesso negado")

Aprovação

numero=input("digite sua nota:")
numero=float(numero)
valida_aprovado=numero>6.0
valida_reprovado=numero<6.0
if valida_aprovado:
    print("aprovado")
elif valida_reprovado:
    print("reprovado")

Desconto

compra=input("digite o valor da compra: $")
numero=float(numero)
valida_valor_desconto=valor>=100
esconto=valor * 0.10
if valida_valor_desconto:
    print("valor original: $)
elif valida_valor normal:
    print
