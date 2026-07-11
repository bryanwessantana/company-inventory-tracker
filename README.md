# Overview

As a software engineer aiming to design highly structured and data-compliant applications, I built this project to master programmatic interactions with relational database engines. Building this utility allowed me to dive deep into SQL execution lifetimes, entity relationship modeling, and ACID-compliant transaction control.

The **Company Inventory & Analytics Tracker** is a Python command-line utility that interfaces with a local SQLite database engine (`inventory.db`). The software programmatically designs and maintains relational schemas for tracking products and suppliers, enforcing foreign-key integrity at the database layer.

My purpose in building this application was to establish a solid foundation in transactional SQL, understand how to safely bind parameters to queries to prevent injection vulnerabilities, and explore how database aggregate calculations can be transformed into actionable financial reporting metrics.

[Software Demo Video](SUA_URL_DO_LOOM_AQUI)

# Relational Database Schema

The database consists of two tables connected by a one-to-many relationship, managed programmatically:

1. **`suppliers` Table**: Stores the vendor source entity.
   - `supplier_id` (INTEGER, Primary Key, Autoincrement)
   - `name` (TEXT, Not Null)
   - `contact` (TEXT)

2. **`products` Table**: Stores inventory items mapped to their corresponding supplier.
   - `product_id` (INTEGER, Primary Key, Autoincrement)
   - `name` (TEXT, Not Null)
   - `price` (REAL, Not Null)
   - `quantity` (INTEGER, Not Null)
   - `last_updated` (TEXT, Not Null)
   - `supplier_id` (INTEGER, Foreign Key referencing `suppliers(supplier_id)`)

# Development Environment

- **IDE**: Visual Studio Code
- **Language**: Python (v3.10+)
- **Database Engine**: SQLite (Native `sqlite3` driver)
- **Version Control**: Git & GitHub

# Useful Websites

- [SQLite Autoincrement Documentation](https://www.sqlite.org/autoinc.html)
- [Python sqlite3 Module API Reference](https://docs.python.org/3/library/sqlite3.html)
- [W3Schools SQL INNER JOIN Statement](https://www.w3schools.com/sql/sql_join_inner.asp)
