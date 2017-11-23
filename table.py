# Cipher with Tables


def decrypt(encrypted_text, key, size_x, size_y):
    # Making key
    tkey = []
    for i in range(len(key)):
        tkey.append((key[i], i))

    nkey = sorted(tkey, key=lambda k: k[0])
    tkey = nkey

    # Making table
    table = []

    for i in range(size_x):
        table.append([])

    for j in range(size_y):
        for i in range(size_x):
            table[i].append(encrypted_text[i*size_y+j])

    # Decrypting
    new_table = []

    for i in range(size_x):
        new_table.append([])

        for j in range(size_y):
            for k in range(size_y):
                if tkey[k][1] == j:
                    new_table[i].append(table[i][k])

    # Making text
    text = ''
    for j in range(size_y):
        for i in range(size_x):
            text += new_table[i][j]

    return text


if __name__ == '__main__':
    print(decrypt('_ОВЯНВТИ_ЕМОНВ_ЕРО_КШЫВДАИЕЕЕСВ_НЛААЕ_АЮЕГК,ТТОТ_СС_ОКЯ', 'ЛИНИЯ', 11, 5))

    print(decrypt('ГНВЕПЛТОААДРНЕВТЕЬИОРПОТМБЧМОРСОЫЬИ', 'ПЕЛИКАН', 5, 7))
    print(decrypt('ЬЕСОУЬ,ГТСХК_ОАТООУ_НАД_ВДОЁЯПЫОВТЩР,СИСИО_ТШЯЙЖНОЬ_|_ИЕЙ_ТДТ_Н-ОЕЬОО_ЛН_', 'РАБОТА', 12, 6))
