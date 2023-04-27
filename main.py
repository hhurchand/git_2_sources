def grocery_list():
    grocery = ["Milk",
               "Bread",
               "Eggs",
               "sausages",
               "pancakes",
               "jam",
               "buns"]
    return grocery

def clothing():
    clothing_list = ["shirt",
    "dress",
    "socks",
    "tie"
    ]
    return clothing_list

def bills():
    bills_items = ["electricity",
    "laundry",
    "travel",
    "fees"
    ]
    return bills_items


if __name__ == "__main__":
    print("Display grocery list")
    print(grocery_list())
    print(clothing())
    print(bills())
