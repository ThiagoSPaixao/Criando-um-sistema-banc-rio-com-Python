cliente = "Thiago Souza da Paixão"
saldo = 1000
possui_cheque_especial = True
cheque_especial = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
menu_saida = ""

menu = f"""
☁️☁️☁️  Olá {cliente}, Seja bem vindo :) 

        ☁️⛅ Núvem Bank☀️☁️
                    Onde seu dinheiro voa alto...
                                                                                    
[1] ☁️   Saldo
[2] ⛅  Saque
[3] 🌤️   Depósito
[4] ☁️   Extrato
[5] ⛅  Investimentos
[6] 🌤️   SAC
[7] ☁️   Sair

Selecione a opção desejada:
""" 

while  True:

    opcao = int(input(menu))

    if opcao == 1:
        print("O seu saldo atual é: ", saldo)
        print("Seu saldo em cheque especial é: ", cheque_especial)
        opcao_saldo = int(input("Posso te ajudar em algo mais? \n[1] Sim, por favor \n[2] Não, obrigado(a) \n"))

        if opcao_saldo == 1:
            print("Retorando ao menu anterior")     
        else:
            print("Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
            break

    elif opcao == 2:

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print ("Limite de saque diário excedido. obrigado :)")
            break

        valor_saque = float(input("Quanto você deseja sacar?: "))

        if valor_saque > saldo:
            print("Saldo insuficiente :( ")

            if possui_cheque_especial == True:
                    opcao_cheque_especial = int(input(f"Mas não fica triste. você tem R${cheque_especial} no seu cheque especial. deseja contratá-lo? \n[1] Sim \n[2] Não \n"))

                    if opcao_cheque_especial == 1:
                        print("⚠️  Atenção!!! O uso do cheque especial está sujeito a juros altos. Recomendamos utilizar essa opção com cautela e verificar o saldo disponível regularmente para evitar endividamento. ⚠️ ")
                        valor_cheque_especial = float(input("Quanto você deseja sacar? "))

                        while valor_cheque_especial > cheque_especial:
                            print(f"Você não possui este valor no seu cheque especial, por favor, escolha um valor entre R$ 0,01 e R${cheque_especial}")
                            valor_cheque_especial = float(input("Quanto você deseja sacar? "))
                            
                        else:
                            saldo += valor_cheque_especial
                            #saldo = saldo + valor_cheque_especial
                            cheque_especial -= valor_cheque_especial
                            #cheque_especial = cheque_especial + valor_cheque_especial 
                            print(f"Seu Saldo atual é R${saldo} Reais")

                            opcao_saida_cheque_especial = int(input("Deseja algo mais? \n [1] Retornar ao menu principal \n [2] Sair \n "))

                            if opcao_saida_cheque_especial == 1:
                                print("Retornando ao menu principal...")

                            else:
                                menu_saida = f"""
 😄 Obrigado por utilizar nossos serviços!  Fica ligadinho(a), você tem até 7 dias para repor o valor do cheque especial. 
 qualquer dúvida, entra em contato com a gente! 👍🏼 
                                
                     ☁️⛅ Núvem Bank☀️☁️
                                 Onde seu dinheiro voa alto...
                            """
                            print(menu_saida)
                            break

                    
                    else:
                        opcao_nao_cheque_especial = int(input("Tudo bem! o que você deseja fazer então: \n[1] Voltar ao menu principal \n[2] Dizer tchau \n"))
                        
                        if opcao_nao_cheque_especial == 1:
                            print("Voltando ao menu pincipal...")

                        else:                     
                            print("tudo bem, tchau então :) Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
                            break

            else:
                opcao_saldo_insuficiente = int(input("Posso te ajudar em algo mais? \n[1] Sim \n[2] Não \n "))

                if opcao_saldo_insuficiente == 2:
                     print("Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
                     break
                
        else:
            saldo -= valor_saque
            #saldo = saldo - valor_saque
            print(f"Saque realizado com sucesso, seu saldo atual é: R${saldo:.2f}")

            extrato += f"Saque: R$ {valor_saque:.2f}\n"

            numero_saques += 1

            opcao_saida_saque = int(input("Posso te ajudar em algo mais? \n [1] Sim, Realizar outra operação. \n [2] Não, obrigado(a), já terminei por aqui.\n"))

            if opcao_saida_saque == 2:
                print("Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
                break
    
    elif opcao == 3:
        valor_deposito = float(input("Quanto você irá depositar? "))

        if valor_deposito > 0:
            saldo += valor_deposito
            #saldo = saldo + valor_deposito
            print(f"Depósito realizado com sucesso, seu saldo atual é: R${saldo:.2f}")
            
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

            opcao_saida_deposito = int(input("Posso te ajudar em algo mais? \n [1] Sim, Realizar outra operação. \n [2] Não, obrigado(a), já terminei por aqui.\n"))

            if opcao_saida_deposito == 2:
                print("Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
                break

    elif opcao == 4:
        print("\n====================EXTRATO======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == 5:
        print("Tá pronto pra ver o seu dinheiro voando alto?! Em breve teremos novidades...")

    elif opcao == 6:
        print("Dúvidas, reclamações e sujestões, entra em contato com a nossa central de atendimento: (81) 99999-9999")
        print("      ☁️⛅ Núvem Bank☀️☁️ \n             Onde seu dinheiro voa alto...")

    elif opcao == 7:
        print("Obrigado por utilizar os nossos serviços. a Núvem Bank agradece.☁️🌤️")
        break

    else:
        print("Por favor, selecione uma opção válida.")