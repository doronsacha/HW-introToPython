import os


########################################################################
########################################################################
def sort_words(txt: str) -> str:
    list_txt = txt.split(" ")

    def calcul_mot(l_txt, index):
        ###cette fct calucl la valeur de chaque mot dans la liste
        taille_mot = 0
        for lettres in l_txt[index]:
            taille_mot += ord(lettres)
        return taille_mot

    def calcul_list(l_txt):
        ## cette fonction creee une liste de chaque valeur des mots en tableau ascii
        list_taille_mot = []
        for mot in range(len(l_txt)):
            list_taille_mot.append(calcul_mot(l_txt, mot))
        return list_taille_mot

    def sorted_list(list, liste_numb):
        for i in range(len(liste_numb) - 1, 0, -1):
            for j in range(i):
                if liste_numb[j] > liste_numb[j + 1]:
                    temp, temp_num = list[j], list_numb[j]
                    list[j], list_numb[j] = list[j + 1], list_numb[j + 1]
                    list[j + 1], list_numb[j + 1] = temp, temp_num
        return list

    list_numb = calcul_list(list_txt)
    sorted_txt = ' '.join(sorted_list(list_txt, list_numb))
    return sorted_txt


########################################################################
# DO NOT EDIT!!!
if __name__ == "__main__":
    text = input().strip(os.linesep)
    sorted_text = sort_words(text)
    print(sorted_text)


