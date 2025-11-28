# Integrantes:
Cazzari Tusquet, Máximo
Castro, Hernán

# Bubble Sort:
- Fecha 25/11

def step()
    for a in range(n):
        for b in range(n-1-a):
            if items[b] > items[b+1]:
                items[b],items[b+1]=items[b+1],items[b]
                return {"a": b, "b": b+1, "swap": True, "done": False}
    return {"done": True}

Problema: Al retornar luego de realizar el swap, la iteración del bucle for se reinicia desde 0, además de no cumplir con el contrato de la función que especifíca devolver un solo micro-paso.
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

Solucionado: Se eliminaron los bucles for para que no se reinicie el proceso y se trabajó con las variables globales "i" y "j".
"i" actua como la cantidad de vueltas que debe realizar.
"j" actua como el índice en el que esta posicionado, los punteros.

# Notas:
- La función step siempre debe devolver un diccionario, o de los contrario no funcionara correctamente. (Puede romper el html)
- "a" y "b" son variables locales, solo usadas para mantener guardado los datos de los indices a la hora de retornarlos.
- Si se utilizan las variables que estan fuera de la función step, se las debe declarar como global dentro de esta.
- El condicional que retorna "done":True debe estar al principio, ya que primero verifica si el algoritmo terminó o debe continuar.

# Observaciones dadas por los docentes:
- Código repetido en la comparación y swap en el inner-loop y outer-loop.
#Solución:
- Se movió el bloque de comparación y swap fuera del if (j+1 == n-i) porque estaba escrito dos veces con la misma lógica. Se comparaba 
mientras el iterador llegaba hacia el final y de nuevo al llegar al final, generando código duplicado.







# Informe de selection_sort:
fecha 27nov

- Al principio no le veía sentido a la variable n y tampoco entendía cómo finalizar un barrido. Después pude relacionar ambas cosas.

- Tuve problemas para entender por qué en la devolución con return, cuando done = True,
tenía que devolver todo el diccionario o no.Llegamos a la conclusión de que lo demás no
importaba, porque done indica que ya está todo listo, así que no hace falta devolver las
 otras variables si igual después se van a reiniciar.
Así mismo, llegamos a la conclusión de siempre poner la condición del return "done"=True al comenzar la fn step().
- Tuve inconvenientes debuggeando en Visual Studio Code, así que terminé haciendo una
función con un while llamando a step() para ver qué hacía mi script en Pyscripter.

- Llegamos a la conclusión de que si no poníamos un return en cada condicional, el
visualizador no funcionaba porque no recibía datos.

- Se implementó la fn buscar() que...

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
            buscar()
            return {"a": a, "b": b, "swap": True, "done": False}
        else:
            buscar()
            return {"a": i, "b": min_idx, "swap": True, "done": False}

def buscar():
    global items, n, i, j, min_idx, fase
    i+=1
    j=i+1
    min_idx=i
    fase="buscar"

#informe de insertion_sort:

No se había colocado el global i, j, min_idx, fase en la función step(), lo cual hacia que ni funcione.

