import math
from collections import Counter

for i in range(7):
    print("* " * i)

print("----------------------------")
print(" ")

for j in range(1, 7):
    print((" " * ((7 - j)//2)) + ("* " * j))

print("----------------------------")
print(" ")

## Find substring

var = "abbbccdfabbf"
x = "b"
c = var.count(x)
idx = 0
for i in range(c):
    idx = var.index(x, idx + 1)
    print(idx)

print("----------------------------")
print(" ")

## Sort character of a string and first alpha symbol and then numeric symbols

var = "as79jeyd4k5szu3d21"
alp = []
nu = []
for idx, val in enumerate(var):
    if val.isalpha():
        alp.append(val)
    else:
        nu.append(val)

alp.sort()
nu.sort()

print("".join(alp + nu))

print("----------------------------")
print(" ")

print("abhi"[::-1])

sen = "Python is very easy"
l = sen.split(" ")
print(" ".join(l[::-1]))

k = sen[::-1].split(" ")
print(" ".join(k[::-1]))

print("----------------------------")
print(" ")

var = "a4b2c2"
fin = ""
c = ""
for idx, val in enumerate(var):
    if val.isalpha():
        for j in range(idx+1, len(var)):
            if var[j].isnumeric():
                c += var[j]
            else:
                break
        fin += val * int(c)
        c = ""

print(fin)

print("----------------------------")
print(" ")

# i/p = "ABCDAABBCDE"
# o/p = "ABCDE"

var = "ABCDAABBCDE"
print("".join(sorted(list(set(var)))))


print("----------------------------")
print(" ")

# i/p = "AABBCCEA"
# o/p = A=3, B = 2, C = 2

var = "AABBCCEA"
k = Counter(var)
for i in k.keys():
    print(i + ":" + str(k[i]), sep="")

print("----------------------------")
print(" ")

# i/p = a4k3b2
# o/p = aeknbd

var = "a4k3b2"
fin = ""
c = ""
for idx, val in enumerate(var):
    if val.isalpha():
        for j in range(idx+1, len(var)):
            if var[j].isnumeric():
                c += var[j]
            else:
                break
        fin += val + chr(ord(val) + int(c))
        c = ""

print(fin)

