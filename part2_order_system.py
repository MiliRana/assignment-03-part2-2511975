# Assignment 3 – Part 2
# Restaurant Menu & Order System
# Name: Mili Rana
# Student ID: 2511975

# Provided Data (do not change)

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# -------------------------
# Task 1 – Show Menu
# -------------------------

# Get unique categories
cats = set([menu[d]["category"] for d in menu])

for cat in cats:
    print(f"\n===== {cat} =====")
    for dish, info in menu.items():
        if info["category"] == cat:
            avail = "Available" if info["available"] else "Unavailable"
            print(dish, "₹"+str(info["price"]), f"[{avail}]")

# Stats
total_items = len(menu)
available_count = sum(1 for d in menu.values() if d["available"])
most_exp_item = max(menu, key=lambda x: menu[x]["price"])
most_exp_price = menu[most_exp_item]["price"]
under_150 = [(d, menu[d]["price"]) for d in menu if menu[d]["price"] < 150]

print("\n--- Menu Stats ---")
print("Total items:", total_items)
print("Available items:", available_count)
print(f"Most expensive: {most_exp_item} ₹{most_exp_price}")
print("Items under ₹150:")
for d, p in under_150:
    print(d, "₹"+str(p))

# -------------------------
# Task 2 – Cart Operations
# -------------------------

cart = []

def add_item(name, qty):
    if name not in menu:
        print(f"{name} not on menu")
        return
    if not menu[name]["available"]:
        print(f"{name} not available")
        return
    # if already in cart, update qty
    for c in cart:
        if c["item"] == name:
            c["quantity"] += qty
            print(f"{name} qty updated to {c['quantity']}")
            return
    cart.append({"item": name, "quantity": qty, "price": menu[name]["price"]})
    print(f"{name} x{qty} added")

def remove_item(name):
    for c in cart:
        if c["item"] == name:
            cart.remove(c)
            print(f"{name} removed from cart")
            return
    print(f"{name} not in cart")

def update_qty(name, qty):
    for c in cart:
        if c["item"] == name:
            c["quantity"] = qty
            print(f"{name} qty changed to {qty}")
            return
    print(f"{name} not in cart")

# simulate order
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1) # should become 3
add_item("Mystery Burger", 1) # not on menu
add_item("Chicken Wings", 1) # unavailable
remove_item("Gulab Jamun")

# order summary
print("\nOrder Summary")
subtotal = 0
for c in cart:
    total = c["quantity"]*c["price"]
    subtotal += total
    print(c["item"], "x"+str(c["quantity"]), "₹"+str(total))

gst = round(subtotal*0.05, 2)
total_amt = subtotal + gst

print("-"*30)
print("Subtotal:", subtotal)
print("GST 5%:", gst)
print("Total Payable:", total_amt)
print("="*30)

# -------------------------
# Task 3 – Inventory with Deep Copy
# -------------------------

import copy
inv_backup = copy.deepcopy(inventory)

# test deep copy
inventory["Paneer Tikka"]["stock"] = 5
print("\nPaneer Tikka stock changed:", inventory["Paneer Tikka"]["stock"])
print("Backup stock:", inv_backup["Paneer Tikka"]["stock"])

# restore
inventory = copy.deepcopy(inv_backup)

# deduct from inventory
for c in cart:
    dish = c["item"]
    qty = c["quantity"]
    if dish in inventory:
        avail = inventory[dish]["stock"]
        if qty > avail:
            print(f"Only {avail} {dish} in stock, taking what we can")
            inventory[dish]["stock"] = 0
        else:
            inventory[dish]["stock"] -= qty

# reorder alerts
print("\nReorder Alerts")
for dish, info in inventory.items():
    if info["stock"] <= info["reorder_level"]:
        print(f"⚠ Reorder {dish} only {info['stock']} left (level {info['reorder_level']})")

# final inventory
print("\nInventory now:")
for dish, info in inventory.items():
    print(dish, info)

print("\nInventory backup (unchanged):")
for dish, info in inv_backup.items():
    print(dish, info)

# -------------------------
# Task 4 – Sales Log Analysis
# -------------------------

# revenue per day
print("\nRevenue per day")
rev_day = {}
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    rev_day[date] = total
    print(date, "₹"+str(total))

best_day = max(rev_day, key=rev_day.get)
print("Best-selling day:", best_day, "₹"+str(rev_day[best_day]))

# most ordered item
item_count = {}
for orders in sales_log.values():
    for o in orders:
        for dish in o["items"]:
            item_count[dish] = item_count.get(dish,0)+1

most_ordered = max(item_count, key=item_count.get)
print("Most ordered item:", most_ordered, f"({item_count[most_ordered]} orders)")

# add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# recompute revenue
print("\nRevenue after 2025-01-05")
rev_day = {}
for date, orders in sales_log.items():
    total = sum(o["total"] for o in orders)
    rev_day[date] = total
    print(date, "₹"+str(total))

best_day = max(rev_day, key=rev_day.get)
print("Best-selling day now:", best_day, "₹"+str(rev_day[best_day]))

# numbered list of orders
print("\nAll orders:")
count = 1
for date, orders in sales_log.items():
    for o in orders:
        items = ", ".join(o["items"])
        print(f"{count}. [{date}] Order #{o['order_id']} — ₹{o['total']} — Items: {items}")
        count += 1
