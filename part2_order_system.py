# Assignment 3 – Part 2
# Restaurant Menu & Order Management System
# Name: Mili Rana
# Student ID: 2511975

# Provided Data (Do not modify)

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



# Task 1 – Explore the Menu

# Collect all unique categories
categories_set = set()
for dish in menu:
    categories_set.add(menu[dish]["category"])

# Display menu grouped by category with formatting
for category_name in categories_set:
    print(f"\n===== {category_name} =====")
    
    for dish_name, details in menu.items():
        if details["category"] == category_name:
            availability = "Available" if details["available"] else "Unavailable"
            print(f"{dish_name:15} ₹{details['price']:.2f} [{availability}]")

# Compute statistics
total_items = len(menu)
available_items = sum(1 for dish in menu.values() if dish["available"])
most_expensive_dish = max(menu, key=lambda d: menu[d]["price"])
most_expensive_price = menu[most_expensive_dish]["price"]
under_150_items = [(d, menu[d]["price"]) for d in menu if menu[d]["price"] < 150]

print("\n--- Menu Statistics ---")
print(f"Total items on menu: {total_items}")
print(f"Total available items: {available_items}")
print(f"Most expensive item: {most_expensive_dish} ₹{most_expensive_price:.2f}")
print("Items under ₹150:")
for dish, price in under_150_items:
    print(f"{dish:15} ₹{price:.2f}")



# Task 2 – Cart Operations

# Cart to store customer's current order
current_order = []

def add_menu_item_to_order(menu_item, qty):
    """Add a menu item to the current order, update quantity if already in order."""
    if menu_item not in menu:
        print(f"❌ Sorry, {menu_item} is not on the menu!")
        return
    if not menu[menu_item]["available"]:
        print(f"⚠ {menu_item} is currently unavailable!")
        return

    # Check if already in order
    for entry in current_order:
        if entry["item"] == menu_item:
            entry["quantity"] += qty
            print(f"✅ Updated quantity of {menu_item} to {entry['quantity']}")
            return

    # Add new item
    current_order.append({
        "item": menu_item,
        "quantity": qty,
        "price": menu[menu_item]["price"]
    })
    print(f"✅ {menu_item} x{qty} added to your order")

def remove_item_from_order(menu_item):
    """Remove a menu item from the current order."""
    for entry in current_order:
        if entry["item"] == menu_item:
            current_order.remove(entry)
            print(f"🗑️ {menu_item} removed from order")
            return
    print(f"⚠ {menu_item} not found in current order")

def change_item_quantity_in_order(menu_item, qty):
    """Change quantity of an item already in order."""
    for entry in current_order:
        if entry["item"] == menu_item:
            entry["quantity"] = qty
            print(f"✏️ Quantity of {menu_item} updated to {qty}")
            return
    print(f"⚠ {menu_item} not found in current order")

# Simulate sequence
print("\n--- Simulating Cart Operations ---")
add_menu_item_to_order("Paneer Tikka", 2)
add_menu_item_to_order("Gulab Jamun", 1)
add_menu_item_to_order("Paneer Tikka", 1)  # Quantity should update
add_menu_item_to_order("Mystery Burger", 1) # Not on menu
add_menu_item_to_order("Chicken Wings", 1)  # Unavailable
remove_item_from_order("Gulab Jamun")

# Print order summary
print("\n🍽️ Order Summary 🍽️")
subtotal = 0
for entry in current_order:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total
    print(f"{entry['item']:15} x{entry['quantity']} ₹{item_total:.2f}")

gst = round(subtotal * 0.05, 2)
total_payable = subtotal + gst

print("-" * 35)
print(f"Subtotal:           ₹{subtotal:.2f}")
print(f"GST (5%):           ₹{gst:.2f}")
print(f"Total Payable:      ₹{total_payable:.2f}")
print("=" * 35)



# Task 3 – Inventory Tracker with Deep Copy

import copy

# Backup inventory before changes
inventory_backup = copy.deepcopy(inventory)

# Demonstrate deep copy works
inventory["Paneer Tikka"]["stock"] = 5
print("\n--- Deep Copy Demonstration ---")
print(f"Paneer Tikka stock (changed): {inventory['Paneer Tikka']['stock']}")
print(f"Paneer Tikka stock (backup):  {inventory_backup['Paneer Tikka']['stock']}")

# Restore original inventory
inventory = copy.deepcopy(inventory_backup)

# Deduct quantities from current order
for entry in current_order:
    dish_name = entry["item"]
    qty_ordered = entry["quantity"]

    if dish_name in inventory:
        available = inventory[dish_name]["stock"]
        if qty_ordered > available:
            print(f"⚠ Only {available} {dish_name} in stock. Adding what we have!")
            inventory[dish_name]["stock"] = 0
        else:
            inventory[dish_name]["stock"] -= qty_ordered

# Check for reorder alerts
print("\n--- Reorder Alerts ---")
for dish, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {dish} — Only {data['stock']} left (reorder level: {data['reorder_level']})")

# Print final inventory
print("\n🍴 Final Inventory 🍴")
for dish, data in inventory.items():
    print(f"{dish:15} {data}")

print("\n🗂 Inventory Backup (unchanged) 🗂")
for dish, data in inventory_backup.items():
    print(f"{dish:15} {data}")



# Task 4 – Daily Sales Log Analysis

# Step 1: Compute total revenue per day
print("\n--- Revenue per Day ---")
daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"💰 {date}: ₹{total:.2f}")

# Step 2: Find best-selling day
best_day = max(daily_revenue, key=daily_revenue.get)
print(f"🏆 Best-selling day: {best_day} with ₹{daily_revenue[best_day]:.2f}")

# Step 3: Most ordered item
item_counts = {}
for orders in sales_log.values():
    for order in orders:
        for dish in order["items"]:
            item_counts[dish] = item_counts.get(dish, 0) + 1

most_ordered = max(item_counts, key=item_counts.get)
print(f"🔥 Most ordered item: {most_ordered} ({item_counts[most_ordered]} orders)")

# Step 4: Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# Recompute revenue per day
print("\n--- Revenue per Day (after 2025-01-05) ---")
daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"💰 {date}: ₹{total:.2f}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"🏆 Best-selling day now: {best_day} with ₹{daily_revenue[best_day]:.2f}")

# Step 5: Numbered list of all orders
print("\n--- All Orders Numbered ---")
counter = 1
for date, orders in sales_log.items():
    for order in orders:
        items_str = ", ".join(order["items"])
        print(f"{counter}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")
        counter += 1
