lines = []
with open('liczby.txt') as f:
    for line in f:
        lines.append(line[:-2:])
divby2 = 0
divby8 = 0
for line in lines:
    if(line[-1::] == '0'):
        divby2+=1
    if line[-3::] == '000':
        divby8+=1

print('podzielne przez 2: {}'.format(divby2))
print('podzielne przez 8: {}'.format(divby8))
