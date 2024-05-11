# Задача: Аналіз даних про книги

# Вхідні дані:
list_dct = [{'author': 'Tolkien', 'book': 'The Hobbit', 'pages_count': 310},
            {'author': 'Orwell', 'book': '1984', 'pages_count': 328},
            {'author': 'Tolkien', 'book': 'The Lord of the Rings', 'pages_count': 1178},
            {'author': 'Orwell', 'book': 'Animal Farm', 'pages_count': 112}]
# Вихідні дані:
result = {} # Словник що містить ключ = 1 значення (ім'я автора) : кортеж (2 значення, 3 значення)

for author_book in list_dct:
    author = author_book['author']
    book = author_book['book']
    pagescount = author_book['pages_count']

    m = result.get(author)

    # визначити чи ця книга є книгою з максимальною кільк. сторінок у цього автора

    # якщо у нас вже є найбільша книга для цього і вона має більше сторінок - переходимо на наступну книгу з списку
    if m and pagescount < m[1]:
        continue

    # якщо попередньої найбільшої книжки ще не існує для цього автора
    # або
    # попередня найбільша книжка має менше сторінок ніж та на яку ми дивимся в циклі зараз
    # то треба зберегти ту на яку дивимся зараз як найбільшу для цього автора
    result[author] = (book, pagescount)

print(result)

