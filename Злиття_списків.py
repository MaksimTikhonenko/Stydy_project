num = [("integer", 5), ("float", 3.2), ("integer", 15), ("float", 7.5), ("integer", 10), ("float", 3.5),
       ("integer", 8), ("float", 7.9), ("integer", 3), ("float", 9.1), ("integer", 20), ("float", 4.9)]
sort_num = {}

for k, v in num:
    if sort_num.get(k):
        sort_num.get(k).append(v)
    else:
        sort_num[k] = [v]
    for n in [v]:
        if n == {int}:
            sort_num.get(v)
        else:
            sort_num.update(v or (n + v))

v = sort_num.values()


print(v)
print(sort_num)
