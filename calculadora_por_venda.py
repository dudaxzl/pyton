nome = (input("digite seu nome: "))
salario_fixo = int (input("digite seu salario fixo:"))
vendas = int (input ("digite seu numero de vendas:"))
if vendas>=20:
    vendas = salario_fixo*0.15
    salario_fixo = salario_fixo + vendas
    print (f"parabéns seu salário desse mês sera de:{salario_fixo:}")
else:
    print (F"Voce nao alcançou sua meta seu salario sera de:{salario_fixo:}")

