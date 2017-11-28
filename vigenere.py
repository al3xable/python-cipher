from string import printable

TABLE_WIDTH = len(printable)
ASC_A = ord(printable[0])

# ThX Chines guy
def init_table():
    return [[chr((col + row) % TABLE_WIDTH + ASC_A) \
             for col in range(TABLE_WIDTH)] \
            for row in range(TABLE_WIDTH)]


def encrypt(table, words, key):
    cipher = ''
    count = 0
    key = key
    for ch in words:
        key_shift = ord(key[count % len(key)]) - ASC_A
        word_shift = ord(ch) - ASC_A
        cipher += table[key_shift][word_shift]
        count += 1
    return cipher


def decrypt(words, key):
    text = ''
    count = 0
    key = key
    for ch in words:
        shift = ord(ch) - ord(key[count % len(key)])
        text += chr((shift + TABLE_WIDTH) % TABLE_WIDTH + ASC_A)
        count += 1
    return text


if __name__ == '__main__':
    encrypted = encrypt(init_table(), words='Cryptosystem is cryptoresistant if the undertaken cryptanalytical attack do not reach the set goals', key='CRYPTOGRAPHY')
    print(encrypted)
    decrypted = decrypt(words=encrypted, key='CRYPTOGRAPHY')
    print(decrypted)
