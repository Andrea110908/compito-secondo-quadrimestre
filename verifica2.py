L = []
for elem in range (0,10):
    a = elem % 2
    if (a ==0):
        L.append(elem)
print(L)

M = []
i = 0
while i < 10 : 
    x = i %2
    if x == 1:
        M.append(i)
    i = i + 1
print(M)        