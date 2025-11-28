Integrantes:
Cazzari Tusquet, Máximo
Castro, Hernán

Bubble Sort:
- Fecha 25/11

def step()
    for a in range(n):
        for b in range(n-1-a):
            if items[b] > items[b+1]:
                items[b],items[b+1]=items[b+1],items[b]
                return {"a": b, "b": b+1, "swap": True, "done": False}
    return {"done": True}

Problema: Al retornar luego de realizar el swap, la iteración del bucle for se reinicia desde 0.
Objetivo: Encontrar otro método para que no se reinicie el bucle for.

global n,i,j
    if i == n-1:
        return {"done": True}
    if j+1 == n-i:
        j=0
        i+=1
        b = j
        j += 1
        if items[b] > items[b+1]:
            items[b],items[b+1]=items[b+1],items[b]
            return {"a": b, "b": b+1, "swap": True, "done": False}
        else:
            return {"a": b, "b": b+1, "swap": False, "done": False}
    else:
        b = j
        j += 1
        if items[b] > items[b+1]:
            items[b],items[b+1]=items[b+1],items[b]
            return {"a": b, "b": b+1, "swap": True, "done": False}
        else:
            return {"a": b, "b": b+1, "swap": False, "done": False}

Solucionado: Se eliminaron los bucles for para que no se reinicie el proceso y se trabajo con las variables globales "i" y "j".
"i" actua como la cantidad de vueltas que debe realizar.
"j" actua como el indice en el que esta posicionado, los punteros.

Notas:
- La función step siempre debe devolver un diccionario, o de los contrario no funcionara correctamente. (Puede romper el html)
- "a" y "b" son variables locales, solo usadas para mantener guardado los datos de los indices a la hora de retornarlos.
- Si se utilizan las variables que estan fuera de la función step, se las debe declarar como global dentro de esta.
- El condicional que retorna "done":True debe estar al principio, ya que primero verifica si el algoritmo terminó o debe continuar.