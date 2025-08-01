def smart_inventory_manager():
    inventory = {}
    
    def display_menu():
        print("\n=== SMART INVENTORY MANAGER ===")
        print(f"Current Inventory Value: {calculate_total_value()}")
        check_low_stock(display_only=True)
        print("\n1. Add new item")
        print("2. Update stock")
        print("3. Search items by category")
        print("4. Check low stock items")
        print("5. Calculate total inventory value")
        print("6. Exit")
    
    def format_currency(amount):
        return "${:,.2f}".format(amount)
    
    def add_item():
        while True:
            name = input("\nEnter item name (or 'cancel' to return): ").strip()
            if name.lower() == 'cancel':
                return
            if name in inventory:
                print("⚠️ Item already exists! Use 'Update stock' instead.")
                continue
            
            try:
                price = float(input("Enter item price: $"))
                if price <= 0:
                    print("Price must be positive!")
                    continue
                
                stock = int(input("Enter initial stock quantity: "))
                if stock < 0:
                    print("Stock cannot be negative!")
                    continue
                
                category = input("Enter item category: ").strip().capitalize()
                
                inventory[name] = {
                    "price": price,
                    "stock": stock,
                    "category": category
                }
                print(f"✅ {name} added successfully!")
                return
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
    
    def update_stock():
        if not inventory:
            print("Inventory is empty! Add items first.")
            return
        
        print("\nCurrent items:")
        for i, item in enumerate(inventory.keys(), 1):
            print(f"{i}. {item}")
        
        while True:
            choice = input("\nEnter item number or name (or 'cancel' to return): ").strip()
            if choice.lower() == 'cancel':
                return
            
            # Find item by number or name
            selected_item = None
            try:
                num = int(choice)
                if 1 <= num <= len(inventory):
                    selected_item = list(inventory.keys())[num-1]
            except ValueError:
                if choice in inventory:
                    selected_item = choice
            
            if not selected_item:
                print("Invalid selection! Try again.")
                continue
            
            current_stock = inventory[selected_item]["stock"]
            print(f"\nCurrent stock for {selected_item}: {current_stock}")
            
            while True:
                action = input("Add or remove stock? (a/r): ").lower()
                if action not in ['a', 'r']:
                    print("Please enter 'a' to add or 'r' to remove.")
                    continue
                
                try:
                    amount = int(input(f"Enter amount to {'add' if action == 'a' else 'remove'}: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                    
                    if action == 'r' and amount > current_stock:
                        print(f"Cannot remove more than current stock ({current_stock})!")
                        continue
                    
                    # Update stock
                    if action == 'a':
                        inventory[selected_item]["stock"] += amount
                    else:
                        inventory[selected_item]["stock"] -= amount
                    
                    print(f"✅ Stock updated! New quantity: {inventory[selected_item]['stock']}")
                    break
                except ValueError:
                    print("Invalid amount! Please enter a whole number.")
            break
    
    def search_by_category():
        if not inventory:
            print("Inventory is empty! Add items first.")
            return
        
        categories = sorted({item["category"] for item in inventory.values()})
        print("\nAvailable categories:")
        for cat in categories:
            print(f"- {cat}")
        
        while True:
            category = input("\nEnter category to search (or 'cancel'): ").strip().capitalize()
            if category.lower() == 'cancel':
                return
            
            if category not in categories:
                print("Category not found! Try again.")
                continue
            
            items_in_category = [
                (name, data) 
                for name, data in inventory.items() 
                if data["category"] == category
            ]
            
            print(f"\nFound {len(items_in_category)} items in {category}:")
            for name, data in items_in_category:
                print(f"• {name} - {format_currency(data['price'])} ({data['stock']} in stock)")
            return
    
    def check_low_stock(display_only=False, threshold=5):
        low_stock_items = [
            (name, data["stock"]) 
            for name, data in inventory.items() 
            if data["stock"] <= threshold
        ]
        
        if not low_stock_items:
            if not display_only:
                print("No items with low stock!")
            return
        
        if not display_only:
            print("\n⚠️ LOW STOCK ALERT:")
        for name, stock in sorted(low_stock_items, key=lambda x: x[1]):
            print(f"- {name} ({stock} unit{'s' if stock != 1 else ''} remaining)")
    
    def calculate_total_value():
        total = sum(data["price"] * data["stock"] for data in inventory.values())
        return format_currency(total)
    
    # Menu control loop
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoose option: "))
        except ValueError:
            print("Invalid input! Please enter a number (1-6).")
            continue
        
        if choice == 1:
            add_item()
        elif choice == 2:
            update_stock()
        elif choice == 3:
            search_by_category()
        elif choice == 4:
            check_low_stock()
        elif choice == 5:
            print(f"\nTotal inventory value: {calculate_total_value()}")
        elif choice == 6:
            print("\nThank you for using Smart Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-6.")

# Start the program
smart_inventory_manager()