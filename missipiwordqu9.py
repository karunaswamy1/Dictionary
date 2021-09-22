count = {"M":0,"I":0,"S":0,"P":0}
word = "MISSISSIPPI"
d={}
for i in word:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

