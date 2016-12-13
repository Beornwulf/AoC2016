import hashlib

input = "abbhdwsy"

password = list('        ')
integer = 0
completion = 0

while (completion < 8):
    to_hash = input + str(integer)
    hash = hashlib.md5(to_hash).hexdigest()
    try:
        index = int(hash[5])
        if hash[:5] == '00000' and index < 8:
            print(hash)
            if password[index] == ' ':
                password[index] = hash[6]
                completion += 1
                print(password)
    except:
        pass
    integer += 1

print(''.join(password))