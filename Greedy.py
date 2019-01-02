import random as rd
import Expansao as exp
import ListaEncadeadaValorada as lev

class Busca(object):
    caminho = []

    def greedy(self, inicio, objetivo):
        heuristica = (objetivo[0] - inicio[0]) + (objetivo[1] - inicio[1])
        visitado = []

        self.caminho.clear
        fila = lev.ListaDuplamenteEncadeada()
        filac = lev.ListaDuplamenteEncadeada()
        fila.insereFim(inicio, None, 0, heuristica)
        filac.insereFim(inicio, None, 0, heuristica)
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
                    heuristica = (objetivo[0] - novo[0]) + \
                        (objetivo[1] - novo[1])
                    if heuristica < atual.valor:
                        fila.insereFim(novo, atual, 0, heuristica)
                        filac.insereFim(novo, atual, 0, heuristica)
                        fila.insereNoGreedy(novo, atual, 0, heuristica)
                        visitado.append(novo)
                    if novo == objetivo:
                        caminho = filac.arvore(filac.tail)
                        tail = filac.tail
                        heuristicaFinal = 0
                        while tail.pai is not None:
                            heuristicaFinal = heuristicaFinal + tail.valor
                            tail = tail.pai
                        return "Caminho greedy: " + str(caminho[::-1]) + "\nheuristica: " + str(heuristicaFinal)
            fila.removeInicio()
