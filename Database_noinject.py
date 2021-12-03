def Action():
    action = raw_input("What would you like to do? (insert, select, update, delete, or exit)")
    if action == "insert":
        Insert()
    elif action == "select":
        Select()
    elif action == "update":
        Update()
    elif action == "delete":
        Delete()
    elif action == "exit":
        conn.close()   

def Insert(): #is working correctly - no sql injection
    print("To insert into the table, please provide the name, year released (YYYY-MM-DD), and description of the show.")
    name = raw_input("Enter name:")
    date = raw_input("Enter year released (YYYY-MM-DD):")
    description = raw_input("Enter description:")

    #sqlInsert = "INSERT INTO TVshow (name, date, description) VALUES (%s, %s, %s)"
    #val = (name, date, description)
    #print(sqlInsert, val)
    cursor.execute("INSERT INTO TVshow (name, yearReleased, description) VALUES (%(name)s , %(date)s, %(description)s)", {'name':name, 'date':date, 'description': description})
    
    conn.commit()
    print(cursor.rowcount, "record inserted.")
    Action()

def Select(): #dont know if sql injection prevention is needed here - it errors each time i've tried to inject sql
    print("To select on the table, please provide the attribute you'd like to view or use '*' to view all")
    selection = raw_input("Enter attribute seperated by a comma ',' :")
    
    sqlSelect = "Select " + selection + " from TVshow"
    cursor.execute(sqlSelect)
    #print(sqlSelect)

    myresult = cursor.fetchall() #print the results
    for x in myresult:
        print(x)
    
    Action()

def Update(): # gotta work on the .execute string parsing - something seems to be different from the insert verison 
    print("To update on the table, please provide the attribute you'd like to update as well as the current value and new value.")
    attribute = raw_input("Enter attribute:")
    id = raw_input("Enter the row id:")
    newVal = raw_input("Enter new value:")

    #sqlUpdate = "UPDATE TVshow SET " + attribute +" = '" + newVal+"' WHERE id = '" + id +"'"
    cursor.execute("UPDATE TVshow SET %(attribute)s =  %(newVal)s WHERE id = %(id)s", {'attribute': attribute, 'newVal': newVal, 'id':id})
    #print(sqlUpdate)

    conn.commit()
    print(cursor.rowcount, "record(s) affected.")
    Action()

def Delete(): # sql injection - todo havent messed with it yet
    print("To delete on the table, please provide the attribute you'd like to delete as well as its current value.")
    attribute = raw_input("Enter attribute:")
    curVal = raw_input("Enter current value:")

    sqlDelete = "DELETE FROM TVshow WHERE " + attribute +" = '" + curVal+"'"
    cursor.execute(sqlDelete)
    #print(sqlDelete)

    conn.commit()
    print(cursor.rowcount, "record(s) deleted.")
    Action()        

import mysql.connector

conn = mysql.connector.connect(user='my.besmera2', password='CSCI355', host='deltona.birdnest.org', database='my_besmera2_group8')
cursor = conn.cursor()
#Fetch a single row using fetchone() method.
data = cursor.fetchone()
if conn.is_connected():
    print("Connection established")
else: 
    print("Connection failed")

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

Action()