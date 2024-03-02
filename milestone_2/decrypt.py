def decrypt(message, key):
    res = ""
    for i in range(len(message)):
        a = message[i]
        if a.isalpha():
            if a.isupper():
                res += chr((ord(a) - key - 65) % 26 + 65)
            else:
                res += chr((ord(a) - key - 97) % 26 + 97)
        else:
            res += a
    return res


key = int(input("Enter key: "))
message = str(input("Enter message: "))
res = decrypt(message, key)
print(res)
