import mysql.connector

conn = mysql.connector.connect(user='my.besmera2', password='CSCI355', host='deltona.birdnest.org', database='my_besmera2_group8')
cursor = conn.cursor()
#Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

def Insert():
    print("To insert into the table, please provide the name, date, and description of the show.")
    name = input("Enter name:")
    date = input("Enter date:") #check which format is used in DB
    description = input("Enter description:")

    sqlInsert = "INSERT INTO TVshow (name, date, description) VALUES (" + name + ", " + date + ", "+ description + ")"
    cursor.execute(sqlInsert)
    #print(sqlInsert)

    conn.commit()
    print(mycursor.rowcount, "record inserted.")

def Select():
    print("To select on the table, please provide the attribute you'd like to view or use '*' to view all")
    selection = input("Enter attribute seperated by a comma ',' :")
    
    sqlSelect = "Select" + selection + "from TVshow"
    cursor.execute(sqlSelect)
    #print(sqlSelect)

    myresult = mycursor.fetchall() #print the results
    for x in myresult:
        print(x)

def Update():
    print("To update on the table, please provide the attribute you'd like to update as well as the current value and new value.")
    attribute = input("Enter attribute:")
    curVal = input("Enter current value:")
    newVal = input("Enter new value:")

    sqlUpdate = "UPDATE TVshow SET" + attribute +" = '" + curVal+"' WHERE" + attribute + "= '" + newVal +"'"
    cursor.execute(sqlUpdate)
    #print(sqlUpdate)

    conn.commit()
    print(mycursor.rowcount, "record(s) affected.")

def Delete():
    print("To delete on the table, please provide the attribute you'd like to delete as well as its current value.")
    attribute = input("Enter attribute:")
    curVal = input("Enter current value:")

    sqlDelete = "DELETE FROM TVshow WHERE" + attribute +" = '" + curVal+"'"
    cursor.execute(sqlDelete)
    #print(sqlDelete)

    conn.commit()
    print(mycursor.rowcount, "record(s) deleted.")

action = input("What would you like to do? (insert, select, update, delete)")
if action == "insert":
    Insert()
elif action == "select":
    Select()
elif action == "update":
    Update()
elif action == "delete":
    Delete()
elif action == "exit":
    conn.close()            #Closing the connection