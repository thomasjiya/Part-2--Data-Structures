# Task 1 — Explore the Menu

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

# ============================================
# Part 1: Print menu grouped by category
# ============================================

# Step 1: Get all unique categories in order
categories = ["Starters", "Mains", "Desserts"]

# Step 2: Loop through each category
for category in categories:
    print(f"\n===== {category} =====")

    # Step 3: Loop through menu and filter by category
    for item_name, details in menu.items():
        if details["category"] == category:

            # Check availability
            if details["available"]:
                status = "[Available]"
            else:
                status = "[Unavailable]"

            # Print formatted row
            # :<16 = left align in 16 spaces
            print(f"{item_name:<16} ₹{details['price']:<8.2f} {status}")

# ============================================
# Part 2: Compute and print menu statistics
# ============================================

print("\n" + "=" * 40)
print("Menu Statistics")
print("=" * 40)

# Total number of items on the menu
total_items = len(menu)
print(f"Total items       : {total_items}")

# Total number of available items
available_items = 0
for details in menu.values():
    if details["available"]:
        available_items += 1
print(f"Available items   : {available_items}")

# Most expensive item
most_expensive_name  = ""
most_expensive_price = 0

for item_name, details in menu.items():
    if details["price"] > most_expensive_price:
        most_expensive_price = details["price"]
        most_expensive_name  = item_name

print(f"Most expensive    : {most_expensive_name} (₹{most_expensive_price:.2f})")

# All items priced under ₹150
print(f"\nItems under ₹150:")
for item_name, details in menu.items():
    if details["price"] < 150:
        print(f"  {item_name:<16} ₹{details['price']:.2f}")
#------------------------------------------------------------------------------------
# Task 2 — Cart Operations
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

cart = []

# ============================================
# Helper function: find item in cart
# Returns the cart entry if found, else None
# ============================================
def find_in_cart(item_name):
    for entry in cart:
        if entry["item"] == item_name:
            return entry
    return None

# ============================================
# Helper function: print current cart state
# ============================================
def print_cart():
    if len(cart) == 0:
        print("  Cart is empty")
    else:
        for entry in cart:
            print(f"  {entry['item']:<18} x{entry['quantity']}  ₹{entry['price'] * entry['quantity']:.2f}")
    print()

# ============================================
# Logic 1: Add item to cart
# ============================================
def add_to_cart(item_name, quantity):
    # Check if item exists in menu
    if item_name not in menu:
        print(f"  ✗ '{item_name}' does not exist in the menu.")
        return

    # Check if item is available
    if not menu[item_name]["available"]:
        print(f"  ✗ '{item_name}' is currently unavailable.")
        return

    # Check if item already in cart
    existing = find_in_cart(item_name)

    if existing:
        # Item already in cart — just increase quantity
        existing["quantity"] += quantity
        print(f"  ✓ '{item_name}' quantity updated to {existing['quantity']}")
    else:
        # Item not in cart — add new entry
        cart.append({
            "item":     item_name,
            "quantity": quantity,
            "price":    menu[item_name]["price"]
        })
        print(f"  ✓ '{item_name}' x{quantity} added to cart")

# ============================================
# Logic 2: Remove item from cart
# ============================================
def remove_from_cart(item_name):
    existing = find_in_cart(item_name)

    if existing:
        cart.remove(existing)
        print(f"  ✓ '{item_name}' removed from cart")
    else:
        print(f"  ✗ '{item_name}' is not in the cart")

# ============================================
# Logic 3: Update quantity of item in cart
# ============================================
def update_quantity(item_name, new_quantity):
    existing = find_in_cart(item_name)

    if existing:
        existing["quantity"] = new_quantity
        print(f"  ✓ '{item_name}' quantity updated to {new_quantity}")
    else:
        print(f"  ✗ '{item_name}' is not in the cart")

# ============================================
# Part 4: Simulate the sequence of actions
# ============================================

print("=" * 40)
print("Step 1: Add Paneer Tikka x2")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("=" * 40)
print("Step 2: Add Gulab Jamun x1")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("=" * 40)
print("Step 3: Add Paneer Tikka x1 (should update to 3)")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("=" * 40)
print("Step 4: Try to add Mystery Burger (does not exist)")
add_to_cart("Mystery Burger", 1)
print_cart()

print("=" * 40)
print("Step 5: Try to add Chicken Wings (unavailable)")
add_to_cart("Chicken Wings", 1)
print_cart()

print("=" * 40)
print("Step 6: Remove Gulab Jamun")
remove_from_cart("Gulab Jamun")
print_cart()

# ============================================
# Part 5: Final Order Summary
# ============================================
print("========== Order Summary ==========")

subtotal = 0

for entry in cart:
    item_total = entry["price"] * entry["quantity"]
    subtotal  += item_total
    print(f"{entry['item']:<20} x{entry['quantity']}    ₹{item_total:.2f}")

# Calculate GST and total
gst   = round(subtotal * 0.05, 2)
total = round(subtotal + gst, 2)

print("------------------------------------")
print(f"{'Subtotal:':<28} ₹{subtotal:.2f}")
print(f"{'GST (5%):':<28} ₹{gst:.2f}")
print(f"{'Total Payable:':<28} ₹{total:.2f}")
print("====================================")

#------------------------------------------------------------------------------------
# Task 3 — Inventory Tracker with Deep Copy
import copy

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

# Part 1: Deep copy inventory before changes

inventory_backup = copy.deepcopy(inventory)

print("=" * 45)
print("Deep Copy Demonstration")
print("=" * 45)

# Manually change one value in inventory
# to prove backup is unaffected
inventory["Paneer Tikka"]["stock"] = 999

print(f"inventory stock (Paneer Tikka)        : {inventory['Paneer Tikka']['stock']}")
print(f"inventory_backup stock (Paneer Tikka) : {inventory_backup['Paneer Tikka']['stock']}")
print("✓ Backup is unaffected by the change!\n")

# Restore inventory to original state before continuing
inventory["Paneer Tikka"]["stock"] = 10
print(f"inventory restored to original        : {inventory['Paneer Tikka']['stock']}\n")

# Part 2: Simulate order fulfilment
final_cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

print("=" * 45)
print("Order Fulfilment — Deducting from Inventory")
print("=" * 45)

for entry in final_cart:
    item_name     = entry["item"]
    qty_needed    = entry["quantity"]
    current_stock = inventory[item_name]["stock"]

    if current_stock >= qty_needed:
        # Enough stock — deduct normally
        inventory[item_name]["stock"] -= qty_needed
        print(f"✓ {item_name}: deducted {qty_needed} unit(s). "
              f"Stock remaining: {inventory[item_name]['stock']}")
    else:
        # Not enough stock — deduct only what is available
        print(f"⚠ Warning: Not enough stock for '{item_name}'. "
              f"Only {current_stock} available. Deducting {current_stock}.")
        inventory[item_name]["stock"] = 0

# Part 3: Reorder alerts
print("\n" + "=" * 45)
print("Reorder Alerts")
print("=" * 45)

reorder_found = False

for item_name, details in inventory.items():
    stock         = details["stock"]
    reorder_level = details["reorder_level"]

    if stock <= reorder_level:
        print(f"⚠ Reorder Alert: {item_name} — "
              f"Only {stock} unit(s) left "
              f"(reorder level: {reorder_level})")
        reorder_found = True

if not reorder_found:
    print("All items have sufficient stock.")

# Part 4: Print both inventory and backup
print("\n" + "=" * 45)
print("Final Comparison — Inventory vs Backup")
print("=" * 45)
print(f"{'Item':<18} {'Current Stock':>15} {'Backup Stock':>13}")
print("-" * 45)

for item_name in inventory:
    current = inventory[item_name]["stock"]
    backup  = inventory_backup[item_name]["stock"]

    # Mark items that have changed
    changed = " ←" if current != backup else ""
    print(f"{item_name:<18} {current:>15} {backup:>13}{changed}")

print("\n✓ Deep copy confirmed — backup preserved original values!")

#------------------------------------------------------------------------------
# Task 4 — Daily Sales Log Analysis

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

def print_revenue_table():
    print(f"\n{'Date':<15} {'Orders':>8} {'Revenue':>12}")
    print("-" * 38)

    best_day         = ""
    best_day_revenue = 0

    for date, orders in sales_log.items():
        # Sum all order totals for this day
        daily_revenue = sum(order["total"] for order in orders)
        order_count   = len(orders)

        print(f"{date:<15} {order_count:>8} {f'₹{daily_revenue:.2f}':>12}")

        # Track best selling day
        if daily_revenue > best_day_revenue:
            best_day_revenue = daily_revenue
            best_day         = date

    print("-" * 38)
    print(f"\n🏆 Best Selling Day: {best_day} (₹{best_day_revenue:.2f})")

# ============================================
# Part 1 & 2: Revenue per day + best day
# ============================================
print("=" * 38)
print("Daily Revenue Report")
print("=" * 38)
print_revenue_table()

# ============================================
# Part 3: Most ordered item
# ============================================
print("\n" + "=" * 38)
print("Most Ordered Item")
print("=" * 38)

item_count = {}  # dictionary to count appearances

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:

            # If item already in count add 1
            # If new item set to 1
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

# Print all item counts
print("\nItem order frequency:")
for item, count in item_count.items():
    print(f"  {item:<18} : {count} order(s)")

# Find item with highest count
most_ordered_item  = max(item_count, key=item_count.get)
most_ordered_count = item_count[most_ordered_item]

print(f"\n🏆 Most Ordered: {most_ordered_item} "
      f"(appeared in {most_ordered_count} orders)")

# ============================================
# Part 4: Add new day and reprint table
# ============================================
print("\n" + "=" * 38)
print("Adding 2025-01-05 to Sales Log...")
print("=" * 38)

# Add new day to sales_log
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\nUpdated Daily Revenue Report")
print("=" * 38)
print_revenue_table()

# ============================================
# Part 5: Numbered list of ALL orders
# using enumerate across all dates
# ============================================
print("\n" + "=" * 38)
print("All Orders — Complete List")
print("=" * 38 + "\n")

order_number = 1  # our running counter

for date, orders in sales_log.items():
    for order in orders:

        # Join items list into a string
        items_str = ", ".join(order["items"])

        print(f"{order_number:<4} [{date}] "
              f"Order #{order['order_id']:<3} "
              f"— ₹{order['total']:.2f} "
              f"— Items: {items_str}")

        order_number += 1