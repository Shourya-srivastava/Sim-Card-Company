# SIM Management System 📱

This is a Python-based SIM management system connected to a MySQL database.

### Features:
- Add new customers
- Generate bills with tax
- Check and update SIM status (blocked/unblocked)
- Update balance
- Fetch single/all customer data
- Count and group customers by area
- Calculate average balance

### Technologies Used:
- Python
- MySQL
- `mysql.connector` library

### How to Run:
1. Make sure you have MySQL installed and running.
2. Create a database named `sim_company` and a table `customer`.
3. Update your MySQL credentials in the script.
4. Run the Python file:
   ```bash
   python sim_management.py
