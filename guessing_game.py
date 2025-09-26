import random

def jogar_adivinhacoe():

    """
    jogo simples: o computador escolhe um numero entre 1 e 100 e o usuario tenta adivinhar

    """

    print("Adivinhe o numero")
    print("Escolha o nivel de dificuldade: ")
    print("Tente adivinhar o numero entre 1 e 36")
    print("1 - Facil(1 a 12) -> 10 tentativas")
    print("2 - Medio(1 a 24) -> 7 tentativas")
    print("3 - Dificil(1 a 36) -> 5 tentativas")

# Definindo fases

    while True:
        level = input("Digite 1, 2 ou 3: ")
        if level == "1":
            secret_number = random.randint(1, 12)
            attempts_max = 10
            break
        elif level == "2":
            secret_number = random.randint(1, 24)
            attempts_max = 7
            break
        elif level == "3":
            secret_number = random.randint(1, 36)
            attempts_max = 5
            break
        else:
            print("Opcao invalida. Tente novamente")

    attempts = 0
    print("Tente adivinhar o numero!")


    while attempts < attempts_max:
        kick = input(f"Seu palpite(tentativa{attempts+1}/{attempts_max}): ")
        attempts += 1

        # validacao de entrada - Garante que o usuario digite um valor inteiro

        try:
            kick_int = int(kick)
        except ValueError:
            print("Por Favor digite um numero inteiro(ex.: 420),")
            continue

        # checagens

        if kick_int < secret_number:
            print("Muito baixo, tente um numero maior")

        elif kick_int > secret_number:
            print("Muito alto, tente um numero menor")

        else:
            print(f"Acertou! o numero era {secret_number}")
            print(f"Numero de tentativas: {attempts}")
            break
    
    else:
        
        # roda caso jogador tente o numero maximo de tentativas

        print("💀 Suas tentativas acabaram!")
        print(f"O numero secreto era: {secret_number}")


if __name__ == "__main__":
    jogar_adivinhacoe()
