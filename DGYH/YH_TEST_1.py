print(ord("A"))
for i in range(26):
    num = 65 + i
    print("%c" % num)


aa = ["%c" % (x+65) for x in range(26) if x%2!=0]
print(aa)

['B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z', 'AA']