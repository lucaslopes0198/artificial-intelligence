import Expansao as exp
import ListaEncadeada as le

class Busca(object):
    caminho = []

    def bidirecional(self, inicio, inicio2):

        visitado1 = []
        visitado2 = []
        caminho2 = []

        self.caminho.clear
        fila = le.ListaDuplamenteEncadeada()
        filac = le.ListaDuplamenteEncadeada()
        fila.insereFim(inicio, None, None)
        filac.insereFim(inicio, None, None)
        visitado1.append(inicio)

        fila2 = le.ListaDuplamenteEncadeada()
        filac2 = le.ListaDuplamenteEncadeada()
        fila2.insereFim(inicio2, None, None)
        filac2.insereFim(inicio2, None, None)
        visitado2.append(inicio2)

        while fila.vazio() is not None and fila2.vazio() is not None:
            atual = fila.removeInicio()
            atual2 = fila2.removeInicio()

            estados = exp.movimento(atual.dado)
            for i in range(len(estados)):
                novo = estados[i]
                flag = True
                for j in range(len(visitado1)):
                    if visitado1[j] == novo:
                        flag = False
                        break
                if flag:
                    fila.insereFim(novo, atual, None)
                    filac.insereFim(novo, atual, None)
                    visitado1.append(novo)
                    if novo in visitado2:
                        while atual2.anterior is not None:
                            atual2 = atual2.anterior
                        while atual2.dado != novo:
                            atual2 = atual2.proximo
                        if atual2.pai is None:
                            caminho2.append(atual.dado)
                        while atual2.pai is not None:
                            atual2 = atual2.pai
                            caminho2.append(atual2.dado)
                        caminho1 = filac.arvore()
                        return "Caminho bidirecional: " + str(list(caminho1[::-1]) + caminho2)

            estados = exp.movimento(atual2.dado)
            for i in range(len(estados)):
                novo = estados[i]
                flag = True
                for j in range(len(visitado2)):
                    if visitado2[j] == novo:
                        flag = False
                        break
                if flag:
                    fila2.insereFim(novo, atual2, None)
                    filac2.insereFim(novo, atual2, None)
                    visitado2.append(novo)
                    if novo in visitado1:
                        while atual.anterior is not None:
                            atual = atual.anterior
                        while atual.proximo is not None and atual.dado != novo:
                            atual = atual.proximo
                        if atual.pai is None:
                            caminho2.append(atual.dado)
                        while atual.pai is not None:
                            atual = atual.pai
                            caminho2.append(atual.dado)
                        caminho1 = filac2.arvore()
                        return "Caminho bidirecional: " + str(list(caminho2[::-1]) + caminho1)
