comprimento = 12
largura = 14
altura = 20

def calcular_volume(comprimento, largura, altura):
    """Calcula o volume de um paralelepípedo."""
    return comprimento * largura * altura

if __name__ == "__main__":
    volume = calcular_volume(comprimento, largura, altura)
    print(f"O volume do paralelepípedo é: {volume} m³")