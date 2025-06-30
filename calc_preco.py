nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

def calcular_preco_total(preco_unitario, quantidade):
    """Calcula o preço total de um produto."""
    return preco_unitario * quantidade

if __name__ == "__main__":
    preco_total = calcular_preco_total(preco_unitario, quantidade)
    print(f"O preço total do produto '{nome_do_produto}' é: R$ {preco_total:.2f}") 
