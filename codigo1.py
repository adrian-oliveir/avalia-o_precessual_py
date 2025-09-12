from collections import Counter

def analisar_texto():
    texto = input("Digite um texto: ")

    palavras = texto.split()

    num_palavras = len(palavras)
    print(f"Total de palavras: {num_palavras}")

    palavra_mais_longa = max(palavras, key=len)
    print(f"A palavra mais longa é: {palavra_mais_longa}")

    contador_palavras = Counter(palavras)
    palavra_mais_frequente = contador_palavras.most_common(1)[0]
    print(f"A palavra que mais aparece é: '{palavra_mais_frequente[0]}' com {palavra_mais_frequente[1]} ocorrências.")

if __name__ == "__main__":
    analisar_texto()
