import time


def b3(color: str, neighbours: int):
    if color == '.' and neighbours == 3:
        return True
    return False


def s23(color: str, neighbours: int):
    if color == '@' and (neighbours == 2 or neighbours == 3):
        return True
    return False


field = []
field_size = int(input())
for i in range(field_size):
    field_list = ['.' for j in range(field_size)]
    field.append(field_list)
print('где разместить точку? (указывайте координаты по полю, то есть 2 5 значит 2 ряд 5 символ)(чтобы остановить, напишите stop):')
while True:
    point = input('''
>>>''')
    if point == 'stop':
        break
    field[int(point.split()[0])][int(point.split()[1])] = '@'
used1field = ''
for i in field:
    stroka = ''
    for j in i:
        stroka += j*3
        stroka += ' '*5
    stroka += '\n'
    used1field += stroka
print(used1field)
input()
while True:
    try:
        quest = {}
        field_print = ''
        index = 0
        for i in field:
            index_in = 0
            stroka = ''
            for j in i:
                neighbor = 0
                for check in range(3):
                    index_in2 = index_in - check + 1
                    if index_in2 != len(i) and index_in2 >= 0 and index > 0:
                        if '@' == field[index - 1][index_in2]:
                            neighbor += 1

                    if check != 1 and index_in2 != len(i) and index_in2 >= 0:
                        if '@' == field[index][index_in2]:
                            neighbor += 1

                    if index != len(field) - 1 and index_in2 != len(i) and index_in2 >= 0:
                        if '@' == field[index + 1][index_in2]:
                            neighbor += 1
                coord = (index, index_in)
                quest[coord] = neighbor
                stroka += j*3
                stroka += ' '*5
                index_in += 1
            if index != len(field) - 1:
                stroka += '\n'
            field_print += stroka
            index += 1
        for key, value in quest.items():
            x, y = key[0], key[1]
            if b3(field[x][y], value):
                field[x][y] = '@'
            elif s23(field[x][y], value):
                field[x][y] = '@'
            else:
                field[x][y] = '.'
        print(field_print)
        time.sleep(0.22)
        for i in range(150):
            print(' ')
    except KeyboardInterrupt:
        quit()