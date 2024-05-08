class Bank_account:
  def __init__(self, balance = 0):
    self.__balance = balance
    self.__file = "project/files/transactios.txt"

  def deposit(self, amount):
    self.__balance += amount
    
    try:
      with open(self.__file, "a") as file:
        file.write(f"deposito (+), {amount}\n")
    except:
      print("Algo deu errado em abrir o arquivo!")
      pass

    print(f"Depósito de R${amount} realizado!")

  def saque(self, amount):
      self.__balance -= amount
      
      try:
        with open(self.__file, "a") as file:
          file.write(f"saque (-), {amount}\n")
      except:
        print("Algo deu errado em abrir o arquivo!")
        pass

      print(f"Saque de R${amount} realizado!")

account = Bank_account()
waiting_menu = False #flag
while True:
    if waiting_menu == True:
      input("\nPressione Enter para voltar...")

    # print("\033c", end="") # terminal clear
    print("\033[H\033[J") # terminal clear
    waiting_menu = True

    print('''
=== Automated Teller Machine ===
    [1] Ver saldo
    [2] Ver extrato
    [3] Fazer o depósito
    [4] Fazer saque
    [5] Sair
================================
''')

    option = input("\bEscolha uma opção: ")
    print("")

    print(option)

    if option == "1":
      print("saldo")
    elif option == "2":
      print("extrato")
    elif option == "3":
      amount = float(input("Digite o valor do depósito "))
      account.deposit(amount)
    elif option == "4":
      amount = float(input("Digite o valor do saque "))
      account.saque(amount)
    elif option == "5":
      print("programa encerrado!\n")
      break
    else:
      print("Opção inválida!")