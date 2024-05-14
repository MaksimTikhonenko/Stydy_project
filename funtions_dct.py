# Завдання 3: Знайти найдовший ключ у словнику

dictionary = {
    "apple": 8,
    "banana": 2,
    "cherry": 3,
    "blueberry": 4,
    "apricot": 7,
    "coconut": 7,
    "nectarine": 5,
    "pomegranate": 3,
    }

def find_longest_key(dct):
    max_key = ""
    for k in dct:
        if len(k) > len(max_key):
            max_key = k
    print("Найдовший ключ : " + str(max_key))

find_longest_key(dictionary)
