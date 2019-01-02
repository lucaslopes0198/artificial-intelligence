import random as rd
import Expansao as exp
import ListaEncadeadaValorada as lev

class Busca(object):
    caminho = []

    def custoUniforme(self, inicio, objetivo):

        visitado = []

        self.caminho.clear
        fila = lev.ListaDuplamenteEncadeada()
        filac = lev.ListaDuplamenteEncadeada()
        fila.insereFim(inicio, None, 0, 0)
        filac.insereFim(inicio, None, 0, 0)
        visitado.append(inicio)

        while fila.vazio() is not None:
            atual = fila.head

            estados = exp.movimento(atual.dado)
            for i in range(len(estados)):
                novo = estados[i]
                flag = True
                for j in range(len(visitado)):
                    if visitado[j] == novo:
                        flag = False
                        break
                if flag:
                    custo = rd.randint(5,15)
                    custo = custo + atual.custo
                    fila.insereFim(novo, atual, custo, custo)
                    filac.insereFim(novo, atual, custo, custo)
                    fila.insereNo(novo, atual, custo, custo)
                    visitado.append(novo)
                    if novo == objetivo:
                        caminho = filac.arvore(filac.tail)
                        custoFinal = filac.tail
                        custoFinal = custoFinal.custo
                        return "Caminho custo uniforme: " + str(caminho[::-1]) + "\nCusto: " + str(custoFinal)
            fila.removeInicio()
