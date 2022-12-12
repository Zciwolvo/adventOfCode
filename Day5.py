

def popIndexes(l: list, n: int) -> list:
    temp = list(l)
    for _ in range(n):
        temp.pop(0)
    return temp

def insertThings(inserted: list, l2: list, n: int) -> list:
    temp = list(inserted[::-1])
    output = list(l2)
    i = n
    while i > 0:
        output.insert(0, temp[len(temp)-i])
        i -= 1
    return output


if __name__ == "__main__":
    #Part1
    stacks = [
        ["R","C","H"],
        ["F","S","L","H","J","B"],
        ["Q","T","J","H","D","M","R"],
        ["J","B","Z","H","R","G","S"],
        ["B","C","D","T","Z","F","P","R"],
        ["G","C","H","T"],
        ["L","W","P","B","Z","V","N","S"],
        ["C","G","Q","J","R"],
        ["S","F","P","H","R","T","D","L"]
    ]

    f = open("Day5.txt", "r")
    commands = []
    for x in f:
        x = x.replace("\n", "")
        x = x.split(" ")
        elements = [int(y) for y in x if y.isdigit()]
        commands.append(elements)
    for command in commands:
        if len(stacks[command[1]-1]) > command[0]:
            for _ in range(command[0]):
                stacks[command[2]-1].insert(0,stacks[command[1]-1][0])
                stacks[command[1]-1].pop(0)
        else:
            while stacks[command[1]-1] != []:
                stacks[command[2]-1].insert(0,stacks[command[1]-1][0])
                stacks[command[1]-1].pop(0)
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)

    #Part2

    stacks = [
        ["R","C","H"],
        ["F","S","L","H","J","B"],
        ["Q","T","J","H","D","M","R"],
        ["J","B","Z","H","R","G","S"],
        ["B","C","D","T","Z","F","P","R"],
        ["G","C","H","T"],
        ["L","W","P","B","Z","V","N","S"],
        ["C","G","Q","J","R"],
        ["S","F","P","H","R","T","D","L"]
    ]

    f = open("Day5.txt", "r")
    commands = []
    for x in f:
        x = x.replace("\n", "")
        x = x.split(" ")
        elements = [int(y) for y in x if y.isdigit()]
        commands.append(elements)
    for command in commands:
        if len(stacks[command[1]-1]) > command[0]:
            stacks[command[2]-1] = insertThings(stacks[command[1]-1], stacks[command[2]-1], command[0])
            stacks[command[1]-1] = popIndexes(stacks[command[1]-1], command[0])
        else:
            stacks[command[2]-1] = insertThings(stacks[command[1]-1], stacks[command[2]-1], len(stacks[command[1]-1]))
            stacks[command[1]-1] = popIndexes(stacks[command[1]-1], len(stacks[command[1]-1]))
    result = ""
    print(stacks)
    for stack in stacks:
        if stack != []:
            result += stack[0]
        else:
            result += " "
    print(result)

