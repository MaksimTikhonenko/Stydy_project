# Агрегація даних у словник за категоріями

market = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "potato"), ("vegetable", "tomato"), ("fruit", "mango"),
          ("vegetable", "cucumber"), ("fruit", "orange"), ("vegetable", "broccoli")]
sort_market = {}

#sort_market.items()

#sort_market = {k: v for k, v in market}

#for k, v in market:
    #if sort_market.get(k):
        #sort_market.get(k).append(v)
    #else:
        #sort_market[k] = [v]
#print(sort_market)

key = {k for k in market}
sort_market = {k:[v] for k,v in key if k in key}

print(key)
