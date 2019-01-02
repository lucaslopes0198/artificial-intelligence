import Expansao as exp
import ListaEncadeada as le

class Busca(object):
    caminho = []

    def profundidade(self, inicio, objetivo):

        visitado = []

        self.caminho.clear
        pilha = le.ListaDuplamenteEncadeada()
        pilhac = le.ListaDuplamenteEncadeada()
        pilha.insereFim(inicio, None, None)
        pilhac.insereFim(inicio, None, None)
        visitado.append(inicio)

        while pilha.vazio() is not None:
            atual = pilha.removeFim()

            estados = exp.movimento(atual.dado)
            for i in range(len(estados)-1, -1, -1):
                novo = estados[i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j] == novo:
                        flag = False
                        break
                if flag:
                    pilha.insereFim(novo, atual, None)
                    pilhac.insereFim(novo, atual, None)
                    visitado.append(novo)
                    if novo == objetivo:
                        caminho = pilhac.arvore()
                        return "Caminho profundidade: " + str(caminho[::-1])
