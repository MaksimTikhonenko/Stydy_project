
#  список кортежів (кожен кортеж містить тип, число)
num = [("integer", 5), ("float", 3.2), ("integer", 15), ("float", 7.5), ("integer", 10), ("float", 3.5),
       ("integer", 8), ("float", 7.9), ("integer", 3), ("float", 9.1), ("integer", 20), ("float", 4.9), ("float", 4.9)]

# кінцевий результат. Словник (тип: сума значень для кожного типу)
sort_num = {}


num_k = {x[0] for x in num}

for k in num_k:
       v = [y[1]for y in num if y[0] == k]
       sort_num[k] = sum(v)

print(sort_num)
