import ProfundidadeLimitada as pl
import ProfundidadeIterativa as pi
import Amplitude as amp
import Profundidade as pro
import Bidirecional as bid
import CustoUniforme as ctu
import Greedy as gdy
import aEstrela as est

def validPos(ini, fim):
    if len(ini) != 2 or ini[0] > 8 or ini[1] > 8:
        print("Informe 2 números de 0 a 8 separados por espaço.")
        quit()
    if len(fim) != 2 or fim[0] > 8 or fim[1] > 8:
        print("Informe 2 números de 0 a 8 separados por espaço.")
        quit()

ini = [int(x) for x in input("Inicio: ").split()]
fim = [int(x) for x in input("Fim: ").split()]

validPos(ini, fim)

escolha = 0
while True:
    escolha = input("Escolha o algoritmo:\n1 - Amplitude\n2 - Bidirecional\n3 - Profundidade\n4 - Profundidade Limitada\n5 - Profundidade Iterativa\n6 - Custo Uniforme\n7 - Greedy\n8 - A*\n0 - Sair\n")

    if escolha == "0":
        break

    if escolha == "1":
        sol = amp.Busca()
        s = sol.amplitude(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "2":
        sol = bid.Busca()
        s = sol.bidirecional(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "3":
        sol = pro.Busca()
        s = sol.profundidade(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "4":
        sol = pl.Busca()
        s = sol.profundidadeLimitada(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "5":
        limite = int(input("Informe o limite inicial: "))
        sol = pi.Busca()
        s = None
        while s is None:
            s = sol.profundidadeIterativa(ini, fim, limite)
            limite += 2
        print("\n" + s + "\n")

    elif escolha == "6":
        sol = ctu.Busca()
        s = sol.custoUniforme(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "7":
        sol = gdy.Busca()
        s = sol.greedy(ini, fim)
        print("\n" + s + "\n")

    elif escolha == "8":
        sol = est.Busca()
        s = sol.aEstrela(ini, fim)
        print("\n" + s + "\n")
