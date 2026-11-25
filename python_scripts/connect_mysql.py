
import mysql.connector

try:

    # 1. Connect to database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sales_analysis"
    )

    print("Connected successfully!")

    # 2. Create cursor
    cursor = connection.cursor()

    # 3. Retrieve customers
    print("\nCUSTOMER RECORDS")
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        print(customer)

    # 4. Retrieve sales revenue
    print("\nTOTAL SALES REVENUE")

    cursor.execute("""
    SELECT SUM(quantity * unit_price)
    FROM order_items
    """)

    revenue = cursor.fetchone()

    print("Revenue:", revenue[0])

    # 5. Retrieve product-wise revenue
    print("\nPRODUCT-WISE REVENUE")

    cursor.execute("""
    SELECT
        p.product_name,
        SUM(oi.quantity * oi.unit_price)
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
    """)

    results = cursor.fetchall()

    for row in results:
        print(row)

except mysql.connector.Error as error:

    print("Error:", error)

finally:

    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()

    print("\nConnection closed.")
