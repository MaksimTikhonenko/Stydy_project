# # Перевірка формату числа

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


with open('input.txt', 'r') as file:    # todo Вичитати кожну лінію окремо
    lines = file.readlines()

for line in lines:
    new_line = line.strip()
    print(is_float(new_line))

# first attempt
# fl = []
# with open('input.txt', 'r') as file:  # Відкрити текстовий файл,та перевірити кожен рядок
#                                         чи є він числом з плаваючою комою
#     lines = file.readlines()
#     # while inp:
#     #     inp.strip()
#     #     inp = file.readline()
# for line in lines:
#     new_line = line.strip()
#     #if isinstance(new_line, float)
#     print(isinstance(new_line, float))
#         #fl.append(new_line)
#     #else:
#         #continue
#
#
# #print(fl)
