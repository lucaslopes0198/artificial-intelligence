class No:
    def __init__(self, dado, anterior, proximo, pai, nivel):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo
        self.pai = pai
        self.nivel = nivel

class ListaDuplamenteEncadeada(object):

    head = None
    tail = None

    def insereInicio(self, dado, pai, nivel):

        no = No(dado, None, None, pai, nivel)

        if self.head is None:
            self.head = no
            self.tail = no
        else:
            no.proximo = self.head
            self.head.anterior = no
            self.head = no

    def insereFim(self, dado, pai, nivel):

        no = No(dado, None, None, pai, nivel)

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

    def removeFim(self):

        if self.head is not None:
            no_atual = self.tail
            if no_atual.anterior is not None:
                self.tail = self.tail.anterior
                self.tail.proximo = None
            else:
                self.head = self.tail = None
        else:
            return False
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

    def arvore(self):

        no_atual = self.tail
        no = []

        while no_atual.pai is not None:
            no.append(no_atual.dado)
            no_atual = no_atual.pai

        no.append(no_atual.dado)

        return no
