# 3_task_list_comprehension

Adjectives = ['Adult', 'Cloudy', 'Golden', 'Horrible', 'National', 'Pleased', 'Careful', 'Comparative']
#Adjectives_2 = []

max_len = int(input("Enter max len: "))

#for el in Adjectives:
    #if len(el) >= max_len:
        #Adjectives_2.append(el)

Adjectives_2 = [el for el in Adjectives if len(el) >= max_len]

print(Adjectives_2)
