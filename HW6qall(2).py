
mat=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

#transpose de la matrice
def transpose(mat, mat_T, i):
    if i == len(mat[0]):
        return mat_T
    mat_T.append(aidcolumntolist(mat, [], 0, i))
    return transpose(mat, mat_T, i + 1)
# transpose aideur
def aidcolumntolist(mat, l, i,j):
    if i == len(mat):
        return l
    l.append(mat[i][j])
    return aidcolumntolist(mat, l, i+1, j)


#transforme une liste en string
def listtoString(list1, str, i):
    if i == len(list1):
        return str
    str += list1[i]
    return listtoString(list1, str, i+1)


#verifie si a il est a gauche de b
def AinleftofB(str1,str2,i):
    if str1 not in str2[i:]:
        return i-1
    return AinleftofB(str1,str2, i+1)

#veirifie si b il est a gauche de a

def AinrightofB(str1,str2,i):
    if str1 not in str2[:i]:
        return i+1
    return AinrightofB(str1,str2, i-1)
#verifie si le mot est dans une des lignes
def passage_ligne(mat,word,i):
    if (word in  listtoString(mat[i],"",0)):
        return i
    if i==0:
        return -1
    return passage_ligne(mat,word,i-1)
#verifie si le mot est dans une des colones
def passage_colone(mat,word,i):
    col=transpose(mat,[],i)
    return passage_ligne(col,word,len(col)-1)






