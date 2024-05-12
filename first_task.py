# 1_task_list_comprehension

import random

numbers = [random.randint(1, 100) for _ in range(25)]
even_nums = []
nums2 = []

for num in numbers:
    if num % 2 == 0:
        even_nums.append(num)

for el in even_nums:
    nums2.append(el ** 2)

print(numbers)
print('Парні числа: ' + str(even_nums))
print('' + str(nums2))
