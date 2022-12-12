

def IsBiggest(mainPoint: int, points: list) -> bool:
    for point in points:
        return all(p < mainPoint for p in point)

def Countscenery(mainPoint: int, points:list ) -> int:
    score = 0
    for point in points:
        for p in point:
            if p >= mainPoint:
                score += 1
                break
            else:
                score += 1
    return score
    
    
if __name__ == "__main__":
    Trees = 0
    scenery = []
    with open("Day8.txt", mode="r", encoding="utf8") as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                lines[i] = [int(num) for num in lines[i]]
            for i in range(0,len(lines)):
                for j in range(0,len(lines)):
                    if i == 0:
                        Trees += 1
                    elif i == len(lines)-1:
                        Trees += 1
                    elif j == 0:
                        Trees += 1
                    elif j == len(lines)-1:
                        Trees += 1
                    else:
                        mainPoint = lines[i][j]
                        lineofSightT = []
                        for col in range(i):
                            lineofSightT.append(lines[col][j])
                         
                        lineofSightT = [lineofSightT]
                        lineofSightL = [lines[i][0:j]]
                        lineofSightR = [lines[i][j+1:len(lines)]]
                        lineofSightB = []
                        for col in range(i+1, len(lines)):
                            lineofSightB.append(lines[col][j])
                        lineofSightB = [lineofSightB]
                        points = [lineofSightT, lineofSightL, lineofSightR, lineofSightB]
                        reversedT = [lineofSightT[0][::-1]]   
                        reversedL = [lineofSightL[0][::-1]]
                        pointsScenery = [reversedT, reversedL, lineofSightR, lineofSightB]
                        state = False
                        score = 1
                        for point in pointsScenery:
                            score *= Countscenery(mainPoint=mainPoint, points=list(point))
                        scenery.append(score)
                        while state == False:
                            for point in points:
                                if IsBiggest(mainPoint=mainPoint, points=list(point)):
                                    Trees += 1
                                    state = True
                                    break
                                else:
                                    continue
                            else:
                                state = True
                        
    print("Visible trees:", Trees)
    print("Scenery score:", max(scenery))