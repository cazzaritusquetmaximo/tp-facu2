# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = [] #Lista de barras 4 5 1 3 2
n = 0 #Longitud de la lista
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    #Ejemplo Longitud 5
    for i in range (len(items)): # 0 - 4
        for j in range (len(items)-1): # 0 - 3
            if items[j] > items[j+1]:
                #swap entre (lista[j], lista[j+1])
                #swap=True?
                items[j],items[j+1]=items[j+1],items[j]
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.

    return {"done": True}