def boolean1(list1, k1):
    count = 0
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):

            if (list1[i] + list1[j] == int(k)):
                count += 1
    if (count > 0):
        return "True"
    else:
        return "False"


list1 = [10, 15, 3, 7]
k = input("enter sum to verify:")
print(boolean1(list1, k))