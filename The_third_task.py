# 3_task_list_comprehension

Adjectives = ['Adult', 'Cloudy', 'Golden', 'Horrible', 'National', 'Pleased', 'Careful', 'Comparative']
Adjectives_2 = []

for el in Adjectives:
    if len(el) >= 7:
        Adjectives_2.append(el)

print(Adjectives_2)
