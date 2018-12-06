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

encryptedLines = []

with open('dane_6_1.txt') as f:
    for lines in f:
        encryptedLines.append(encrypt(lines, 107))

for line in encryptedLines:
    print(line)
