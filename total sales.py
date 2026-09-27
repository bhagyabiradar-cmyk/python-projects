import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"],
    "Sales": [50000, 20000, 45000, 15000, 25000, 55000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Total sales for each product
result = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(result)

# Average sales for each product
average = df.groupby("Product")["Sales"].mean()

print("\nAverage Sales by Product:")
print(average)