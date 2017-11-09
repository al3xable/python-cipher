# Ceasar Cipher


def encrypt(msg, a, b, m = 33):
    result = ""
    for ch in msg:
        if ch == '-' or ch == ' ':
            result += ch
        else:
            t = abs(abs(ord(ch)-65))
            k = ((a * t) + b) % m
            for j in range(abs(k)):
                if (ch == 'Я'):
                    ch = 'А'
                ch = chr(ord(ch)+1)
            result += ch

    return result


if __name__ == '__main__':
    text = 'СМЫСЛ ЖИЗНИ НАШЁЙ - НЕПРЕРЫВНОЕ ДВИЖЕНИЕ'
    print(text)
    text = encrypt(text, 7, 2)
    print(text)
