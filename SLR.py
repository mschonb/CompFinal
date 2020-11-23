import csv

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
            temp = [line.split(',')[0], line.split(',')[1].replace('\n', '')]
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
    
# print(read_instructions("action1.csv"))
# print(read_instructions("goto1.csv"))
# print(read_productions("producciones1.txt"))
# print(read_input("entrada1.txt"))

def main():
    # read files
    actions = read_instructions("action1.csv")
    gotos = read_instructions("goto1.csv")
    prods = read_productions("producciones1.txt")
    inputs = read_input("entrada1.txt")

    # print(actions)
    # print(gotos)
    # print(prods)
    # print(inputs)

    # create instance variables
    parsing_stack = ['$', '0']
    print(parsing_stack)
    steps = 0
    a = inputs[0]

    # Main algorithm
    while(True):
        s = parsing_stack[len(parsing_stack) - 1]
        aux = actions[int(s) + 1][actions[0].index(a)]
        # case: actions is shift
        if(aux[0] == 's'):
            print(f"{parsing_stack} {aux}")
            parsing_stack.append(aux[1])
            a = inputs[steps + 1]

        # case action is reduce
        elif(aux[0] == 'r'):
            x = prods[int(aux[1]) - 1]
            popped_sum = 0
            for _ in range(int(x[1])):
                popped_sum += int(parsing_stack.pop())

            # unhardcode this (0)
            # this_goto = popped_sum + \
            #    int(gotos[int(parsing_stack[int(len(parsing_stack)) - 1])][0])

            parsing_stack.append(
                gotos[int(parsing_stack[int(len(parsing_stack)) - 1])][0])
            print(f"{parsing_stack} {x[0]}")
        # Finished parsing
        elif(aux == 'accept'):
            break

        # no transition rule.
        else:
            print("No hay regla de transición. No se acepta la cadena.")
            break


if __name__ == "__main__":
    main()
