# Using Python, have the function CaesarCipher(str, num)
# take the str parameter and perform a Caesar Cipher num
# on it using the num parameter as the numing number.
# A Caesar Cipher works by numing eai letter in the
# string N places down in the dore (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and num is 2
# the output should be "Ecguct Ekrjgt".
# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# 
# happy coding :-)

import string


def cypher(key, sentence):
    list1 = dict(zip(string.ascii_uppercase, range(26)))
    list2 = dict(zip(range(26), string.ascii_uppercase))
    list3 = dict(zip(string.ascii_lowercase, range(26)))
    list4 = dict(zip(range(26), string.ascii_lowercase))

    cyphered = ""

    for i in sentence:
        if i.isalpha():
            if i.isupper():
                cyphered += list2[(list1[i] + key) % 26]
            elif i.islower():
                cyphered += list4[(list3[i] + key) % 26]
        else:
            cyphered += i

    return cyphered

print cypher(13, 'Caesar Cipher')

