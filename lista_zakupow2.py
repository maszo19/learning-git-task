shopping = {"piekarnia": ["chleb", "bułki", "pączek"],
          "warzywniak": ["marchew", "seler", "rukola"]
          }
count = 0

for store, list in shopping.items():
    list = [item.capitalize() for item in list]
    print(f"Idę do {store.capitalize()}, by kupić {list}")
    count += len(list)

print(f"W sumie kupuję {count} produktów.\n")