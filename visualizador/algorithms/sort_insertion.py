# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TO-DO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    #return {"done": True}
    global items, n, i, j

    if i >= n: #Verificacion de si el algoritmo ya termino.
        return {"done": True}

    if j == None: #Fijar cursor sobre el elemento que queremos insertar.
        j=i
        return {"a": i, "b": j, "swap": False, "done": False}

    if j>0: #Si j=0, j-1 seria el último elemento y no queremos comparar eso.
        if items[j-1] > items[j]: #Si el anterior numero es mas grande, hacemos swap.
            items[j-1],items[j]=items[j],items[j-1]
            a=j
            b=j-1
            j=j-1
            return {"a": a, "b": b, "swap": True, "done": False}
        else: #De lo contrario, solo restamos el cursor.
            a=j
            b=j-1
            j=j-1
            return {"a": a, "b": b, "swap": False, "done": False}

    if j<=0: #Una vez que el cursor llegue al final, reiniciamos el cursor y aumentamos el indice.
        i+=1
        j=None
        return {"a": i, "b": j, "swap": False, "done": False}

