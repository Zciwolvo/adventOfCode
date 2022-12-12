


def Common(l1: list, l2: list) -> int:
    if all(item in l2 for item in l1):
        return 1
    else: 
        return 0

def AnyCommon(l1: list, l2: list) -> int:
    if any(item in l2 for item in l1):
        return 1
    else: 
        return 0

if __name__ == "__main__":
    f = open("Day4.txt", "r")
    rooms = []
    output = 0
    ouputPart2 = 0
    for x in f:
        x = x.split("-")
        x = " ".join(x).split(",")
        y = [char for char in x[-1]]
        y.pop(-1)
        y = " ".join(x).split(" ")
        rooms.append(y)
    for room in rooms:
        pairL = [num for num in range(int(room[0]),int(room[1])+1)]
        pairR = [num for num in range(int(room[2]),int(room[3])+1)]
        if len(pairL) > len(pairR):
            output += Common(pairR, pairL)
            ouputPart2 += AnyCommon(pairR, pairL)
        else:
            output += Common(pairL, pairR)
            ouputPart2 += AnyCommon(pairL, pairR)

    print(output)
    print(ouputPart2)


