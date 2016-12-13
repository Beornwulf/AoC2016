import hashlib

input = "abbhdwsy"

password = ''
integer = 0

while (len(password) < 8):
    to_hash = input + str(integer)
    hash = hashlib.md5(to_hash).hexdigest()
    if (hash[:5] == '00000'):
        password += hash[5]
    integer += 1

print(password)