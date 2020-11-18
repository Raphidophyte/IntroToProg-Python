# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JHerndon,11/16/2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# File to List
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstTask, lstPriority = row.split(",")
    dicRow = {"Task": lstTask[0], "Priority": lstPriority[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", 'r')
#        for row in lstTable:
#            lstRow = row.split(",")
#            dicRow = {"strTask": lstRow[0], "strPriority": lstRow[1]}
#            print(dicRow.keys())
        print(objFile.read())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        print("Enter a 'Task' and 'Priority' for your ToDo List")
        lstTask = input("Enter a 'Task': ")
        lstPriority = input("Enter a 'Priority' (high, medium or low): ")
        lstRow = [lstTask, lstPriority]
#        lstRow = (dicRow.split(","))
        dicRow = {"Task": lstTask[0], "," "Priority": lstRow[1]}
        lstTable.append(dicRow)
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
#        strRem = input("Which item should be removed?: ")
#       for row in lstTable:
#          if row["lstTask"].lower() == strRem.lower():
#                lstTable.remove(row)
#                print(strRem, "has been removed")
#            else:
                print("Task not in file")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(lstTask + "," + lstPriority + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Goodbye")
        break  # and Exit the program
