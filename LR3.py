"""
Marcelo Schonbrunn
Yann Le Lorier
"""

import sys
import execjs

# reads goto or actions from a csv file
# returns array where row 0 is either terminals or variables
# and the rest of the rows are the actions/gotos
def read_instructions(fname):
    instructions = []
    temp = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines:
            temp = line.split(',')
            instructions.append(temp)

    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            instructions[i][j] = instructions[i][j].replace('\n', '')

    return instructions

# reads production csv and returns a list
# with all production pops
def read_productions(fname):
    productions = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines:
            splitted_line = line.split(',', maxsplit=2)
            temp = [splitted_line[0], splitted_line[1], splitted_line[2].replace('\n', '')]
            productions.append(temp)

    return productions

# reads input .txt and retuns a list with
# the input string.
def read_input(fname):
    input = []
    with open(fname) as f:
        line = f.readline()
        input = line.split(' ')

    for index, symbol in enumerate(input):
        input[index] = symbol.replace('\n', '')
    return input


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

    return None


la_f2 = """
f2 = function (ss) {
        for(var i = 0; i < ss.length; i++) {
        ss[i]["put"] = function(key,value) {this[key] = value};
        ss[i]["contains"] = function(key) {return this[key] != null};
        ss[i]["get"] = function(key) {return this[key]};
        ss[i]["containsKey"] = function(key) {return this[key] != null};
     }
}
"""
semantic_act = ''
funcion_acc = "f = function (ss) { f1 = " + semantic_act + la_f2 + "f2(ss); f1(ss); return ss;}"

def main(arg_list):
    # read files
    try:
        actions = read_instructions(arg_list[1])
        gotos = read_instructions(arg_list[2])
        prods = read_productions(arg_list[3])
        inputs = read_input(arg_list[4])
    except IndexError as ierr:
        usage(ierr)

    # print(actions)
    # print(gotos)
    # print(prods)
    # print(inputs)

    # create instance variables
    parsing_stack = ['0']
    steps = 0
    a = inputs[0]
    right_sent = inputs.copy()
    number = []
    this_terminal = {}
    numbers = []

    # Main algorithm
    while(True):
        s = parsing_stack[len(parsing_stack) - 1]
        aux = actions[int(s) + 1][actions[0].index(a)]
        #print("aux: ", aux)

        # case: actions is shift
        if(aux != '' and aux[0] == 's'):
            # print(f"{right_sent} {parsing_stack} {aux}")
            parsing_stack.append(aux[1:])
            steps += 1
            a = inputs[steps]

        # case action is reduce
        elif(aux != '' and aux[0] == 'r'):
            x = prods[int(aux[1:]) - 1]
            reduction = x[0].replace(' ', '', 2).split('->') #S -> DIGIT DIGITS
            # print(f"{right_sent} {parsing_stack} {x[0]}")
            for _ in range(int(x[1])):
                parsing_stack.pop()
            
            #magic
            # print(x)
            semantic_act = x[2]
            funcion_acc = "f = function (ss) { f1 = " + semantic_act + la_f2 + "f2(ss); f1(ss); return ss;}"
            ctx = execjs.compile(funcion_acc)

            #case found a terminal
            if int(x[1]) == 1 and reduction[1]!='#':
                print(x[0])
                this_terminal = [{}]
                this_terminal = ctx.call("f", this_terminal)
                #only one element
                number.append(this_terminal[0])
            elif reduction[1]=='#':
                print(x[0])
            #Any other productor
            elif int(x[1])!=1:
                print(x[0])
                if x[0] == 'S -> DIGIT DIGITS':# or x[0]=='S -> * S S':
                    number.insert(0, {"n":0})
                    number.insert(0, dict())
                    number = ctx.call("f", number)
                    numbers.append(number.pop(0))
                    number.pop(0)
                    number.pop(0)
                    print("numbers", numbers)
                elif x[0]=='S -> + S S' or x[0]=='S -> * S S':
                    numbers.reverse()
                    numbers.insert(0, dict())
                    numbers.insert(0,dict())
                    numbers = ctx.call("f", numbers)
                    print(numbers)
                    del numbers[1:4]
                    print(numbers)
                    numbers.reverse()
                else:
                    number.insert(0, dict())
                    number = ctx.call("f", number)
                del number[1:3]
            print("number:", number)
            #eo magic

            curr_non_t = gotos[0].index(reduction[0])

            to_replace = searchInArray(right_sent, reduction[1])
            right_sent[to_replace[0]:to_replace[1]] = [reduction[0]]

            parsing_stack.append(
                gotos[int(parsing_stack[len(parsing_stack)-1]) + 1][curr_non_t])
        # Finished parsing
        elif(aux == 'accept'):
            print("Input:", inputs)
            print("Result:", numbers[0])
            # print(f"{right_sent} {parsing_stack} {aux}")
            break

        # no transition rule.
        else:
            print("Lo sentimos la regla de transicion que busca no existe, favor de verificarla, gracias")
            break

def usage(err=None):
    if err:
        print(err)

    print("Usage:\n\tpython LR.py <actionfile.csv> <gotofile.csv> <productions.txt> <input.txt>")
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        usage()

    main(sys.argv)
