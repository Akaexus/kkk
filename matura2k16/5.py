
def parseFile(filename):
    lines = []
    with open(filename) as sf:
        for line in sf:
            lines.append(line)
    return [line.replace('\n', '').replace('\r', '').split('\t') for line in lines[1::]]

students = {}
rooms = {}
orphanedStudents = {}
for line in parseFile('studenci.txt'):
    students[line[0]] = {
        'imie': line[2],
        'nazwisko': line[1],
        'books': []
    }
for line in parseFile('wypozyczenia.txt'):
    if line[1] in students:
        if 'books' not in students[line[1]]:
            students[line[1]]['books'] = []
        students[line[1]]['books'].append(line[2])


print('\n\n========3========')
m = 0
f = 0
for pesel in students:
    if int(pesel[9])%2==0:
        f+=1
    else:
        m+=1
print('female {}, male {}'.format(f, m))

for line in parseFile('meldunek.txt'):
    if line[1] not in rooms:
        rooms[line[1]] = {}
    rooms[line[1]][line[0]] = students[line[0]]
    del(students[line[0]])

print('\n\n========1========')
maxBooks = 0
maxRoomID = 0
maxPesel = 0
for roomID in rooms:
    for pesel in rooms[roomID]:
        if len(rooms[roomID][pesel]['books'])>maxBooks:
            maxBooks = len(rooms[roomID][pesel]['books'])
            maxPesel = pesel
            maxRoomID = roomID
person = rooms[maxRoomID][maxPesel]
print(person['imie']+' '+person['nazwisko'])
print(person['books'])


print('\n\n========2========')
personsInRooms = 0
for roomID in rooms:
    personsInRooms+=len(rooms[roomID])
print(round(personsInRooms/len(rooms), 4))


print('\n\n========4========')
sstudents = []
for pesel in students:
    sstudents.append(students[pesel])

for i in range(1, len(sstudents)):
    if sstudents[i-1]['nazwisko']<sstudents[i]['nazwisko']:
        sstudents[i-1], sstudents[i] = sstudents[i], sstudents[i-1]
for student in sstudents:
    print(student['nazwisko']+' '+student['imie'])

print('\n\n==========5==========')
sumOfBooks = 0
for roomID in rooms:
    books = []
    for pesel in rooms[roomID]:
        for book in rooms[roomID][pesel]['books']:
            if book not in books:
                books.append(book)
    sumOfBooks+=len(books)
for pesel in students:
    sumOfBooks+= len(students[pesel]['books'])
print(sumOfBooks)
