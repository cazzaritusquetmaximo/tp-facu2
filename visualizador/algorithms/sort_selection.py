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
"""
def step():
    # TO-DO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}
"""
#02:04am, 27nov
def step():

    if items[j]<items[min_idx]: ##compara el item delantero a "i"
        fase="buscar" ##no se si va aca
        min_idx=items[j]    ##le da valor nuevo actualizado al indice minimo del barrido
        return {"a": min_idx, "b": j+1, "swap": False, "done": False} ## => actualizar "j_actual" seria j+1?

    ##el barrido termina cuando hizo [i:n-1] vueltas pero como corno se le indico???

    ##fase swap
    if min_idx!=i:
        fase="swap"
        items[j]=items[i], items[i]=items[min_idx]
        return {"a": min_idx, "b": j, "swap": True, "done": False} ## => solo cambie swap=True

    i+=1, fase="buscar", j=i+1
    if >=len(items):
        return {"done": True}
