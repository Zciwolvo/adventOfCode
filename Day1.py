#https://adventofcode.com/2022/day/1

def countCalories(elf):
    weight = 0
    for item in elf:
        weight += item


if __name__ == "__main__":
    inventories = []
    i = 0
    while i < 2236:
        p = input()
        inventories.append(p)
        i += 1

    backpacks = []
    weight = 0
    for item in inventories:
        if item != '':
            weight += int(item)
        else:
            backpacks.append(weight)
            weight = 0
    top3 = []
    for i in range(3):
        top3.append(max(backpacks))
        backpacks.remove(max(backpacks))
    print(top3)
    total_top3 = sum(top3)
    print("answer: ")
    print(total_top3)






