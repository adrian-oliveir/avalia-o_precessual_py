import random

def gerar_senha():
    nome = input("Digite seu nome: ")

    letras = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*?<>"

    todos = letras + maiusculas + numeros + simbolos

    senha = ""  

    qtd_inicio = 10 - (len(nome) // 2)
    for i in range(qtd_inicio):
        escolhido = random.choice(todos)
        senha += escolhido

    senha += nome

    while len(senha) < 20:
        escolhido = random.choice(todos)
        senha += escolhido

    print("\nSenha gerada:")
    print(senha)


if __name__ == "__main__":
    gerar_senha()
