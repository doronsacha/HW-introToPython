# cheela aleph aleph

n=int(input(""))
liste_two=[]
for i in range(0,n+1):
    a=i**2
    liste_two.append(2**a)          # on ajoute a la liste vide 2 puissance apuissance i carre
print(liste_two)


#cheela aleph beth
N=int(input(""))
liste_five=[]
for i in range(1,N):
    if i%5!=0:    #verifie quel sont les nombres qui ne sont pas multiples de 5
        liste_five.append(i)
print(liste_five)

# targuil bait aleph guimel

count=0  #variable count pour verifier si un moment la liste croit ou decroit quand elle le doit pas
liste_str=input("")
testo=[]
for i in range(0,len(liste_str)):    # partie du code pour recupere une liste du michtamech
    if liste_str[i]!=' ':
        testo.append(int(liste_str[i]))
for i in range(0,int(len(testo)/ 2)):
    if testo[i]>testo[i+1]:
        count+=1
for j in range(int(len(testo) / 2),len(testo)-1):
    if testo[j]<testo[j+1]:
        count+=1
if count!=0:
    print("Not a Middle-Peak list")
else:
    print("A Middle-Peak list")

#chela un daleth
a=input("")
b=input("")

def delete_word(a,b):
    b_list = []
    for i in b:
        if (i != ' '):
            b_list.append(i)
    if a[-1] != ' ':
        a +=' '

    sentence = ""
    in_word = False
    start_word = 0
    for j in range(len(a)):
        if (a[j] in b_list) or (in_word):
            in_word = True
            start_word=j+1
        elif a[j] == ' ':
            sentence= sentence + a[start_word:j+1]
            start_word=j+1
        if a[j] == ' ':
            in_word = False
    return sentence[0:-1]
print(delete_word(a,b))

