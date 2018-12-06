lines = []
with open('liczby.txt') as f:
    for line in f:
        lines.append(line[:-2:])

moreZeros = 0
for line in lines:
    zeros = 0
    ones = 0
    for digit in list(line):
        if digit == '1':
            ones+=1
        else:
            zeros+=1
    if(zeros>ones):
        moreZeros+=1
print(moreZeros)
