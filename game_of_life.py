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
t = 0
field_size = ''
print('Вас приветствует программа игра в жизнь! для начала, вам нужно указать размеры поля, но если вы хотите увидеть примеры расположений точек, то рекомендуется поставить значение 50')
while t == 0:
    try:
        field_size = int(input('''размеры поля:
>>>'''))
        t+=1
    except ValueError:
        print('ValueError, try again')
for i in range(field_size):
    field_list = ['.' for j in range(field_size)]
    field.append(field_list)
print('''где разместить точку? 
(указывайте координаты по полю, то есть 2 5 значит 2 ряд 5 символ)(чтобы остановить, напишите "начать"). 
Можете написать несколько значений без запятых через пробел. Если вам необходимы примеры, то напишите "Примеры":''')
while True:
    point = input('''>>>''')
    if point.lower() == 'начать':
        break
    elif point.lower() == 'примеры':
        print('''
1)цикл
2)устойчивая
3)двигающаяся
4)пожиратель
5)ружье
        ''')
        try:
            example_number = int(input('''
>>>'''))
            if example_number == 1:
                for i in range(3):
                    field[22][22+i] = '@'
                    field[23][22+i] = '@'
                    field[24][22+i] = '@'
                    field[25][25+i] = '@'
                    field[26][25+i] = '@'
                    field[27][25+i] = '@'
            elif example_number == 2:
                field[23][23] = '@'
                field[23][24] = '@'
                field[24][23] = '@'
                field[24][24] = '@'
            elif example_number == 3:
                field[5][4] = '@'
                field[6][5] = '@'
                field[7][3] = '@'
                field[7][4] = '@'
                field[7][5] = '@'
            elif example_number == 4:
                field[24][24] = '@'
                field[23][24] = '@'
                field[25][24] = '@'
                field[23][25] = '@'
                field[24][23] = '@'
            elif example_number == 5:
                field[24][13] = '@'
                field[23][13] = '@'
                field[25][13] = '@'
                field[22][14] = '@'
                field[21][15] = '@'
                field[21][16] = '@'
                field[26][14] = '@'
                field[27][15] = '@'
                field[27][16] = '@'
                field[24][5] = '@'
                field[25][5] = '@'
                field[25][4] = '@'
                field[23][27] = '@'
                field[24][26] = '@'
                field[24][27] = '@'
                field[28][26] = '@'
                field[28][27] = '@'
                field[29][27] = '@'
                field[25][29] = '@'
                field[25][30] = '@'
                field[26][29] = '@'
                field[26][30] = '@'
                field[26][31] = '@'
                field[27][29] = '@'
                field[27][30] = '@'

        except ValueError:
            print('некорректное число')
    try:
        point_splitted = list(map(lambda x: int(x), point.split()))
        if len(point_splitted)%2==0:
            index = 0
            for i in point_splitted[::2]:
                field[point_splitted[index]][point_splitted[index+1]] = '@'
                index += 2
        else:
            print('list length error,try again')
    except (IndexError, ValueError):
        print('неверные координаты, попробуйте еще раз')
    used1field = ''
    for i in field:
        stroka = ''
        for j in i:
            stroka += j * 2
            stroka += ' ' * 2
        stroka += '\n'
        used1field += stroka
    print(used1field)
input('начинаем?\n'
      '>>>')
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
                stroka += j*2
                stroka += ' '*2
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