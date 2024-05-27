# # Перевірка формату числа

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


# with open('input.txt', 'r') as file:    # todo Вичитати кожну лінію окремо
#     lines = file.readlines()
#
# for line in lines:
#     new_line = line.strip()
#     print(is_float(new_line))


with open('input.txt', 'r') as file:    # todo Completed!!!
    line = file.readline()
    while line:
        line.strip()
        line = file.readline()
        print(is_float(line))
