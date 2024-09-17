class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            return "A pilha está vazia."
        return self.itens.pop()

    def topo(self):
        if self.esta_vazia():
            return "A pilha está vazia."
        return self.itens[-1]

    def tamanho(self):
        return len(self.itens)


# Uso
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print("Topo:", pilha.topo()) 
print("Desempilhado:", pilha.desempilhar())  
print("Tamanho:", pilha.tamanho())
