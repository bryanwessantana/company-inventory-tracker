# Overview

As a software engineer aiming to design highly structured and data-compliant applications, I built this project to master programmatic interactions with relational database engines. Building this utility allowed me to dive deep into SQL execution lifetimes, entity relationship modeling, and ACID-compliant transaction control.

[cite_start]The **Company Inventory & Analytics Tracker** is a Python command-line utility that interfaces with a local SQLite database engine (`inventory.db`)[cite: 136, 140]. [cite_start]The software programmatically designs and maintains relational schemas for tracking products and suppliers, enforcing foreign-key integrity at the database layer[cite: 137, 140, 143].

[cite_start]My purpose in building this application was to establish a solid foundation in transactional SQL, understand how to safely bind parameters to queries to prevent injection vulnerabilities, and explore how database aggregate calculations can be transformed into actionable financial reporting metrics[cite: 141, 142, 145].

[Software Demo Video](SUA_URL_DO_LOOM_AQUI)

# Relational Database Schema

[cite_start]The database consists of two tables connected by a one-to-many relationship, managed programmatically[cite: 140, 143]:

1. **`suppliers` Table**: Stores the vendor source entity.
   - [cite_start]`supplier_id` (INTEGER, Primary Key, Autoincrement) [cite: 140]
   - [cite_start]`name` (TEXT, Not Null) [cite: 140]
   - [cite_start]`contact` (TEXT) [cite: 140]

2. [cite_start]**`products` Table**: Stores inventory items mapped to their corresponding supplier[cite: 140, 143].
   - [cite_start]`product_id` (INTEGER, Primary Key, Autoincrement) [cite: 140]
   - [cite_start]`name` (TEXT, Not Null) [cite: 140]
   - [cite_start]`price` (REAL, Not Null) [cite: 140]
   - [cite_start]`quantity` (INTEGER, Not Null) [cite: 140]
   - [cite_start]`last_updated` (TEXT, Not Null) [cite: 140]
   - [cite_start]`supplier_id` (INTEGER, Foreign Key referencing `suppliers(supplier_id)`) [cite: 140, 143]

# Development Environment

- [cite_start]**IDE**: Visual Studio Code [cite: 61]
- [cite_start]**Language**: Python (v3.10+) [cite: 61, 136]
- [cite_start]**Database Engine**: SQLite (Native `sqlite3` driver) [cite: 136]
- [cite_start]**Version Control**: Git & GitHub [cite: 61, 151, 175]

# Useful Websites

- [SQLite Autoincrement Documentation](https://www.sqlite.org/autoinc.html)
- [Python sqlite3 Module API Reference](https://docs.python.org/3/library/sqlite3.html)
- [W3Schools SQL INNER JOIN Statement](https://www.w3schools.com/sql/sql_join_inner.asp)
