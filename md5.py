import hashlib

text = "Zakharenka Lab #8 md5 hash"
md5 = hashlib.md5(text.encode('utf-8')).hexdigest()

print('TEXT : {}\nHASH: {}'.format(text, md5))
