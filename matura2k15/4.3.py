lines = []
with open('liczby.txt') as f:
    for line in f:
        lines.append(line[:-2:])


#true if b1>b2
def compareBinaryNumbers(b1, b2):
    if len(b1)>len(b2):
        return True
    elif len(b1)<len(b2):
        return False
    else:
        for i in range(len(b1)-1, -1, -1):
            if b1[i]!=b2[i]:
                if b1[i]=='1':
                    return True
                else:
                    return False
                return False

minLine = lines[0]
minIndex = 0
maxLine = lines[0]
maxIndex = 0
for i in range(0, len(lines)):
    if compareBinaryNumbers(minLine, lines[i]):
        minLine = lines[i]
        minIndex = i
    if compareBinaryNumbers(lines[i], maxLine):
        maxLine = lines[i]
        maxIndex = i
print('MAX {} i jest w {} linijce'.format(maxLine, maxIndex+1))
print('MIN {} i jest w {} linijce'.format(minLine, minIndex+1))
