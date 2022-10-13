# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
def LikeSymbols(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    list = []
    str3 = None
    for i in range(len1):
        count = 0
        for j in range(len2):
            if str1[i] == str2[j]:
                count += 1
        str3 = f"{str1[i]} - {count}"
        list.append(str3)
    return list

print(LikeSymbols(str1, str2))




