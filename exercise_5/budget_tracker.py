from datetime import datetime
import math

# Global data storage
budget_data = {}
budget_limits = {}

def add_transaction(date_str, category, amount, transaction_type):
    """Add an income or expense transaction"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        month_key = date_obj.strftime("%Y-%m")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return
    
    if month_key not in budget_data:
        budget_data[month_key] = {"income": {}, "expenses": {}}
    
    if transaction_type not in ["income", "expenses"]:
        print("Error: Transaction type must be 'income' or 'expenses'")
        return
    
    if category in budget_data[month_key][transaction_type]:
        budget_data[month_key][transaction_type][category] += amount
    else:
        budget_data[month_key][transaction_type][category] = amount

def set_budget_limit(category, limit):
    """Set monthly budget limit for a category"""
    budget_limits[category] = limit

def get_monthly_summary(month_key):
    """Generate monthly summary"""
    if month_key not in budget_data:
        return None
    
    month_data = budget_data[month_key]
    total_income = sum(month_data["income"].values())
    total_expenses = sum(month_data["expenses"].values())
    net_savings = total_income - total_expenses
    savings_percentage = (net_savings / total_income * 100) if total_income > 0 else 0
    
    # Expense breakdown
    expense_breakdown = []
    for category, amount in month_data["expenses"].items():
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        expense_breakdown.append((category, amount, percentage))
    
    # Budget alerts
    budget_alerts = []
    for category, amount in month_data["expenses"].items():
        if category in budget_limits:
            limit = budget_limits[category]
            if amount > limit:
                over_amount = amount - limit
                percentage = (amount / limit * 100) if limit > 0 else 0
                budget_alerts.append((category, over_amount, percentage))
    
    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_savings": net_savings,
        "savings_percentage": savings_percentage,
        "expense_breakdown": expense_breakdown,
        "budget_alerts": budget_alerts
    }

def generate_bar_chart(value, max_value, width=20):
    """Generate text-based bar chart"""
    filled = math.ceil((value / max_value) * width) if max_value > 0 else 0
    return '█' * filled + '░' * (width - filled)

def display_report(month_key):
    """Display formatted monthly report"""
    summary = get_monthly_summary(month_key)
    if not summary:
        print(f"No data for {month_key}")
        return
    
    # Format month display
    month_display = datetime.strptime(month_key, "%Y-%m").strftime("%B %Y")
    
    print(f"\n=== BUDGET REPORT: {month_display} ===")
    print(f"Income: ${summary['total_income']:,.2f}")
    print(f"Expenses: ${summary['total_expenses']:,.2f}")
    print(f"Savings: ${summary['net_savings']:,.2f} ({summary['savings_percentage']:.1f}%)\n")
    
    # Expense breakdown
    if summary['expense_breakdown']:
        print("EXPENSE CATEGORIES:")
        max_expense = max(amt for _, amt, _ in summary['expense_breakdown'])
        for category, amount, percentage in summary['expense_breakdown']:
            
            print(f"- {category.ljust(10)}:  {amount:,.0f} ({percentage:.1f}%)")
    
    # Budget alerts(if any)
    if summary['budget_alerts']:
        print("\nBUDGET WARNINGS:")
        for category, over, percent in summary['budget_alerts']:
            print(f"! {category} exceeded by ${over:,.0f} ({percent:.0f}% of limit)")

# Example usage
if __name__ == "__main__":
    # Set budget limits
    set_budget_limit("food", 400)
    set_budget_limit("rent", 1200)
    set_budget_limit("transport", 200)
    
    # Add sample transactions
    add_transaction("2024-01-05", "salary", 3000, "income")
    add_transaction("2024-01-10", "food", 150, "expenses")
    add_transaction("2024-01-15", "food", 300, "expenses")  # Will exceed food budget
    add_transaction("2024-01-01", "rent", 1200, "expenses")
    add_transaction("2024-01-20", "transport", 50, "expenses")
    
    # Display report
    display_report("2024-01")