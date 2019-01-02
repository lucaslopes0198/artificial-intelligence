import Expansao as exp
import ListaEncadeada as le

class Busca(object):
    caminho = []

    def amplitude(self, inicio, objetivo):

        visitado = []

        self.caminho.clear
        fila = le.ListaDuplamenteEncadeada()
        filac = le.ListaDuplamenteEncadeada()
        fila.insereFim(inicio, None, None)
        filac.insereFim(inicio, None, None)
        visitado.append(inicio)

        while fila.vazio() is not None:
            atual = fila.removeInicio()

            estados = exp.movimento(atual.dado)
            for i in range(len(estados)):
                novo = estados[i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j] == novo:
                        flag = False
                        break
                if flag:
                    fila.insereFim(novo, atual, None)
                    filac.insereFim(novo, atual, None)
                    visitado.append(novo)
                    if novo == objetivo:
                        caminho = filac.arvore()
                        return "Caminho amplitude: " + str(caminho[::-1])
