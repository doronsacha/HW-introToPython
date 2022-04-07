mat=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
import inp_reader

def across(char_mat,row,start,end):
    return across_helper(char_mat,row,start,end,start, "")


def across_helper(char_mat,row,start,end,i,result):
    if i == end:
        return result
    else:
        result+=char_mat[row][i]
        return across_helper(char_mat,row,start,end,i+1,result)

def down(char_mat,col,start,end):
    return down_helper(char_mat,col,start,end,start,"")

def down_helper(char_mat,col,start,end,j,result):
    if j==end:
        return result
    else:
        result+=char_mat[j][col]
        return down_helper(char_mat,col,start,end,j+1,result)


def word_search_at_index(search_word,char_mat, idx,start,end):
    if down(char_mat,idx,start,end)==search_word:
        return "down"
    if across(char_mat,idx,start,end)==search_word:
        return "across"
    return "not found"



def word_search(search_word, char_mat, idx):
    return word_search_helper(search_word, char_mat, idx,0)

def word_search_helper(search_word, char_mat, idx,start):
    if start== len(char_mat)-len(search_word)+1:
        return "not found"

    end= len(search_word)+ start
    answer=word_search_at_index(search_word,char_mat,idx,start,end)
    if answer=="not found":
        return word_search_helper(search_word, char_mat, idx,start+1)
    return "("+answer+","+str(idx)+","+str(start)+","+str(end)+")"


def word_searche_for_real_helper(search_word, char_mat, idx):
    if idx== len(char_mat):
        return "not found"
    final_answer=word_search(search_word,char_mat,idx)
    if final_answer=="not found":
        return word_searche_for_real_helper(search_word,char_mat,idx+1)
    return final_answer


def word_search_for_real(search_word,char_mat):
    return word_searche_for_real_helper(search_word,char_mat,0)

