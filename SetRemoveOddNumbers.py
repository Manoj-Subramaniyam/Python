set1={23,52,24,75,46,91}
listset1=list(set1)
outputset={}
outputset=set(outputset)
#print(type(outputset))
#print(listset1)
for i in range(0,len(listset1)):
    if(listset1[i]%2==0):
        outputset.add(listset1[i])
print(outputset)