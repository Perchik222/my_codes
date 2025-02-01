from math import log


def Fano(symbol, max_len):
    coded_name = '0' * max_len
    end = 0
    if max_len <= 1:
        if '0' in symbols_coded:
            symbols_coded['1'] = symbol
        else:
            symbols_coded['0'] = symbol
    else:
        for i in range(2 ** (max_len - 2)):
            if end == 1:
                break
            for j in range(2):
                if end == 1:
                    break
                ex = list(coded_name)
                ex[-1 + (i * -1)] = '1' if i != 0 else '0'
                if j == 0:
                    ex[-1] = '0'
                else:
                    ex[-1] = '1'
                if ''.join(ex) not in symbols_coded.keys():
                    symbols_coded[''.join(ex)] = symbol
                    end += 1
                elif i + 1 == 2 ** (max_len - 2) and 2 ** (max_len - 2) > 1:
                    if end == 1:
                        break
                    for c in range(max_len - 2):
                        ex[c + (i * -1)] = '1'
                        if c == 0:
                            ex[-1] = '0'
                        else:
                            ex[-1] = '1'
                        if ''.join(ex) not in symbols_coded.keys():
                            symbols_coded[''.join(ex)] = symbol
                            end += 1
                            break
        for i in range(2 ** (max_len - 2)):
            if end == 1:
                break
            coded_name = '1' + '0' * (max_len - 1)
            for j in range(2):
                if end == 1:
                    break
                ex = list(coded_name)
                ex[-1 + (i * -1)] = '1' if i != 0 else '0'
                if j == 0:
                    ex[-1] = '0'
                else:
                    ex[-1] = '1'
                if ''.join(ex) not in symbols_coded.keys():
                    symbols_coded[''.join(ex)] = symbol
                    end += 1
                elif i + 1 == 2 ** (max_len - 2) and 2 ** (max_len - 2) > 1:
                    if end == 1:
                        break
                    for c in range(max_len - 2):
                        if ex[0] != 1:
                            ex[c + (i * -1)] = '1'
                        else:
                            ex[c + (i * -1)] = '1'
                        if c == 0:
                            ex[-1] = '0'
                        else:
                            ex[-1] = '1'
                        if ''.join(ex) not in symbols_coded.keys():
                            symbols_coded[''.join(ex)] = symbol
                            end += 1
                            break


text = input('>>>')
text = text.lower() if text.islower() else text
text_splitted = text.split()
symbols = []
symbols_coded = {}
for i in text_splitted:
    for j in i:
        if j not in symbols:
            symbols.append(j)
length = len(symbols)
max_len = 0
if round(log(length, 2)) - log(length, 2) == 0.0:
    max_len = int(log(length, 2))
else:
    for i in range(length):
        if 2 ** i > length:
            max_len = i
            break
for i in symbols:
    Fano(i, max_len)
coded_message = ''
for j in text:
    for i, y in symbols_coded.items():
        if j == y:
            coded_message += i
    if j == ' ':
        coded_message += ' '
print('сообщение: ' + text)
print(length)
print(symbols)
print('зашифрованный вид: ' + coded_message)
print('значения: ', symbols_coded)
