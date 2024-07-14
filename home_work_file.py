# # Перевірка формату числа

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


with open('txt_file/input.txt', 'r') as file:    # todo Completed!!!
    line = file.readline()
    while line:
        line.strip()
        line = file.readline()
        print(is_float(line))
