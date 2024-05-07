# Агрегація даних у словник за категоріями

market = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "potato"), ("vegetable", "tomato"), ("fruit", "mango"),
          ("vegetable", "cucumber"), ("fruit", "orange"), ("vegetable", "broccoli")]
sort_market = {}

key1 = []
key2 = []
vol1 = []
vol2 = []

for a, b in market:

    if a == "fruit":
        key1.append(a)
    if a == "vegetable":
        key2.append(a)

    print(key1)