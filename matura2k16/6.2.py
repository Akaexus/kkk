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

with open('dane_6_2.txt') as f:
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        line = line.split(' ')
        if len(line) is 2 and line[1]!='':
            decryptedLines.append(decrypt(line[0], int(line[1])))
for line in decryptedLines:
    print(line)
