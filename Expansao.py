def movimento(estado_atual):
    estados = []

    estado1 = [estado_atual[0]-1, estado_atual[1]-2]
    estados.append(validaEstado(estado1))
    estado2 = [estado_atual[0]-2, estado_atual[1]-1]
    estados.append(validaEstado(estado2))

    estado3 = [estado_atual[0]+1, estado_atual[1]-2]
    estados.append(validaEstado(estado3))
    estado4 = [estado_atual[0]+2, estado_atual[1]-1]
    estados.append(validaEstado(estado4))

    estado5 = [estado_atual[0]+1, estado_atual[1]+2]
    estados.append(validaEstado(estado5))
    estado6 = [estado_atual[0]+2, estado_atual[1]+1]
    estados.append(validaEstado(estado6))

    estado7 = [estado_atual[0]-1, estado_atual[1]+2]
    estados.append(validaEstado(estado7))
    estado8 = [estado_atual[0]-2, estado_atual[1]+1]
    estados.append(validaEstado(estado8))

    return list(filter(None.__ne__, estados))

def validaEstado(estado):
    if estado[0] >= 0 and estado[0] < 8 and estado[1] >= 0 and estado[1] < 8:
        if estado is not None:    
            return estado
