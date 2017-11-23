# Cesar Cipher


def offset(msg, k):
    result = ""
    for ch in msg:
        if ch == ' ' or ch == '-':
            result += ch
        else:
            result += chr(ord(ch) + k)
    return result


def encrypt(msg, k):
    return offset(msg, k)


def decrypt(msg, k):
    return offset(msg, -k)


if __name__ == '__main__':
    text = 'Я МЫ ДОЛЖНЫ ПРИЗНАТЬ ОЧЕВИДНОЕ: ПОНИМАЮТ ЛИШЬ ТЕ, КТО ХОЧЕТ ПОНЯТЬ'
    print(text)
    text = encrypt(text, 10)
    print(text)
    text = decrypt(text, 10)
    print(text)