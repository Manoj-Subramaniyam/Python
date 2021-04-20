d={}
Name="Python World"
for i in Name:
    count=0
    for j in  Name:
        if(i==j):
            count+=1
    d.update({i:count})
print(d)