import pymysql
import os

def insert_customer(cursor, database):
    os.system('clear')
    try:
        record = {}
        record["uname"] = input("Enter username: ")
        record["fname"] = input("Enter First Name: ")
        record["lname"] = input("Enter Last Name: ")
        record["email"] = input("Enter email id: ")
        record["phone"] = input("Enter phone: ")
        record["dno"] = input("Enter Door Number: ")
        record["street"] = input("Enter Street: ")
        record["city"] = input("Enter City: ")
        record["state"] = input("Enter State: ")
        record["zipcode"] = input("Enter Zipcode: ")

        query = "INSERT INTO Registered_Customer VALUES('%s', '%s', '%s', '%s', '%s')" % (record["uname"], record["email"], record["phone"], record["fname"], record["lname"])

        cursor.execute(query)

        query = "INSERT INTO Registered_Customer_Shipping_Address VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (record["uname"], record["dno"], record["street"], record["city"], record["state"], record["zipcode"])

        cursor.execute(query)
        database.commit()
        print("User added.\n")
    except Exception as e:
        print("Query failed!\n")
        database.rollback()
        print(e)

def insert_delivery_provider(cursor, database):
    os.system('clear')
    try:
        record = {}
        record["cid"] = input("Enter unique CompanyID: ")
        record["name"] = input("Enter Company Name: ")
        record["email"] = input("Enter email id: ")
        record["phone"] = input("Enter phone: ")
        record["dno"] = input("Enter Door Number: ")
        record["street"] = input("Enter Street: ")
        record["city"] = input("Enter City: ")
        record["state"] = input("Enter State: ")
        record["zipcode"] = input("Enter Zipcode: ")
        record["clength"] = int(input("Enter Contract Length: "))
        record["renew"] = input("Enter Last Renewed Date (YYYY-MM-DD):  ")
        record["pay"] = int(input("Enter payment: "))
        record["nod"] = int(input("Enter number of drivers: "))

        query1 = "INSERT INTO Delivery_Provider VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (record["cid"], record["name"], record["email"], record["phone"], record["dno"], record["street"], record["city"], record["state"], record["zipcode"])

        query2 = "INSERT INTO Delivery_Provider_Contract VALUES('%s', '%d', '%s', '%d', '%d')" % (record["cid"], record["clength"], record["renew"], record["pay"], record["nod"])

        cursor.execute(query1)
        cursor.execute(query2)
        database.commit()
        print("Delivery Provider Added.\n")
    except Exception as e:
        print("Query failed!\n")
        database.rollback()
        print(e)

def insert_product(cursor):
    os.system('clear')
    try:
        record = {}
        record["pid"] = input("Enter Unique Product ID: ")
        record["price"] = input("Enter price: ")
        record["mname"] = input("Enter Model Name: ")
        record["bname"] = input("Enter Brand Name: ")
        record["stock"] = int(input("Enter stock: "))

        print("1. Laptop\n")
        print("2. Phone\n")
        print("3. Smartwatch\n")
        print("4. TV\n")
        print("5. Camera\n")
        category = input("Enter category: ")

        if category == 1:
            laptop = {}
            laptop["ssize"] = float(input("Enter screen size: "))
            laptop["sto"] = int(input("Enter storage: "))
            laptop["res"] = input("Enter resolution: ")
            laptop["ram"] = int(input("Enter RAM: "))
            laptop["gpur"] = int(input("Enter GPU RAM: "))
            laptop["gpun"] = input("Enter GPU Name: ")
            laptop["proname"] = input("Enter Processor Name: ")
            laptop["proco"] = int(input("Enter Number of Processor Cores: "))
            laptop["prosp"] = float(input("Enter Processor Speed: "))

            ports = {}
            ports = (input("Enter space seperated ports: ")).split(' ')
    except:
        print("Not done.")

def handle_insert(cursor, database):
    os.system('clear')
    print("1. Insert registration of customer.\n")
    print("2. Insert new delivery provider.\n")
    print("3. Insert new product.\n")
    print("Enter 0 to return.\n")

    i_choice = int(input("Enter your choice: "))
    if i_choice == 0:
        return
    elif i_choice == 1:
        insert_customer(cursor, database)
    elif i_choice == 2:
        insert_delivery_provider(cursor, database)
#elif i_choice == 3:
#insert_product(cursor)

    temp = input("Press any key to continue...")
