# 1_task_list_comprehension

import random

numbers = [random.randint(1, 100) for _ in range(25)]
#even_nums = []
#nums2 = []

#for num in numbers:
    #if num % 2 == 0:
        #even_nums.append(num)

#for el in even_nums:
    #nums2.append(el ** 2)

# list comprehension

even_nums = [num for num in numbers if num % 2 ==0]

nums2 = [el ** 2 for el in even_nums]

print('Початковий список: '+str(numbers))
print('Парні числа: ' + str(even_nums))
print('Парні числа у квадраті: ' + str(nums2))
