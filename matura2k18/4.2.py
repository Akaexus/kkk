maxUniqueLetters = 0
lineWithMaxUniqueLetters = ''
with open('sygnaly.txt') as f:
    for line in f:
        uniqueLetters = []
        a = list(line)[:-2:] # na linuxie czyta jako \r\n, wiec wywalam dwa znaki
        for letter in a:
            if letter not in uniqueLetters:
                uniqueLetters.append(letter)
        if maxUniqueLetters < len(uniqueLetters):
            maxUniqueLetters = len(uniqueLetters)
            lineWithMaxUniqueLetters = ''.join(a)

with open('wyniki4.txt', 'a') as f:
    f.write('\n\n\n zad 4.2\n'+lineWithMaxUniqueLetters + ' ' + str(maxUniqueLetters))
print(lineWithMaxUniqueLetters)
print(maxUniqueLetters)
