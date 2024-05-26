def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    new_line = line.strip()
    print(is_float(new_line))
