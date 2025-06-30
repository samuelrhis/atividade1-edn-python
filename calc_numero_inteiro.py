def calcular_diferenca(a, b, c, d):
    return (a * b) - (c * d)

if __name__ == "__main__":
    v1 = int(input("Digite o primeiro valor:"))
    v2 = int(input("Digite o segundo valor:"))
    v3 = int(input("Digite o terceiro valor:"))
    v4 = int(input("Digite o quarto valor:"))

    resultado = calcular_diferenca(v1, v2, v3, v4)

    print(f"DIFERENCA = {resultado}")