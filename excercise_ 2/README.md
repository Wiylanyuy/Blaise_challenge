
Smart Inventory Manager
📝 Description
A Python-based inventory management system that helps track product stock levels, prices, and categories. The program provides real-time inventory valuation, low-stock alerts, and category-based searching capabilities.

✨ Features
Inventory Tracking: Store item details including name, price, stock quantity, and category

Stock Management: Add or remove stock quantities for existing items

Category Search: Quickly find all items in a specific category

Low Stock Alerts: Automatic warnings for items with ≤5 units remaining

Inventory Valuation: Calculate total value of all items in stock

User-Friendly Interface: Clear menu system with input validation


🚀 How to Use
Run the program in a Python environment:

bash
python inventory_manager.py
Follow the on-screen menu options:

Add new item: Enter product details

Update stock: Increase or decrease inventory quantities

Search by category: Find all products in a specific category

Check low stock: View items needing restocking

Calculate total value: See current inventory worth

Exit: Close the program

📊 Sample Usage
text
=== SMART INVENTORY MANAGER ===
Current Inventory Value: $2,847.50

⚠️ LOW STOCK ALERT:
- Laptop (2 units remaining)
- Mouse (3 units remaining)

Choose option: 3
Category to search: Electronics
Found 4 items in Electronics:
• Laptop - $999.99 (2 in stock)
• Phone - $599.99 (15 in stock)
⚠️ Input Validation
The program includes robust input validation for:

Numeric values (prices and quantities)

Positive numbers where required

Existing item checks

Valid menu selections

📂 Data Structure
Inventory is stored in memory using nested dictionaries:

python
{
    "item_name": {
        "price": float,
        "stock": int,
        "category": str
    }
}
📜 License
This project is open-source and available for free use.
