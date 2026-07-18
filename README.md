# 📦 Company Inventory & Analytics Tracker

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Academic-BYU--Idaho-002E5D?style=for-the-badge" alt="BYU-Idaho" />
</p>

As a software engineer aiming to design highly structured and data-compliant applications, I built this project to master programmatic interactions with relational database engines. Building this utility allowed me to dive deep into SQL execution lifetimes, entity relationship modeling, and ACID-compliant transaction control.

The **Company Inventory & Analytics Tracker** is a Python command-line utility that interfaces with a local SQLite database engine (`inventory.db`). The software programmatically designs and maintains relational schemas for tracking products and suppliers, enforcing foreign-key integrity at the database layer.

My purpose in building this application was to establish a solid foundation in transactional SQL, understand how to safely bind parameters to queries to prevent injection vulnerabilities, and explore how database aggregate calculations can be transformed into actionable financial reporting metrics.

🎬 **[Software Demo Video](https://www.loom.com/share/6f3c0c92d25c4eb49463813d2dfb81a3)**

---

## 🗄️ Relational Database Schema

The database consists of two tables connected by a one-to-many relationship, managed programmatically with foreign-key enforcement enabled:

```sql
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    last_updated TEXT NOT NULL,
    supplier_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
```

## 🚀 Getting Started

Prerequisites
* Python 3.10 or higher installed.

### Installation & Execution

Clone this repository to your local machine:
```bash
git clone https://github.com/bryanwessantana/company-inventory-tracker.git
```

Navigate into the project directory:
```bash
  cd company-inventory-tracker
```

Run the application:
```bash
  python inventory.py
```
---

## 🎮 Interface Preview
When you run the application, you will interact with a terminal menu structured like this:

```Plaintext
======================================
     COMPANY INVENTORY TRACKER
======================================
1. Add New Supplier
2. Add New Product
3. View Inventory Analytics (Financial Report)
4. Search Product by ID
5. Exit
--------------------------------------
Select an option: _
```
---

## 🛠️ Development Environment

* **IDE:** Visual Studio Code
* **Language:** Python (v3.10+)
* **Database Engine:** SQLite (Native sqlite3 driver)
* **Version Control:** Git & GitHub

---

## 🔮 Future Enhancements
To further evolve this application, the following milestones are planned:

* [ ] Implement automated unit testing for database transactions using pytest.
* [ ] Containerize the local environment and migrate from SQLite to a production-ready PostgreSQL instance.
* [ ] Refactor the raw SQL queries into an Object-Relational Mapper (ORM) approach using SQLAlchemy.

---

## 🔗 Useful Websites

* [SQLite Autoincrement Documentation](https://www.sqlite.org/autoinc.html)
* [Python sqlite3 Module API Reference](https://docs.python.org/3/library/sqlite3.html)
* [W3Schools SQL INNER JOIN Statement](https://www.w3schools.com/sql/sql_join_inner.asp)

---
