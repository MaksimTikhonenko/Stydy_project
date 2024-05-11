# Агрегація даних у словник за категоріями

market = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "potato"), ("vegetable", "tomato"), ("fruit", "mango"),
          ("vegetable", "cucumber"), ("fruit", "orange"), ("vegetable", "broccoli")]
# sort_market = {}

# for k, v in market:
    # if sort_market.get(k):
        # sort_market.get(k).append(v)
    # else:
        # sort_market[k] = [v]
# print(sort_market)

sort_market = {}

categ = {x[0] for x in market} # витягти set з market


for cat in categ: # Перебираємо categ та формуємо змінну cat, та витягуємо категорії    # Перебираємо всі елементи в змінній cat та формуємо змінну el
    el = [a[1] for a in market if a[0] == cat]
    sort_market[cat] = el

print(sort_market)
