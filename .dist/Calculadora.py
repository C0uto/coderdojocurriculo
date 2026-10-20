def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    return a / b
def mostrar_menu():
    print("\n--- Calculadora Dojo 3000 ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
while True:
    mostrar_menu()
    opcao = input("\nEscolhe uma opção: ")
    if opcao == "0":
        print("\nAté à próxima, ninja!")
        break
    x = float(input("\nPrimeiro número: "))
    y = float(input("\nSegundo número: "))
    if opcao == "1":
        print("\nResultado:", somar(x, y))
    elif opcao == "2":
        print("\nResultado:", subtrair(x, y))
    elif opcao == "3":
        print("\nResultado:", multiplicar(x, y))
    elif opcao == "4":
        print("\nResultado:", dividir(x, y))
    else:
        print("\nOpção inválida!")