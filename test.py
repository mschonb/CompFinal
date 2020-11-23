rsf = ['+', 'a', '*', 'a', 'S', '$'] 
reduction = 'a'


def searchInArray(rsf, reduction):
    if len(reduction) == 1:
        return [rsf.index(reduction), rsf.index(reduction)]
    index = 0
    counter = 0
    for v in rsf:
        if index == len(reduction) - 1:
            return [counter - index,  counter - index + len(reduction) - 1]
        if v == reduction[index]:
            index += 1
        else:
            index = 0
        counter += 1
    return None

print(searchInArray(rsf, reduction))