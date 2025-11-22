# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

#items[5,4,2,1,3] , len(5)
def step(j):

    if items[j] > items[j+1]:
    items[j],items[j+1]=items[j+1],items[j]

    return {"done": True}





def step():
    # TO-DO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.
"""
    for i in range (len(items)):
        for j in range (len(items)-1):
            if items[j] > items[j+1]:
                #swap entre (lista[j], lista[j+1])
                #swap=True?
                items[j],items[j+1]=items[j+1],items[j]
"""

    return {"done": True}

