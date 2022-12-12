


if __name__ == "__main__":
    with open("Day10.txt", mode="r", encoding="utf8") as file:
            lines = file.read().splitlines()
            prevCommand = 0
            cycle = 0
            currentStrength = 1
            strengths = []
            i = 0
            multiplier = 0
            while i != len(lines)-1:
                print("new cycle")
                while ((cycle - 20)) % 40*multiplier != 0: 
                    print(i, cycle)
                    if lines[i] == "noop":
                        cycle += 1
                        i += 1
                        if ((cycle - 20)) % 40 != 0: 
                            strengths.append((cycle)*(currentStrength))
                            cycle = 0
                            currentStrength = 1
                            multiplier += 1
                            i = 0
                    else:
                        if type(lines[i]) is not list:
                            lines[i] = lines[i].split(" ") 
                        lines[i][1] = int(lines[i][1])
                        cycle += 2
                        currentStrength += int(lines[i][1])
                        if ((cycle - 1) - 20) % 40*multiplier == 0:
                            print(cycle, currentStrength)
                            strengths.append((cycle-1)*(currentStrength-lines[i][1]))
                            cycle = 0
                            currentStrength = 1
                            multiplier += 1
                            i = -1
                        i += 1
                    if i == len(lines)-1:
                        multiplier += 1
                        break
                else:
                    print(cycle, currentStrength)
                    strengths.append(cycle*currentStrength)
                    cycle = 0
                    currentStrength = 1
                    i = 0
                    multiplier += 1
    print(sum(strengths))

                