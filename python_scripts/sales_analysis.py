import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("datasets/cleaned/customers_cleaned.csv")
products = pd.read_csv("datasets/cleaned/products_cleaned.csv")
orders = pd.read_csv("datasets/cleaned/orders_cleaned.csv")
order_items = pd.read_csv("datasets/cleaned/order_items_cleaned.csv")

print(customers.head())
print(products.head())
print(orders.head())
print(order_items.head())

print(customers.columns)
print(products.columns)
print(orders.columns)
print(order_items.columns)

sales = pd.merge(orders,order_items,on="order_id")
sales = pd.merge(sales,products,on="product_id")
sales = pd.merge(sales,customers,on="customer_id")
print(sales.head())

sales["revenue"] = sales["quantity"] * sales["unit_price"]
total_revenue = sales["revenue"].sum()
print("Total Sales Revenue:", total_revenue)

total_orders = sales["order_id"].nunique()
average_order_value = total_revenue / total_orders
print("Average Order Value:", average_order_value)

product_sales = sales.groupby("product_name")["quantity"].sum()
best_selling_product = product_sales.sort_values(ascending=False)
print("Best Selling Products:")
print(best_selling_product.head())
print("Best Selling Product:")
print(best_selling_product.index[0])

least_selling_product = product_sales.sort_values(ascending=True)
print("Least Selling Product:")
print(least_selling_product.index[0])

customer_spending = sales.groupby("customer_name")["revenue"].sum()
top_customers = customer_spending.sort_values(ascending=False).head(5)
print("Top 5 Customers:")
print(top_customers)

category_sales = sales.groupby("category")["revenue"].sum()
category_sales = category_sales.sort_values(ascending=False)
print("Sales by Category:")
print(category_sales)

sales["order_date"] = pd.to_datetime(sales["order_date"])
sales["month"] = sales["order_date"].dt.to_period("M")
monthly_revenue = sales.groupby("month")["revenue"].sum()
print("Monthly Revenue:")
print(monthly_revenue)

order_status = orders.groupby("status")["order_id"].nunique()
print("Order Status Analysis:")
print(order_status)
status_revenue = sales.groupby("status")["revenue"].sum()
print("Revenue by Order Status:")
print(status_revenue)



category_sales = sales.groupby("category")["revenue"].sum()
category_sales = category_sales.sort_values()
plt.figure(figsize=(9, 5))
category_sales.plot(kind="barh")
plt.title("Revenue by Product Category")
plt.xlabel("Total Revenue")
plt.ylabel("Product Category")

plt.tight_layout()

plt.savefig("reports/category_sales.png")

plt.show()

daily_revenue = sales.groupby(
    sales["order_date"].dt.date
)["revenue"].sum()

print("Daily Revenue:")
print(daily_revenue)

plt.figure(figsize=(10, 5))

daily_revenue.plot(kind="line", marker="o")

plt.title("Daily Revenue Trend")
plt.xlabel("Order Date")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig("reports/daily_revenue.png")

plt.show()

completed_sales = sales[
    sales["status"].str.lower() == "completed"
]

total_revenue = completed_sales["revenue"].sum()

print("Realized Revenue:", total_revenue)

product_sales.to_csv("reports/product_sales.csv")
top_customers.to_csv("reports/top_customers.csv")
category_sales.to_csv("reports/category_sales.csv")
order_status.to_csv("reports/order_status.csv")
sales.to_csv("reports/complete_sales_analysis.csv", index=False)

print("\nMONTHLY REVENUE DATA")
print(monthly_revenue)

#print(orders["order_date"].dtype)
#print(orders["order_date"].head())

#orders["order_date"] = pd.to_datetime(orders["order_date"],errors="coerce")

#print("Earliest order:", orders["order_date"].min())

#print("Latest order:", orders["order_date"].max())

#print("Unique months:",
     # orders["order_date"].dt.to_period("M").nunique())
