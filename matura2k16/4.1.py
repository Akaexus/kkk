points = []

def isPartOfCircle(x, y):
    return (x-200)**2+(y-200)**2==200**2

def isInsideCircle(x, y):
    return (x-200)**2+(y-200)**2<200**2

with open('punkty.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        point = {
            'x': int(line.split(' ')[0]),
            'y': int(line.split(' ')[1]),
        }
        points.append(point)

circlePoints = 0
insidePoints = 0
for p in points:
    if(isPartOfCircle(p['x'], p['y'])):
        circlePoints+=1
    if(isInsideCircle(p['x'], p['y'])):
        insidePoints+=1
print(circlePoints)
print(insidePoints)
