products = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"]
sales = [45000, 30000, 18000, 5000, 12000]

total_sales = sum(sales)
average_sales = total_sales / len(sales)

highest_index = sales.index(max(sales))
lowest_index = sales.index(min(sales))

print("----- SALES ANALYSIS -----")

for i in range(len(products)):
    print(products[i], "₹", sales[i])

print("\nTotal Sales: ₹", total_sales)
print("Average Sales: ₹", round(average_sales, 2))

print(
    "Highest Sale:",
    products[highest_index],
    "₹",
    sales[highest_index]
)

print(
    "Lowest Sale:",
    products[lowest_index],
    "₹",
    sales[lowest_index]
)