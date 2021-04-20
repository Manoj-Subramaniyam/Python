
def mul(list2):
    list3=[]

    for i in range(0,len(list2)):
        temp=1;
        for j in range(0,len(list2)):
            if i != j:
                temp=temp*list2[j]
        list3.append(temp)
    return list3
list2=[1,2,3,4,5]
print(mul(list2))