def all_variants(string):
    #перебираем все возможные длины подпоследовательностей от 1 до длины строки
    for length in range(len(string)+1):
        #проходим по всем возможным начальным индексам для подпоследовательности заданной длины
        for start in range(len(string) - length + 1):
            #возвращаем подстроку строки string начиная с индекса start и длиной length
            yield string[start:start + length]

a = all_variants("abc")
for i in a:
    print(i)