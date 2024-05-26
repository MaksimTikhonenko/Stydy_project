# Завдання 1: Знайти максимальний та мінімальний елемент у списку + find_max_min_basic

def find_max_min(lst): # todo об'єднати max and min
    max_number = lst[0] # max_number = max(list)
    for num in lst:
        if num > max_number:
            max_number = num
    min_number = lst[0] # min_number = min(list)
    for n in lst:
        if n < min_number:
            min_number = n

    print('max : '+str(max_number), "\n" 'min : '+str(min_number))

num = [3, 1, 4, 1, 5, 9.5, 0, 2, 6, 5, 3, -3, 5]

find_max_min(num)

# Завдання 2: Знайти середнє значення у списку + find_average_basic

def find_average(lst):
    a = 0
    for x in lst:
        a += x

    b = 0
    for y in lst: # Змінна 'у' залишається по за циклом
        b += 1

    result = a / b
    print("Середнє значення: " + str(result))

find_average(num)
