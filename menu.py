import pymysql
import os
from insertion import *
from updation import *
from deletion import *
from dept_sum import *
from minmax import *

os.system('clear')
#username = input("Enter your username: ")
#password = input("Enter your password: ")

try:
    database = pymysql.connect("localhost", "murali", "Murali-2001", "dna")
    cursor = database.cursor()

    while 1:
        os.system('clear')
        print("1. Insert a record.\n")
        print("2. Update a record.\n")
        print("3. Delete a record.\n")
        print("4. Aggregate Salary by Department.\n")
        print("5. Cheapest Product of a certain type. \n")
        print("6. Most expensive Product of a certain type. \n")
        print("Enter 0 to exit.\n")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            database.close()
            break
        elif choice == 1:
            handle_insert(cursor, database)
        elif choice == 2:
            handle_update(cursor, database)
        elif choice == 3:
            handle_delete(cursor, database)
        elif choice == 4:
            dept_sum(cursor, database)
        elif choice == 5:
        	cost_min(cursor, database)
        elif choice == 6:
        	cost_max(cursor, database)

except Exception as e:
    print(e)

