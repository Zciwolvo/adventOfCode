#https://adventofcode.com/2022/day/3
import string

def removeDuplicates(list: list) -> list:
    output = []
    for i in list:
        if i not in output:
            output.append(i)
    return output

def Common(l1: list, l2: list, l3: list) -> str:
    common_elements = list(
    set(l1[0]).intersection(l2[0], l3[0])
    )
    return common_elements



if __name__ == "__main__":
    priorities= list(string.ascii_letters)
    bags = []
    i = 0
    prioSum = 0
    while i < 300:
        p = list(map(str, input().strip().split() ))
        bags.append(p)
        i += 1
        badges = []
    for i in range(len(bags)):
        if i % 3 == 0:
            team = [bags[i],bags[i+1],bags[i+2]]
            commonItem = Common(team[0], team[1], team[2])
            badges.append(priorities.index(commonItem[0]) + 1)
        j = [char for char in str(bags[i][0])]
        fHalf = j[0:int(len(j)/2)]
        fHalf = removeDuplicates(fHalf)
        sHalf = j[int(len(j)/2):len(j)]
        sHalf = removeDuplicates(sHalf)
        for i in fHalf:
            if i in sHalf and i:
                prioSum += (priorities.index(i) + 1)
                   
print(prioSum)
print(sum(badges))