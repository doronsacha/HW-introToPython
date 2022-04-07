mat=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
## permet de renvoyer le mot dans la ligne row du debut a la fin
def across(char_mat, row, start, end):
        return "".join((char_mat[row])[start:end+1])

## permet de renvoyer le mot dans la  colone du debut a la fin
def down(char_mat, col, start, end):
    if start==end:
        return ''
    end-=1
    return down(char_mat,col,start,end) + (char_mat[end])[col]


def word_search_at_index(search_word,char_mat, idx,start,end):
    if down(char_mat,idx,start,end)==search_word:
        return "down"
    if across(char_mat,idx,start,end)==search_word:
        return "across"
    return "not found"

def rechercheur(search_word, char_mat, idx,start):
    if start== len(char_mat)-len(search_word)+1:
        return "not found"

    end= len(search_word)+ start
    rep=word_search_at_index(search_word,char_mat,idx,start,end)
    if rep=="not found":
        return rechercheur(search_word, char_mat, idx,start+1)
    else:
        return "("+rep+","+str(idx)+","+str(start)+","+str(end)+")"


def recherchemot(search_word, char_mat, idx):
    if idx== len(char_mat):
        return "not found"
    reponse=word_search(search_word,char_mat,idx)
    if reponse=="not found":
        return recherchemot(search_word,char_mat,idx+1)
    return reponse

def word_search(search_word, char_mat, idx):
    return rechercheur(search_word, char_mat, idx,0)

def final(mot,matos):
    return recherchemot(mot,matos,0)

def total()
