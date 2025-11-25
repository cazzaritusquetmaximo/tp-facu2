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


def step():
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    # Cuando no queden pasos, devolvé {"done": True}.

    global n,i,j #Necesitamos trabajar con las variables globales

    if i == n-1: #Primero verificamos si ya se realizaron todas las vueltas. Si no es el caso, se sigue ordenando.
        return {"done": True}
    
    if j+1 == n-i: #Comparamos si ya se llego al final. De ser el caso, reiniciamos el indice y pasamos a la siguiente vuelta.
        j=0
        i+=1
        b = j #Le damos a b el valor de j para que podamos agregar +1 a j sin afectar al condicional.
        j += 1
        if items[b] > items[b+1]:
            items[b],items[b+1]=items[b+1],items[b] #swap
            return {"a": b, "b": b+1, "swap": True, "done": False}
        else: #no swap, pero retornamos False para que se produsca el raycast. (Intentar comentar esta parte para ver cual es el error)
            return {"a": b, "b": b+1, "swap": False, "done": False}

    else: #Mismo proceso de arriba, pero sin reiniciar j.
        b = j
        j += 1
        if items[b] > items[b+1]:
            items[b],items[b+1]=items[b+1],items[b]
            return {"a": b, "b": b+1, "swap": True, "done": False}
        else:
            return {"a": b, "b": b+1, "swap": False, "done": False}