opcao = -1
while opcao != 0:
  print("===Calculadora===")
  print("1- soma")
  print ("2- subtrair")
  print ("3- multiplicacao")
  print ("4- dividir")
  print ("0 fecha a calculadora")
  opcao = int(input("Digite a opção escolhida:"))
  if opcao >=1 and opcao <=4:
       numero1 = int(input("Digite o primeiro numero:"))
       numero2 = int(input("Digite o segundo numero:"))
  if opcao ==1:  
      print("voce escolheu soma:")   
      resultado = numero1 + numero2
      print (f"O resultado da sua soma é:{resultado}")
  elif opcao ==2:
      print("voce escolheu subtraçao: ")
      resultado = numero1 - numero2
      print(f"o resultado da sua subtração é:{resultado}")
  elif opcao ==3:
      print("voce escolheu multiplicação:")
      resultado = numero1 * numero2
      print(f"o resultado da sua multiplicação é:{resultado}")
  elif opcao ==4:
      print("voce escolheu divisao:")
      resultado = numero1 / numero2
      print(f"o resultado da sua divisão é:{resultado}")
      break 
  else:
      print ("Opção invalida")
      

