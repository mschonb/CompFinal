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
    parsing_stack = ['0']
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
            steps += 1
            a = inputs[steps]

        # case action is reduce
        elif(aux[0] == 'r'):
            x = prods[int(aux[1]) - 1]
            print(f"{parsing_stack} {x[0]}")
            for _ in range(int(x[1])):
                parsing_stack.pop()

            parsing_stack.append(
                gotos[int(parsing_stack[len(parsing_stack)-1]) + 1][0])
        # Finished parsing
        elif(aux == 'accept'):
            print(f"{parsing_stack} {aux}")
            break

        # no transition rule.
        else:
            print("No hay regla de transición. No se acepta la cadena.")
            break


if __name__ == "__main__":
    main()
