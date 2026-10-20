import random

def introducao():
    print("\nHá muitos anos, um rei escondeu o seu maior tesouro")
    print("num castelo no alto da montanha. 🏰")
    print("\nDizem que o castelo está abandonado, mas que um")
    print("dragão guarda a porta do tesouro. 🐉")
    print("\nSó quem encontrar a chave dourada conseguirá entrar...")
    print("\nA tua missão, ninja, é encontrar o tesouro!")
    input("\nPrime ENTER para começar a aventura... ")

def sala_entrada(tem_chave):
    print("\nEstás à entrada do castelo abandonado.")
    print("1 - Explorar o jardim")
    print("2 - Entrar no castelo")
    print("3 - Explorar o lago")
    escolha = input("O que fazes? ")
    if escolha == "1":
        jardim(tem_chave)
    elif escolha == "2":
        castelo(tem_chave)
    elif escolha == "3":
        lago(tem_chave)
    else:
        print("Não percebi...")
        sala_entrada(tem_chave)

def jardim(tem_chave):
    print("\nO jardim está cheio de ervas daninhas, mas algo te chama a atenção.")
    print("1 - Levantar uma pedra grande")
    print("2 - Entrar no labirinto de sebes")
    print("3 - Provar os frutos de uma árvore")
    print("4 - Voltar à entrada")
    escolha = input("O que fazes? ")
    if escolha == "1":
        if tem_chave:
            print("\nJá apanhaste a chave. Debaixo da pedra só há minhocas.")
        else:
            print("\nEncontras uma chave dourada debaixo da pedra! 🔑")
            tem_chave = True
        jardim(tem_chave)
    elif escolha == "2":
        labirinto(tem_chave)
    elif escolha == "3":
        print("\nOs frutos são deliciosos! Ganhas energia, mas nada mais acontece.")
        jardim(tem_chave)
    elif escolha == "4":
        sala_entrada(tem_chave)
    else:
        print("Não percebi...")
        jardim(tem_chave)

def labirinto(tem_chave):
    print("\nEntras no labirinto de sebes. Os caminhos parecem todos iguais...")
    caminho_certo = random.choice(["1", "2", "3"])
    tentativas = 0
    while tentativas < 4:
        print("\nEstás numa encruzilhada.")
        print("1 - Seguir pela esquerda")
        print("2 - Seguir em frente")
        print("3 - Seguir pela direita")
        escolha = input("Que caminho segues? ")
        if escolha == caminho_certo:
            print("\nEncontras finalmente a saída do labirinto! 🌿")
            jardim(tem_chave)
            return
        elif escolha in ["1", "2", "3"]:
            tentativas = tentativas + 1
            print("\nAndas às voltas e voltas ao mesmo sítio... 🔄")
        else:
            print("Não percebi...")
    print("\nA noite chega e com ela um lobo faminto encontra-te. 🐺")
    fim_do_jogo(False)

def lago(tem_chave):
    print("\nAo chegar ao lago vês algo a brilhar no centro do mesmo, é uma espada cravada numa rocha.")
    print("\nUma espada daria jeito para enfrentar o dragão que protege o tesouro.")
    print("\nComo chegas à espada:")
    print("1 - A nado")
    print("2 - Num barco a remo")
    print("3 - Voltas trás")
    escolha = input("O que fazes? ")
    if escolha == "1":
        print("Das profundezas do lago surge um monstro marinho que acaba por comer-te.")
        fim_do_jogo(False)
    elif escolha == "2":
        print("Das profundezas do lago surge um monstro marinho que acaba por destruir o teu barco e comer-te.")
        fim_do_jogo(False)
    elif escolha == "3":
        sala_entrada(tem_chave)
    else:
        print("Não percebi...")
        lago(tem_chave)

def castelo(tem_chave):
    print("\nChegas a uma porta enorme com uma fechadura.")
    print("1 - Tentar abrir a porta")
    print("2 - Bater à porta")
    print("3 - Espreitar por uma janela")
    print("4 - Voltar à entrada")
    escolha = input("O que fazes? ")
    if escolha == "1":
        if tem_chave:
            print("\nA chave encaixa na fechadura!")
            fim_do_jogo(True)
        else:
            print("\nA porta está trancada e o barulho acorda o dragão! 🐉")
            fim_do_jogo(False)
    elif escolha == "2":
        print("\nUma voz de trovão ecoa lá dentro e o dragão abre a porta... e devora-te! 🐉")
        fim_do_jogo(False)
    elif escolha == "3":
        print("\nVês o dragão a dormir sobre uma montanha de ouro. Tens de ser silencioso...")
        castelo(tem_chave)
    elif escolha == "4":
        sala_entrada(tem_chave)
    else:
        print("Não percebi...")
        castelo(tem_chave)

def fim_do_jogo(vitoria):
    if vitoria:
        print("🏆 Encontraste o tesouro! Ganhaste!")
    else:
        print("💀 Perdeste... Tenta outra vez!")

print("=== A Aventura do Castelo ===")
introducao()
sala_entrada(False)
