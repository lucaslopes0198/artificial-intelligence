import random as rd
import Expansao as exp
import ListaEncadeadaValorada as lev

class Busca(object):

    caminho = []

    def aEstrela(self, inicio, objetivo):

        valor = (objetivo[0] - inicio[0]) + (objetivo[1] - inicio[1])
        visitado = []

        self.caminho.clear
        fila = lev.ListaDuplamenteEncadeada()
        filac = lev.ListaDuplamenteEncadeada()
        fila.insereFim(inicio, None, 0, valor)
        filac.insereFim(inicio, None, 0, valor)
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
                    custo = rd.randint(3, 10)
                    custo = custo + atual.custo
                    heuristica = (objetivo[0] - novo[0]) + (objetivo[1] - novo[1])
                    valor = custo + heuristica
                    fila.insereFim(novo, atual, custo, valor)
                    filac.insereFim(novo, atual, custo, valor)
                    fila.insereNo(novo, atual, custo, valor)
                    visitado.append(novo)
            if atual.dado == objetivo:
                custoFinal = atual.valor
                caminho = filac.arvore(atual)
                return "Caminho a estrela: " + str(caminho[::-1]) + "\nCusto: " + str(custoFinal)
            fila.removeInicio()
