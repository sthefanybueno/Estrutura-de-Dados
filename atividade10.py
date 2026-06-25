def two_sum(numeros, alvo):
    # mapeia cada valor ao seu índice em `numeros`
    mapa = {}  

    for i, valor_atual in enumerate(numeros):
        comp = alvo - valor_atual
        if comp in mapa:
            return [mapa[comp], i]
        mapa[valor_atual] = i
       

if __name__ == "__main__":
    numeros = [2, 7, 11, 15]
    alvo = int(input("Digite o valor alvo: \n>>"))
    resultado = two_sum(numeros, alvo)
    print(resultado)  # saída esperada: [0, 1] 