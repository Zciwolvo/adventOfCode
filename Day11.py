

if __name__ == "__main__":
    with open("Day11.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        n = int((len(lines)+1) / 7)
        index = 0
        monkeData = {}
        counter = 0
        for i in range(n):
            sItems = lines[index+1].split(":")
            try:
                sItems = sItems[1].split(",")
            except IndexError:
                pass
            sItems = [int(x) for x in sItems]
            
            operation = lines[index+2].split(":")
            operation = operation[1]
            operation = operation.split(" ")
            operation = [operation[-2], operation[-1]]
            
            test = lines[index+3].split(" ")
            test = test[-1]
            
            truth = lines[index+4].split(" ")
            truth = truth[-1]

            falsehood = lines[index+5].split(" ")
            falsehood = falsehood[-1]

            monkeData["monke"+str(counter)] = [sItems, operation, test, truth, falsehood, 0]
            index += 7
            counter += 1
        for round in range(10000):
            print("round:", round+1)
            for i in range(n):
                #currentMonkeInv = monkeData["monke"+str(i)][0]
                #print(i, currentMonkeInv)
                ######Giga problem z dzieleniem!
                for _ in range(len(monkeData["monke"+str(i)][0])):
                    if monkeData["monke"+str(i)][0] != []:
                        #currentMonkeInvItem = monkeData["monke"+str(i)][0][0]
                        #currentMonkeOperation = monkeData["monke"+str(i)][1][0]
                        try:
                            currentMonkeOperator = int(monkeData["monke"+str(i)][1][1])
                        except ValueError:
                            currentMonkeOperator = monkeData["monke"+str(i)][0][0]
                        currentMonkeDivisor = int(monkeData["monke"+str(i)][2])
                        currentTargetMonkeTrue = monkeData["monke"+str(int(monkeData["monke"+str(i)][3]))][0]
                        currentTargetMonkeFalse = monkeData["monke"+str(int(monkeData["monke"+str(i)][4]))][0]
                        if monkeData["monke"+str(i)][1][0] == "+":
                            monkeData["monke"+str(i)][0][0] = monkeData["monke"+str(i)][0][0] + int(currentMonkeOperator)
                            monkeData["monke"+str(i)][0][0] = int(monkeData["monke"+str(i)][0][0] // 3)
                            monkeData["monke"+str(i)][5] += 1
                        else:
                            monkeData["monke"+str(i)][0][0] = monkeData["monke"+str(i)][0][0] * int(currentMonkeOperator)

                            monkeData["monke"+str(i)][0][0] = int(monkeData["monke"+str(i)][0][0] // 3)
                            monkeData["monke"+str(i)][5] += 1

                        if monkeData["monke"+str(i)][0][0] % currentMonkeDivisor == 0:
                            currentTargetMonkeTrue.append(monkeData["monke"+str(i)][0][0])
                            monkeData["monke"+str(i)][0].remove(monkeData["monke"+str(i)][0][0])
                        else:
                            currentTargetMonkeFalse.append(monkeData["monke"+str(i)][0][0])
                            monkeData["monke"+str(i)][0].remove(monkeData["monke"+str(i)][0][0])
        monkeBuisseness = []
        for i in range(n):
            monkeBuisseness.append(monkeData["monke"+str(i)][5])
        monkeBuisseness.sort()
        monkeBuisseness.reverse()
        print(monkeBuisseness[0]*monkeBuisseness[1])
