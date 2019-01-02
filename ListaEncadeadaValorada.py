class No:
    def __init__(self, dado, anterior, proximo, pai, custo, valor):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo
        self.pai = pai
        self.custo = custo
        self.valor = valor


class ListaDuplamenteEncadeada(object):

    head = None
    tail = None

    def insereNo(self, dado, pai, custo, valor):

        no = No(dado, None, None, pai, custo, valor)
        atual = self.head

        while atual.valor < valor:
            atual = atual.proximo
        if atual.anterior is not None:
            ant = atual.anterior
            ant.proximo = no
            no.anterior = ant
            no.proximo = atual
            atual.anterior = no

    def insereNoGreedy(self, dado, pai, custo, valor):

        no = No(dado, None, None, pai, custo, valor)
        atual = self.head

        while atual.valor > valor:
            atual = atual.proximo
        if atual.anterior is not None:
            ant = atual.anterior
            ant.proximo = no
            no.anterior = ant
            no.proximo = atual
            atual.anterior = no

    def insereFim(self, dado, pai, custo, valor):

        no = No(dado, None, None, pai, custo, valor)

        if self.head is None:
            self.head = no
            self.tail = no
        else:
            self.tail.proximo = no
            no.anterior = self.tail
            self.tail = no

    def removeInicio(self):

        no_atual = None

        if self.head is not None:
            no_atual = self.head
            if no_atual.proximo is not None:
                self.head = self.head.proximo
            else:
                self.head = self.tail = None
        return no_atual

    def vazio(self):

        if self.head is None:
            return True
        else:
            return False

    def mostrar(self):

        print("Lista Duplamente Encadeada:")
        no_atual = self.head
        no = ""

        while no_atual is not None:
            no += " | " + str(no_atual.dado) + str(no_atual.pai) + " | "
            no_atual = no_atual.proximo

        print(no)

    def arvore(self, No):

        no_atual = No
        no = []

        while no_atual.pai is not None:
            no.append(no_atual.dado)
            no_atual = no_atual.pai
        no.append(no_atual.dado)
        return no
