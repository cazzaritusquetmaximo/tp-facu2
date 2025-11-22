Idea "bubble sort":
- Otorgar una lista de valores.
- 

Ejemplo Bubble:
Lista i=0 [5,4,1,3,2] -> [4,5,1,3,2] -> [4,1,5,3,2] -> [4,1,3,5,2] -> [4,1,3,2,5]
i=1 -> [4,1,3,2,5] -> [1,4,3,2,5] -> [1,3,4,2,5] -> [1,3,4,2,5]
for i in range (len(items)): (i{0 - 4]
    for j in range (len(items)-1): (j{0 - 3]
        if items[j] > items[j+1]: (j{1]4 - j{2]3
            (TRUE
            items[j],items[j+1]=items[j+1],items[j]