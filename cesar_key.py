# Cesar with Key Cipher


def make_alphabet(k, key):
    abc = ''
    for i in range(ord('А'), ord('Я') + 1):
        abc += chr(i)

    for a in key:
        abc = abc.replace(str(a), '')

    # New key
    st = set()
    nk = ''
    for l in key:
        if l not in st:
            st.add(l)
            nk += l

    # Make ABC
    abc = nk + abc
    sr = abc[len(abc)-k:len(abc)]
    abc = sr + abc.replace(sr, '')

    return abc


def encrypt(msg, k, key):
    abc = make_alphabet(k, key)
    print('Алфавит: ' + abc)

    for l in range(ord('А'), ord('Я') + 1):
        msg = msg.replace(chr(l), abc[l-ord('А')])

    return msg


if __name__ == '__main__':
    text = 'РАЗУМА ЛИШАЕТ НЕ СОМНЕНИЕ, А УВЕРЕННОСТЬ'
    print('Фраза: ' + text)
    eText = encrypt(text, 10, 'КРИПТОГРАФИЯ')
    print('Результат: ' + eText)
