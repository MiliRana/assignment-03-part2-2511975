# Assignment 3 – Part 2
# Restaurant Menu & Order Management System
# Name: Mili Rana
# Student ID: 2511975

# Provided Data

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



#Task 1 — Explore the Menu

categories = set()
for item in menu:
    categories.add(menu[item]["category"])

# Print menu grouped by category
for cat in categories:
    print("=====", cat, "=====")
    
    for item in menu:
        if menu[item]["category"] == cat:
            price = menu[item]["price"]
            available = menu[item]["available"]
            
            if available:
                status = "Available"
            else:
                status = "Unavailable"
            
            print(f"{item}    ₹{price:.2f}    [{status}]")
    
    print()


# Menu statistics
total_items = len(menu)
available_items = 0
most_expensive_item = ""
most_expensive_price = 0
under_150 = []

for item in menu:
    price = menu[item]["price"]
    available = menu[item]["available"]
    
    if available:
        available_items += 1
    
    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_item = item
    
    if price < 150:
        under_150.append((item, price))

print("Total number of items:", total_items)
print("Total available items:", available_items)
print("Most expensive item:", most_expensive_item, most_expensive_price)

print("Items under ₹150:")
for item, price in under_150:
    print(item, price)



# Task 2 – Cart Operations

# Cart will store items selected by the customers
cart = []

def add_to_cart(item_name, quantity):
    # Check if item exists in menu
    if item_name not in menu:
        print("Item does not exist in menu.")
        return

    # Check if item is available
    if not menu[item_name]["available"]:
        print("Item is currently unavailable.")
        return

    # Check if item already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print("Quantity updated in cart.")
            return

    # If item not already in cart, add new entry
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })

    print("Item added to cart.")

def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print("Item removed from cart.")
            return

    print("Item not found in cart.")

def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print("Quantity updated.")
            return

    print("Item not found in cart.")

print("\n--- Cart Operations ---")

add_to_cart("Paneer Tikka", 2)
print(cart)

add_to_cart("Gulab Jamun", 1)
print(cart)

add_to_cart("Paneer Tikka", 1)   # Should update quantity to 3
print(cart)

add_to_cart("Mystery Burger", 1) # Not in menu
print(cart)

add_to_cart("Chicken Wings", 1)  # Unavailable
print(cart)

remove_from_cart("Gulab Jamun")
print(cart)

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    print(f"{item['item']}   x{item['quantity']}   ₹{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")
print("====================================")
