# Cipher with Magic Squares

import numpy as np


def encrypt(text, key):
    w = h = len(text) / len(key)
    x = 0
    y = 0
    result = ""
    while x < h:
        result += text[key[x][y] - 1];
        y += 1
        if y > w - 1:
            y = 0
            x += 1
    return result


def decrypt(text, key):
    key = key.flatten()
    result = [' '] * len(key)
    i = 0
    for ch in key:
        result[ch - 1] = text[i]
        i += 1
    return ''.join(result)


if __name__ == '__main__':
    #key = [
    #    [16, 3, 2, 13],
    #    [5, 10, 11, 8],
    #    [9, 6, 7, 12],
    #    [4, 15, 14, 1]
    #]

    key = [
        [4, 15, 6, 9],
        [5, 10, 3, 16],
        [11, 8, 13, 2],
        [14, 1, 12, 7]
    ]

    #key = [
    #    [16, 3, 2, 13],
    #    [9, 6, 7, 12],
    #    [5, 10, 11, 8],
    #    [4, 15, 14, 1]
    #]

    print(decrypt('ЗС_ТДРЕАИ_ЧОАП_В', np.array(key)))

    encrypted = encrypt('ПриезжаюСегодня.', np.array(key))
    print(encrypted)
    decrypted = decrypt(encrypted, np.array(key))
    print(decrypted)

    print('===========')

    encrypted = 'воыюалмьго_ветсо'
    print(encrypted)
    decrypted = decrypt(encrypted, np.array(key))
    print(decrypted)
