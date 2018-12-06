word = ''
with open('sygnaly.txt') as f:
    i = 1
    for line in f:
        if i%40 == 0:
            word += line[9]
        i+=1
    print(word)

with open('wyniki4.txt', 'a') as f:
    f.write('zad 4.1\n'+word)
