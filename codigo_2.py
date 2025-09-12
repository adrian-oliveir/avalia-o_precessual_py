def main():
    
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    print("\nLista original:")
    print(numeros)

    numeros_ordenados = sorted(numeros)
    print("\nLista ordenada em ordem crescente:")
    print(numeros_ordenados)

    numeros_unicos = list(set(numeros))
    print("\nLista sem números repetidos:")
    print(numeros_unicos)

if __name__ == "__main__":
    main()
