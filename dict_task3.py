# Агрегація даних у словник за категоріями

market = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "potato"), ("vegetable", "tomato"), ("fruit", "mango"),
          ("vegetable", "cucumber"), ("fruit", "orange"), ("vegetable", "broccoli")]
#sort_market = {}

#for k, v in market:
    #if sort_market.get(k):
        #sort_market.get(k).append(v)
    #else:
        #sort_market[k] = [v]
#print(sort_market)

kv = set({k: [v] for k, v in market})


print(kv)
#print(sort_market)
