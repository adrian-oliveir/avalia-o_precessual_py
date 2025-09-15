def analisar_texto():
    texto = input("Digite um texto: ")

    palavras = texto.split()

    total = len(palavras)
    print("Total de palavras:", total)

    maior = ""
    for p in palavras:
        if len(p) > len(maior):
            maior = p
    print("A palavra mais longa é:", maior)

    contagem = {}
    for p in palavras:
        if p in contagem:
            contagem[p] += 1
        else:
            contagem[p] = 1

    mais_freq = None
    vezes = 0
    for p, qtd in contagem.items():
        if qtd > vezes:
            vezes = qtd
            mais_freq = p

    print(f"A palavra que mais aparece é: '{mais_freq}' com {vezes} ocorrências.")


if __name__ == "__main__":
    analisar_texto()
