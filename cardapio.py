opcao = 0
while opcao !=5:
    print ("Cardápio")
    print ("1- Hambúrguer")
    print ("2- Pizza")
    print ("1- Salada")
    print ("4- Refrigerante")
    print ("5- Sair")
    opcao = int(input("Escolha sua opção: "))
    if opcao ==1:
        print ("Você escolheu Hambúrguer.")
    elif opcao ==2:
        print ("Você escolheu pizza.")
    elif opcao ==3:
        print ("Você escolheu salada.")
    elif opcao ==4:
        print ("Você escolheu refrigerante.")
    elif opcao ==5:
        print ("Saindo do cardápio...")
        break
    else:
        print ("Opção inválida. Tente novamente")        
    
    