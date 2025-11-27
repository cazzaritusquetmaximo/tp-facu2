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
def step():
#[2,8,5,3,9,4,1]
    global items, n, i, j, min_idx, fase

    # Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    if j<n:
        fase="buscar"
        if items[j]<items[min_idx]:
            min_idx=j
        j+=1
    # Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
        return {"a": min_idx, "b": j, "swap": False, "done": False}

    #   Al terminar el barrido, pasar a fase "swap".
    if j>=n:
        fase="swap"
    # Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
        if min_idx!=i:
            items[?]=items[?], items[?]=items[?]
            return {"a": min_idx, "b": j, "swap": True, "done": False}

    # Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    if "swap"=True:
        i+=1
        j=i+1
        min_idx=i
        fase="buscar"

    # Cuando i llegue al final, devolvé {"done": True}.
    if i>=n-1:
        return {"a": min_idx, "b": j, "swap": False, "done": True}


## si lo ejecuto con el visualizador solo funciona 1 vez, no ordena nada porque hay algo a lo que le estoy errando(creo que =>
## => ademas ordena de atras para adelante), y nunca me deja "recargar" el script, me salta "no se pudo  cargar el .py"