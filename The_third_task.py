# 3_task_list_comprehension

import sys

Adjectives = ['Adult', 'Cloudy', 'Golden', 'Horrible', 'National', 'Pleased', 'Careful', 'Comparative']
Adjectives_2 = []

max_len = int(sys.argv[1])

for el in Adjectives:
    if len(el) >= max_len:
        Adjectives_2.append(el)

print(Adjectives_2)
