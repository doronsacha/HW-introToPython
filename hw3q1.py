
# cheela 2 aleph

n=int(input(""))
matrix=[]
for i in range(n):
    ligne=input("")
    my_list=ligne.split(" ")
    for i in range(len(my_list)):
        my_list[i]=float(my_list[i])
    matrix.append(my_list)
print(matrix)

# cheela 2 beth

def matrices():
    n=int(input(""))
    matrix=[]
    for i in range(n):
        ligne=input("")
        my_list=ligne.split(" ")
        for i in range(len(my_list)):
            my_list[i]=float(my_list[i])
        matrix.append(my_list)
    return matrix


a=matrices()
c=[]
for i in range(len(a[0])):
    for j in range(len(a)):
        c.append((a[j])[i])
print(c)
#cheela 2 guimel

a=matrices()
b=matrices()
c=[]
new=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        c.append((a[i])[j]*(b[i])[j])
        if j==(len(a[i])-1):
            new.append(c)
            c=[]
print(new)
