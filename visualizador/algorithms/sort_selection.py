# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():

    global items, n, i, j, min_idx, fase

    if i==n-1:
        return {"done": True}

    while j<n: ##barrido
        fase="buscar"
        if items[j]<items[min_idx]:
            min_idx=j
            return {"a": min_idx, "b": j, "swap": False, "done": False}
        j+=1
        return {"a": min_idx, "b": j, "swap": False, "done": False}

    if j==n: ##barrido terminado, fase swap
        fase="swap"
        if min_idx!=i:
            a=i
            b=min_idx
            items[i],items[min_idx]=items[min_idx],items[i]
            i+=1
            j=i+1
            min_idx=i
            fase="buscar"
            return {"a": a, "b": b, "swap": True, "done": False}
        else:
            i+=1
            j=i+1
            min_idx=i
            fase="buscar"
            return {"a": i, "b": min_idx, "swap": True, "done": False}