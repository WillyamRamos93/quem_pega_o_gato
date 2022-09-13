

def verifica_positivo(nome):
    while True:
        numero = input(f"Digite a posicao inicial do {nome}: ")
        valor = int(numero)
        if valor < 0:
            print("Voce precisa digitar um numero positivo, tente novamente")
            continue
        break

    return valor


def armazena_posicao():
    for i in posicao:
        posicao[i] = verifica_positivo(i)

    return posicao


def calcula(cat, dog):
    if cat > dog:
       resultado = cat - dog
    elif cat < dog:
        resultado = dog - cat
    else:
        resultado = cat

    return resultado


def teste(rex, bob, oli):

    calcula_rex = calcula(rex, oli)
    calcula_bob = calcula(bob, oli)

    if calcula_rex < calcula_bob:
        nome = "Rex"
    elif calcula_rex > calcula_bob:
        nome = "Bob"
    else:
        nome = "Oli"

    return nome


# ============== Main ==============

posicao = dict.fromkeys(["Rex", "Bob", "Oli"])

armazena_posicao()
vencedor = teste(posicao["Rex"], posicao["Bob"], posicao["Oli"])
if vencedor == "Oli":
    print("O gato fugiu enquanto os cachorros brigavam!")
else:
    print(f"O {vencedor} pegou o gato!")

