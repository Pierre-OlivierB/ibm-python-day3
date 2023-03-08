from math import sqrt


def reverse_list(s):
    print(type(s), s)
    temp_list = list(s)
    print(type(temp_list), temp_list)
    test = temp_list.reverse()
    print(temp_list)
    print(type(test))
    return ''.join(temp_list)


word = "oki"
# print(reverse_list(word))

tab = ['test', 'oki', 'doki']
tab.reverse()
testtab = tab
# print(testtab)

# *---------------------------------------
# Al-Khwarizmi
bu_s = 14
bu_n = 20
bu_o = 1775

root = 34
num = 40*1775

mid_root = root/2
result_by_self = mid_root*mid_root
result = result_by_self+num
new_result = sqrt(result)
finish = new_result - mid_root
# print(finish)

# *------------------------------------------------
# *Calendar
# TODO :
# on se donne la liste des noms des mois, la liste des longueurs des mois, l'année, le premier jour de l'année sous la forme :
# 0 pour lundi
# 1 pour mardi
# ...
# 6 pour dimanche
premier_jour = 0
annee = 2023
mois_j = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois_n = ["jan", "fev", "mar", "avr", "mai", "jun",
          "jul", "aou", "sep", "oct", "nov", "dec"]
list_j = ["lu", "ma", "me",
          "je", "ve", "sa", "di"]
# *-----------------------------
# modifier la liste des longueurs de mois pour le cas d'une année bisextile
mois_bis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# *-------------------------------------
# imprimer les 365 numéros de jours...
# à la suite (1 2 3 4 ... 31 1 2 3 ... 28 ... 1 2 3 ... 31 1 2 ... 31)
# sans chercher à grouper, juste les jours les uns après les autres, sur 365 lignes..
# for j in range(len(mois_n)):
#     for i in range((mois_j[j])):
#         if i % 7 == 0:
#             print(end="\n")
#         print(i+1, "", end="")
#     print("", end="\n")
# *-----------------------------------
# même chose que ci-dessus, en revenant à la ligne tous les 7 jours :
# print(4)          : passe à la ligne
# print(5, end="")  : ne passe pas à la ligne
# le résultat ne ressemble toujouors pas à grand chose... mais on y arrive
# *-----------------------------------
# on peut maintenant ajouter un séparateur rudimentaire comme "----------------------"
# ansi que le nom du mois, et une ligne d'entête : print("lun mar mer jeu ven sam dim")
first_day = 0
for j in range(len(mois_n)):
    print("    ", mois_n[j])
    print(" ".join(list_j), end="\n")
    if first_day > 0:
        for x in range(first_day):
            print("   ", end="")
    for i in range((mois_j[j])):
        # print(i+first_day)
        if (i+first_day) % 7 == 0:
            print(end="\n")
        if (i < 10):
            print(i+1, " ", end="")
        elif (i >= 10):
            print(i+1, "", end="")
    print("", end="\n")
    print('---------')
    # print(mois_j[j]-28)
    first_day = mois_j[j]-28
# *-----------------------------------
# comment démarrer un mois ?
# on va "offsetter"
# essayons juste avec un mois éprouvette de 31 jours
# jours = [x+1 for x in range(31)]
# print(jours)


offset = 3  # le mois démarre un jeudi
# lundi = 0 , mardi = 1 ... dimanche = 6
# on peut utiliser format
# *-----------------------------------
# calcul de l'offset suivant du mois suivant
offset = 3
jours = 31


# print(new_offset)
# *-----------------------------------
# on reprend tout ça.
premier_jour = 0
mois_j = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois_n = ["jan", "fev", "mar", "avr", "mai", "jun",
          "jul", "aou", "sep", "oct", "nov", "dec"]
# *-----------------------------------
# on fait une fonction affiche_mois() qui prends en paramètres :
#   le numéro du mois (1 à 12)
#   l'offset
#   et qui renvoie le nouvel offset


def affiche_mois(indice, offset):
    return
# *-----------------------------------
# on utilise affiche mois pour afficher les mois de 1 à 12.
