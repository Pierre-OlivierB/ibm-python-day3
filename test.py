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
