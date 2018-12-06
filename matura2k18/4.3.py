finalLine = ''
with open('sygnaly.txt') as f:
    for line in f:
        line = line[:-2:] # na linuxie czyta jako \r\n, wiec wywalam dwa znaki
        l = list(line)
        l = [ord(x) for x in l]
        if max(l)-min(l)<=10:
            print(line)
            finalLine = line
with open('wyniki4.txt', 'a') as f:
    f.write('\n\n\n zad 4.3\n'+finalLine)
