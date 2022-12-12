
def IsUnique(l: list) -> bool:
    return len(set(l)) == len(l)

def FindUnique4(l: list) -> int:
    for i in range(len(l)-4):
        subSequence = sequence[i:(i+4)]
        if IsUnique(subSequence):
            return(i+4)

def FindUnique14(l: list) -> int:
    for i in range(len(l)-14):
        subSequence = sequence[i:(i+14)]
        if IsUnique(subSequence):
            return(i+14)

if __name__ == "__main__":
    f = open("Day6.txt", "r")
    for x in f:
        sequence = x
        sequence = [char for char in sequence]
    sequence4Output = FindUnique4(sequence)
    print(sequence4Output)
    sequence14Output = FindUnique14(sequence)
    print(sequence14Output)
