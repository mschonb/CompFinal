rsf = ['*', 'DIGIT', 'DIGIT', 'DIGITS', '+', '5', '#', '3', '#', '$']
reduction = 'DIGIT DIGITS'
def searchInArray(rsf, reduction):
    #case looking for single char
    if len(reduction) == 1:
        return (rsf.index(reduction), rsf.index(reduction) + 1)

    #case looking for set of chars
    index = 0
    counter = 0
    for v in rsf:
        if index == len(reduction) - 1:
            return (counter - index,  counter - index + len(reduction))
        if v == reduction[index]:
            index += 1  
        else:
            index = 0
        counter += 1

    #case looking for set of strings
    aux = reduction.split(' ')
    if len(aux) == 1:
        return (rsf.index(aux[0]), rsf.index(aux[0]) + 1) #S -> DIGIT; aux = [DIGIT]; rsf.index(aux[0])
    index = 0
    counter = 0 

    while counter < len(rsf):
        #print(rsf[i], ' == ', aux[index])
        if index == len(aux):
            return (counter - index,  counter - index + len(aux))
        if rsf[counter] == aux[index]:
            index += 1
        else:
            counter -= index
            index = 0
        counter += 1



print(searchInArray(rsf, reduction))