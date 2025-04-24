import mysql.connector as m1
def ALL():
    print('1.Adding Customer')
    print('2.Grnerate the bill')
    print('3.Fetch Single Customer Data')
    print('4.Fetch All Customer Record')
    print('5.Count Number of Customers')
    print('6.Group Customer by area')
    print('7.Check the status of SIM (blocked/unblocked)')
    print('8.Blocking SIM')
    print('9.Updating balance information')
    print('10.Average balance of customer')
    print('11.Exit')
# Connect to the MySQL database
conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
cursor = conn.cursor()

#ADDING CUSTOMER
def add_customer():
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Get customer data from the user
        customer_id = input("Enter Customer ID")
        sim_no=int(input("enter the phone number"))
        balance = float(input("Enter Balance: "))
        card_status = input("Enter Card Status: ")
        purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
        address = input("Enter Address: ")            
        # Insert the new customer into the database
        insert_query = "INSERT INTO customer (customer_id,sim_no, balance, card_status, purchase_date, address) VALUES (%s, %s, %s, %s, %s, %s)"
        customer_data = (customer_id,sim_no, balance, card_status, purchase_date, address)
        cursor.execute(insert_query,customer_data)
        conn.commit()
        print("Customer added successfully!")
    except:
        print("Record can't be added")
#GENERATING BILL
def generate_bill(customer_id):
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        x=100.00
        c=9/100*x
        U=x+2*c
        # Fetch customer details
        cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
        customer = cursor.fetchone()

        if customer:
            print("Customer ID:", customer[0])
            print("SIM No:", customer[1])
            print("Balance:", customer[2])
            print("Purchase Date:", customer[4])
            print("Address:", customer[5])
            print("Purchase Amount :",x)
            print("cgst@9%",c)
            print("sgst@9%",c)
            print("Total Amount:",U)
        else:
            print("Customer not found!")

    except:
        print("error")
        
#FETCHING ONE CUSTOMER DATA
def fetch1(customer_id):
    
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Fetch customer details
        cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
        customer = cursor.fetchone()

        if customer:
            print("Customer ID:", customer[0])#st1
            print("SIM No:", customer[1])
            print("Balance:", customer[2])
            print("Card Status:", customer[3])
            print("Purchase Date:", customer[4])
            print("Address:", customer[5])#st6
        else:
            print("Customer not found!")

    except:
        print("error")
#FETCH ALL CUSTOMER DATA
def fetch_all_customer_data():
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Fetch all customer details
        cursor.execute("SELECT * FROM customer")
        customer = cursor.fetchall()

        if customer:
            print("\nCustomer Data:")
            for customers in customer:
                print("\nCustomer ID:", customers[0])
                print("SIM No:", customers[1])
                print("Balance:", customers[2])
                print("Card Status:", customers[3])
                print("Purchase Date:", customers[4])
                print("Address:", customers[5])
        else:
            print("No customers found!")

    except:
        print("error")
#COUNT NO. OF CUSTOMER DATA    
def count_customers():
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Count the number of customers
        cursor.execute("SELECT COUNT(*) FROM customer")
        count = cursor.fetchone()[0]
        print("Total Number of Customers: ",count)
    except:
        print("error")
#GROUPING AREA WISE
def group_customers_by_area():
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Group customers by area and count them
        cursor.execute("SELECT address, COUNT(*) FROM customer GROUP BY address")
        grouped_data = cursor.fetchall()

        if grouped_data:
            print("\nCustomer Count by Area:")
            for area, count in grouped_data:
                print("Area: ",area, "Count:" ,count)
        else:
            print("No customers found!")
    except:
        print("error")
#CHECKING SIM STATUS
def check_sim_status(customer_id):
    try:
        
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Fetch the SIM status for the specified customer
        cursor.execute("SELECT card_status FROM customer WHERE customer_id = %s", (customer_id,))
        sim_status = cursor.fetchone()
        if sim_status:
            print(f"\nSIM Status for Customer ID {customer_id}: {sim_status[0]}")
        else:
            print(f"Customer with ID {customer_id} not found!")
    except:
        print("error")

def update_sim_status(customer_id, new_status):
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Update the SIM status for the specified customer
        update_query = "UPDATE customer SET card_status = %s WHERE customer_id = %s"
        cursor.execute(update_query, (new_status, customer_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"\nSIM Status for Customer ID {customer_id} updated to {new_status}")
        else:
            print(f"Customer with ID {customer_id} not found!")
    except:
        print("error")
    conn.close()
def update_balance(customer_id, new_status):
    try:
        conn = m1.connect(host="localhost",user="root",password="TIGER",database="sim_company")
        cursor = conn.cursor()
        # Update the SIM status for the specified customer
        update_query = "UPDATE customer SET balance = %s WHERE customer_id = %s"
        cursor.execute(update_query, (new_status, customer_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"\nSIM Status for Customer ID {customer_id} updated to {new_status}")
        else:
            print(f"Customer with ID {customer_id} not found!")
    except:
        print("error")
    conn.close()
def calculate_average_balance():
    try:
        # Calculate the average balance of all customers
        cursor.execute("SELECT AVG(balance) FROM customer")
        average_balance = cursor.fetchone()[0]

        if average_balance is not None:
            print(f"\nAverage Balance of All Customer: {average_balance:.2f}")
        else:
            print("No customers found!")

    except:
        print("error")

    
#main
FF="Y"
while (FF=='Y'):
    ALL()
    a=int(input("Enter your choice"))
    if (a==1):
        add_customer()
    elif (a==2):
        cs=input("enter the customer id")
        generate_bill(cs)
    elif(a==3):
        cs=input("enter the customer id")
        fetch1(cs)
    elif(a==4):
        fetch_all_customer_data()
    elif(a==5):
        count_customers()
    elif(a==6):
        group_customers_by_area()
    elif(a==7):
        cs=input("enter the customer id")
        check_sim_status(cs)
    elif(a==8):
        cs=input("enter the customer id")
        ns=input("enter new status")
        update_sim_status(cs,ns)
    elif(a==9):
        cs=input("enter the customer id")
        ns=input("enter BALANCE")
        update_balance(cs,ns)
    elif (a==10):
        calculate_average_balance()
    elif (a==11):
        print("Exiting the program.")
        break
    else:
        print("Invalid Syntax")
    FF=input("to be continued in menu press Y")   
