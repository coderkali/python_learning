supermarket = { "store1":  
                   {"name":"Kali general Store",
                    "items":[
                         {"name":"Soap","Quantity":30},
                         {"name":"Brush","Quantity":40},
                         {"name":"Pen","Quantity":20}
                         ]
                    },
                "store2":  
                   {"name":"Meeta Book Store",
                    "items":[
                         {"name":"Python","Quantity":30},
                         {"name":"Java","Quantity":40},
                         {"name":"React","Quantity":20}
                         ]
                    },
                }

# Print the store details

print(supermarket["store1"])
print(supermarket["store1"]["name"])
print(supermarket.get("store1").get("name"))

# Print names of all items in store1


itemsList = supermarket["store1"]["items"]
print(itemsList)

for items in itemsList:
    print(items["name"])


# How many quantity of React

itemsList = supermarket["store2"]["items"]
print(itemsList)

for items in itemsList:
    if items["name"] == "React":
        print(items["Quantity"])
    



