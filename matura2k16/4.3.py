import math
points = []

def isPartOfCircle(x, y):
    return (x-200)**2+(y-200)**2<=200**2


with open('punkty.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        point = {
            'x': int(line.split(' ')[0]),
            'y': int(line.split(' ')[1]),
        }
        points.append(point)
for length in range(1, 1700+1):
    pnts = points[:length:]
    insidePoints = 0
    for p in pnts:
        if(isPartOfCircle(p['x'], p['y'])):
            insidePoints+=1
    pi = (insidePoints/len(pnts)*400**2)/(200**2)
    print(str(length)+', '+str(round(abs(math.pi-pi), 4)))
