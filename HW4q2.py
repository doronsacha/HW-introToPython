import os


########################################################################
# DO NOT EDIT!!!
def read_list():
    lst = input().strip().strip('\'')
    if len(lst):
        lst = lst.strip(os.linesep).split(' ')
        lst = [float(n) for n in lst]

    else:
        lst = []

    return lst
########################################################################


########################################################################
########################################################################
def find_dominant(lst: list, x: float) -> {float, None}:
    if lst is None or x==None or int(len(lst))==0:
        return None
    max = float("-inf")
    for i in range(len(lst)):
        if lst[i] == x and i != len(lst) - 1:
            if lst[i + 1] > max:
                max = lst[i + 1]
    if max == float("-inf"):
        return None
    return max


def get_all_triplets(lst: list) -> list:
    if lst is None or int(len(lst))==0:
        return lst
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    k=max(lst)
    histo = [0] * (k+ 1)
    list_final = []
    for i in range(len(lst)):
        histo[lst[i]]+=1
    for i in range(k+1):
        if histo[i]==3:
            list_final.append(i)
            list_final.append(i)
            list_final.append(i)
    return list_final
########################################################################


########################################################################
# DO NOT EDIT!!!
if __name__ == "__main__":
    in_lst = read_list()
    in_x = input().strip(os.linesep)
    check_in_x = all([True if (c.isnumeric() or c == '.' or c == '-') else False
                      for c in in_x]) and len(in_x)
    in_x = float(in_x) if check_in_x else None
    dominant_x = find_dominant(lst=in_lst, x=in_x)
    print(dominant_x)

    in_lst = read_list()
    counted_list = get_all_triplets(lst=in_lst)
    print(counted_list)
