import Expansao as exp
import ListaEncadeada as le

class Busca(object):
    caminho = []

    def profundidadeIterativa(self, inicio, objetivo, limite):

        visitado = []

        self.caminho.clear
        pilha = le.ListaDuplamenteEncadeada()
        pilhac = le.ListaDuplamenteEncadeada()
        pilha.insereFim(inicio, None, 0)
        pilhac.insereFim(inicio, None, 0)
        visitado.append(inicio)
        while pilha.vazio() is not None:
            atual = pilha.removeFim()
            if atual == False:
                limite += 2
                print("Caminho não encontrado.\nPróximo limite: ", limite)
                break
            niv = atual.nivel + 1
            if niv < limite:
                estados = exp.movimento(atual.dado)
                for i in range(len(estados)-1, -1, -1):
                    novo = estados[i]
                    flag = True
                    if novo in visitado and novo != [0, 0]:
                        ind = visitado.index(novo)
                        head = pilhac.head
                        while head.dado != novo:
                            head = head.proximo
                        if niv < head.nivel:
                            visitado.pop(ind)
                    for j in range(len(visitado)):
                        if visitado[j] == novo:
                            flag = False
                            break
                    if flag:
                        pilha.insereFim(novo, atual, niv)
                        pilhac.insereFim(novo, atual, niv)
                        visitado.append(novo)
                        if novo == objetivo:
                            caminho = pilhac.arvore()
                            return "Caminho profundidade limitada: " + str(caminho[::-1])
