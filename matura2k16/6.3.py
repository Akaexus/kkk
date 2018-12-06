def encrypt(word, key):
    key = key%26
    encryptedWord = []
    for letter in word:
        letter = ord(letter)+key
        if letter>90:
            letter = (65+(letter-65)%26)
        encryptedWord.append(chr(letter))
    return ''.join(encryptedWord)

def decrypt(word, key):
    key = key%26
    return encrypt(word, 26-key)

decryptedLines = []

with open('dane_6_3.txt') as f:
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        line = line.split(' ')
        decryptedWord = line[0]
        encryptedWord = line[1]
        f = False
        for key in range(0, 26):
            if encrypt(decryptedWord, key) == encryptedWord:
                f = True
        if f == False:
            print(decryptedWord)
