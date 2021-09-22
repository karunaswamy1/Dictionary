my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
vallist=[]
for i in my_dict.values():
    vallist.append(i)
max=0
maxlist=[]
for k in range(1,4):
    for j in range (len(vallist)-k-1):
        if vallist[j]>vallist[j+1]:
            temp=vallist[j]
            vallist[j]=vallist[j+1]
            vallist[j+1]=temp
    maxlist.append(vallist[j+1])
print(maxlist)