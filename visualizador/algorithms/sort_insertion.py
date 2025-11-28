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
    ## TO-DO:
    ## - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    #return {"done": True}

    # Si i >= n: devolver {"done": True}.
    if i >= n:
        return {"a": a, "b": b, "swap": False, "done": True}

    # Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    if j==None:
        j=i
        return {"a": a, "b": b, "swap": False, "done": False}

    # Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    while j > 0 and items[j-1] > items[j]:
        items[j-1],items[j]=items[j],items[j-1]
        {"a": a, "b": b, "swap": True, "done": False}

    # Si ya no hay que desplazar: avanzar i y setear j=None.
    if j<=0:
        i+=1
        j=None
    ##deberia devolver algo?

