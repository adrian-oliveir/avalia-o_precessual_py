def main():
    numeros = []

    for i in range(10):
        n = int(input("Digite o " + str(i+1) + "º número: "))
        numeros.append(n)

    print("\nLista original:")
    print(numeros)

    lista_ordenada = numeros[:] 
    for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada)-1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                temp = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j+1] = temp

    print("\nLista em ordem crescente:")
    print(lista_ordenada)

    unicos = []
    for n in numeros:
        if n not in unicos:
            unicos.append(n)

    print("\nLista sem números repetidos:")
    print(unicos)


if __name__ == "__main__":
    main()

