tuple1 = (('a', 32), ('b', 54), ('c', 19), ('d', 43))
tuplelist = list(tuple1)
for i in range(0, len(tuplelist)):

    for j in range(i + 1, len(tuplelist)):
        if (tuplelist[j][1] < tuplelist[i][1]):
            temp = tuplelist[j]
            # print(tuplelist[j])
            tuplelist[j] = tuplelist[i]
            tuplelist[i] = temp

print(tuple(tuplelist))