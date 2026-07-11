import sqlite3
from datetime import datetime

def connect_db():
    """
    Establishes a connection to the SQLite database file and enables foreign key constraints.
    Returns the connection object.
    """
    conn = sqlite3.connect("inventory.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def initialize_database():
    """
    Creates the 'suppliers' and 'products' tables if they do not already exist in the database.
    Demonstrates programmatic database and relational table creation with constraints.
    """
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create Suppliers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT
        );
    """)
    
    # Create Products table with a foreign key relation and a timestamp column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            last_updated TEXT NOT NULL,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        );
    """)
    conn.commit()
    conn.close()

def insert_supplier(name, contact):
    """
    Inserts a new supplier record into the database using parameterized queries.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?);", (name, contact))
        conn.commit()
        print("[SUCCESS] Supplier inserted successfully.")
    except sqlite3.Error as e:
        print(f"[ERROR] Could not insert supplier: {e}")
    finally:
        conn.close()

def insert_product(name, price, quantity, supplier_id):
    """
    Inserts a new product entry, dynamically capturing the current timestamp.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO products (name, price, quantity, last_updated, supplier_id) 
            VALUES (?, ?, ?, ?, ?);
        """, (name, price, quantity, timestamp, supplier_id))
        conn.commit()
        print("[SUCCESS] Product inserted successfully.")
    except sqlite3.Error as e:
        print(f"[ERROR] Could not insert product: {e}")
    finally:
        conn.close()

def update_product_stock(product_id, new_qty):
    """
    Modifies an existing product's stock level and updates its tracking timestamp.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            UPDATE products 
            SET quantity = ?, last_updated = ? 
            WHERE product_id = ?;
        """, (new_qty, timestamp, product_id))
        conn.commit()
        print("[SUCCESS] Product stock updated successfully.")
    except sqlite3.Error as e:
        print(f"[ERROR] Could not update stock: {e}")
    finally:
        conn.close()

def delete_product(product_id):
    """
    Deletes a specific product entry from the database using its primary ID key.
    """
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE product_id = ?;", (product_id,))
        conn.commit()
        print("[SUCCESS] Product deleted successfully.")
    except sqlite3.Error as e:
        print(f"[ERROR] Could not delete product: {e}")
    finally:
        conn.close()

def view_inventory_report():
    """
    Performs an INNER JOIN query to retrieve products bound to their relative supplier info.
    Fulfills the relational Join module requirement.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.product_id, p.name, p.price, p.quantity, s.name, p.last_updated
        FROM products p
        INNER JOIN suppliers s ON p.supplier_id = s.supplier_id;
    """)
    rows = cursor.fetchall()
    print("\n--- INVENTORY RELATIONAL REPORT ---")
    for row in rows:
        print(f"ID: {row[0]} | Product: {row[1]} | Price: ${row[2]} | Qty: {row[3]} | Supplier: {row[4]} | Updated: {row[5]}")
    print("-----------------------------------\n")
    conn.close()

def view_analytical_summary():
    """
    Uses aggregate functions (SUM and AVG) to compute mathematical summaries of database numbers.
    Fulfills the Aggregate metric requirement.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(quantity * price), AVG(price) FROM products;")
    summary = cursor.fetchone()
    total_val = summary[0] if summary[0] else 0.0
    avg_price = summary[1] if summary[1] else 0.0
    print("\n--- METRIC ANALYTICAL SUMMARY ---")
    print(f"Total Inventory Asset Capital Valuation: ${total_val:.2f}")
    print(f"Average Unit Price Across Stock Catalog: ${avg_price:.2f}")
    print("---------------------------------\n")
    conn.close()

def filter_products_by_date(start_date, end_date):
    """
    Filters database records based on a text-based date/time range comparison.
    Fulfills the Date/Time filter requirement.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_id, name, last_updated 
        FROM products 
        WHERE last_updated BETWEEN ? AND ?;
    """, (start_date + " 00:00:00", end_date + " 23:59:59"))
    rows = cursor.fetchall()
    print(f"\n--- MODIFIED ENTRIES FROM {start_date} TO {end_date} ---")
    for row in rows:
        print(f"ID: {row[0]} | Item: {row[1]} | Timestamp: {row[2]}")
    print("---------------------------------------------------------\n")
    conn.close()

def main():
    """
    The main execution loop providing an interactive command line interface menu.
    """
    initialize_database()
    while True:
        print("\n=== COMPANY INVENTORY & ANALYTICS TRACKER ===")
        print("1. Add Supplier")
        print("2. Add Product")
        print("3. Update Product Stock (Modify)")
        print("4. Delete Product")
        print("5. View Relational Inventory Report (Join)")
        print("6. View Financial Metrics Summary (Aggregate)")
        print("7. Filter Updates By Date Range")
        print("8. Exit Application")
        
        choice = input("Select a menu option: ")
        if choice == "1":
            name = input("Enter Supplier Name: ")
            contact = input("Enter Contact Email/Phone: ")
            insert_supplier(name, contact)
        elif choice == "2":
            name = input("Enter Product Name: ")
            price = float(input("Enter Unit Price: "))
            qty = int(input("Enter Starting Quantity: "))
            supp_id = int(input("Enter Associated Supplier ID: "))
            insert_product(name, price, qty, supp_id)
        elif choice == "3":
            prod_id = int(input("Enter Product ID to Modify: "))
            qty = int(input("Enter New Stock Quantity: "))
            update_product_stock(prod_id, qty)
        elif choice == "4":
            prod_id = int(input("Enter Product ID to Delete: "))
            delete_product(prod_id)
        elif choice == "5":
            view_inventory_report()
        elif choice == "6":
            view_analytical_summary()
        elif choice == "7":
            start = input("Enter Start Date (YYYY-MM-DD): ")
            end = input("Enter End Date (YYYY-MM-DD): ")
            filter_products_by_date(start, end)
        elif choice == "8":
            print("Terminating runtime engine. Goodbye.")
            break
        else:
            print("Invalid directive option selected. Try again.")

if __name__ == "__main__":
    main()