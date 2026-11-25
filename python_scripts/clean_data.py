import pandas as pd

# Load all four datasets
customers = pd.read_csv("datasets/raw/customers.csv")
products = pd.read_csv("datasets/raw/products.csv")
orders = pd.read_csv("datasets/raw/orders.csv")
order_items = pd.read_csv("datasets/raw/order_items.csv")

# Display the first five rows of each dataset
print("CUSTOMERS DATA")
print(customers.head())

print("\nPRODUCTS DATA")
print(products.head())

print("\nORDERS DATA")
print(orders.head())

print("\nORDER ITEMS DATA")
print(order_items.head())

# Clean the customers dataset

# Step 1: Remove duplicate records
customers = customers.drop_duplicates()

# Step 2: Fill missing city values
customers["city"] = customers["city"].fillna("Unknown")

# Step 3: Standardize customer names
customers["customer_name"] = customers["customer_name"].str.strip().str.title()

# Step 4: Standardize city names
customers["city"] = customers["city"].str.strip().str.title()

# Step 5: Display cleaned data
print("\nCLEANED CUSTOMERS DATA")
print(customers)

# Step 6: Check the number of records
print("\nTotal customer records:", len(customers))

products = products.drop_duplicates()
products["category"]=products["category"].str.strip().str.title()
products["product_name"]=products["product_name"].str.strip().str.title()
products["price"] = pd.to_numeric(products["price"], errors="coerce")
products = products.dropna(subset=["product_id", "product_name", "category", "price"])
print("\nCLEANED PRODUCTS DATA")
print(products)
print("\nPRODUCTS DATA TYPES")
print(products.dtypes)

orders=orders.drop_duplicates()
orders["status"]=orders["status"].str.strip().str.title()
orders["order_date"]=pd.to_datetime(orders["order_date"],errors="coerce")
orders=orders.dropna(subset=["order_id","customer_id","order_date","status"])
print("\nCLEANED ORDER DATA")
print(orders)
print("\nORDERS DATA TYPES")
print(orders.dtypes)

order_items=order_items.drop_duplicates()
order_items["quantity"]=pd.to_numeric(order_items["quantity"],errors="coerce")
order_items["unit_price"]=pd.to_numeric(order_items["unit_price"],errors="coerce")
order_items=order_items.dropna(subset=["order_item_id","order_id","product_id","quantity","unit_price"])
print("\nCLEANED ORDER ITEMS DATA")
print(order_items)
print("\nORDER ITEMS DATA TYPES")
print(order_items.dtypes)



import os

# Create cleaned folder if it doesn't exist
os.makedirs("datasets/cleaned", exist_ok=True)

# Save all four cleaned datasets
customers.to_csv("datasets/cleaned/customers_cleaned.csv", index=False)
products.to_csv("datasets/cleaned/products_cleaned.csv", index=False)
orders.to_csv("datasets/cleaned/orders_cleaned.csv", index=False)
order_items.to_csv("datasets/cleaned/order_items_cleaned.csv", index=False)

print("\nAll cleaned datasets saved successfully!")
