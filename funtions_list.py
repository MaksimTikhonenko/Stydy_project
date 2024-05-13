# Завдання 1: Знайти максимальний та мінімальний елемент у списку + find_max_min_basic

def find_max_min(list):
    # if list is None: #comorehension
    #     print("Список має: None")
    #     return
    max_number = max(list)
    min_number = min(list)

    print('max : '+str(max_number), "\n" 'min : '+str(min_number))

num = [3, 1, 4, 1, 5, 9.5, 0, 2, 6, 5, 3, -3, 5]

#find_max_min(num)

# Завдання 2: Знайти середнє значення у списку + find_average_basic

def find_average(lst):
    a = sum(lst)
    b = len(lst)
    result = (a / b)
    print("Середнє значення: " + str(result))

find_average(num)
