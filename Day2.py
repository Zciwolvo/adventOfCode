#https://adventofcode.com/2022/day/2

if __name__ == "__main__":
    tacticts = []
    i = 0
    while i < 2500:
        p = list(map(str, input().strip().split() ))
        tacticts.append(p)
        i += 1
    score = 0
    for j in tacticts:
        if j[0] == "A":
            if j[1] == "X":
                score += 4
            elif j[1] == "Y":
                score += 8
            else:
                score += 3
        elif j[0] == "B":
            if j[1] == "X":
                score += 1
            elif j[1] == "Y":
                score += 5
            else:
                score += 9
        elif j[0] == "C":
            if j[1] == "X":
                score += 7
            elif j[1] == "Y":
                score += 2
            else:
                score += 6
    print(score)

    secondPartScore = 0

    for j in tacticts:
        if j[0] == "A":
            if j[1] == "X":
                secondPartScore += 3
            elif j[1] == "Y":
                secondPartScore += 4
            else:
                secondPartScore += 8
        elif j[0] == "B":
            if j[1] == "X":
                secondPartScore += 1
            elif j[1] == "Y":
                secondPartScore += 5
            else:
                secondPartScore += 9
        elif j[0] == "C":
            if j[1] == "X":
                secondPartScore += 2
            elif j[1] == "Y":
                secondPartScore += 6
            else:
                secondPartScore += 7

    print(secondPartScore)