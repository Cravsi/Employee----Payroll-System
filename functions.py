import mysql.connector
import validations as val
from datetime import date

# Global Variables
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "mydb"
)

# Displays welcome message when applications opens
def welcomeMessage():
    print("\nHello & Welcome!")

def exitMessage():
    print("\nSee you next time!")

# Count the count of rows returned by SQL statement
def countRows(myCommand):
    myDataSet = db.cursor()
    myDataSet.execute(myCommand)
    count = myDataSet.fetchall()
    myDataSet.close()
    
    return len(count)

def getEmployeeName(empID):
    # Retrieve employee's name
    myCommand = f"SELECT firstName, surname FROM employee WHERE empID = {empID};"

    # Retrieves employee's name from database
    try:                               
        myDataSet = db.cursor()
        myDataSet.execute(myCommand)
        
        for x in myDataSet:
            empName = x[0] + " " + x[1]
        myDataSet.close()

        return empName
                                
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")     

# Displays Menu to the user and retrieves menu choice
def displayMenu():
    # Loops until a valid menu choice has been received from the user
    while True:
            option = 0
            print("\nPlease choose one from the menu below!")
            print("1 = View Employee Details")
            print("2 = Add an Employee")
            print("3 = Change Employee Details")
            print("4 = Delete an Employee")
            print("5 = Enter Payroll Details")
            print("6 = Employee Summary Report")
            print("7 = Export Employee & Payroll Data to Excel")
            print("8 = Exit")
            option = val.intValid("\nPlease enter the menu item number: ", "Please enter a valid integer")

            # Ensures the menu choice from the user is valid
            if option not in range (1, 9):
                print(f"\n{option} is not a menu option")
            else:
                return option

# Displays an employee's details to the user from their ID            
def displayDetails(empID):

    # SQL Command
    myCommand = f"SELECT firstName, surname, address, email, mobile, startDate, endDate FROM employee WHERE empID = {str(empID)};"

    # Retrieves employee details from database
    try:                        
        count = countRows(myCommand) # countRows() prints "func 1"
                    
        if count != 0:
            
            myDataSet = db.cursor()
            myDataSet.execute(myCommand)
            
            for x in myDataSet:
                empFirstName = x[0]
                empSurname = x[1]
                empAddress = x[2]
                empEmail = x[3]
                empMobile = x[4]
                endDate = x[5]
                startDate =  x[6]

                print("\nEmployee " + str(empID) + "'s details: ")
                print("\tName: \t\t" + empFirstName + " " + empSurname)
                print("\tAddress: \t" + empAddress)
                print("\tMobile: \t" + empMobile)
                print("\tEmail: \t\t" + empEmail)
                print("\tStart Date: \t" + str(startDate))
                print("\tEnd Date: \t" + str(endDate))
            myDataSet.close()
            
        else:
            print(f"Employee ID {empID} does not exist")
                                
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
            
# Menu option 1 - User can view employee's details
def viewEmployeeDetails():
    loopAgain = True

    # Loops until users chooses to exit
    while loopAgain:
        # Retrieves employee number from the user
        empID = val.intValid("\nPlease provide an employee number: ", "That employee number was invalid, please try again: ")

        displayDetails(empID)

        # Ask if user would like to search for another user
        loopAgain = val.yesNoValid("\nWould you like to search for another employee? [Y/N]: ")

# User inputs details
def confirmDetails():
    details = []

    while True:
        # Retrieves employee number from the user
        details.append(val.stringValid("Please enter their first name: ", "You must enter a first name: "))
        details.append(val.stringValid("Please enter their last name: ", "You must enter a last name: "))
        details.append(val.stringValid("Please enter their home address: ", "You must enter an address: "))
        details.append(val.stringValid("Please enter their email address: ", "You must enter an email: "))
        details.append(val.stringValid("Please enter their mobile number: ", "You must enter a number: "))
        details.append(val.dateValid("Please enter their start date: "))
        details.append(val.dateValid("Please enter their end date: "))

        # Places details list into variables
        empFirstName = details[0]
        empSurname = details[1]
        empAddress = details[2]
        empEmail = details[3]
        empMobile = details[4]
        startDate = details[5]
        endDate =  details[6]

        # Displays details to user
        print("\nPlease confirm the details entered below: ")
        print("\tName: \t\t" + empFirstName + " " + empSurname)
        print("\tAddress: \t" + empAddress)
        print("\tMobile: \t" + empMobile)
        print("\tEmail: \t\t" + empEmail)
        print("\tStart Date: \t" + str(startDate))
        print("\tEnd Date: \t" + str(endDate))

        # User will confirm if details are correct
        detailsConfirmed = val.yesNoValid("Are these details correct? [Y/N]: ")

        # Details  list returned if correct
        if detailsConfirmed:
            return details

# Menu option 2 - User submit new employee and details to table
def addEmployee():
    loopAgain = True

    # Loops until users chooses to exit
    while loopAgain:
        print("Please enter the details of the new Employee:")
        
        # Allows user to input new employee's details
        newEmployee = confirmDetails()

        empFirstName = newEmployee[0]
        empSurname = newEmployee[1]
        empAddress = newEmployee[2]
        empEmail = newEmployee[3]
        empMobile = newEmployee[4]
        startDate = newEmployee[5]
        endDate =  newEmployee[6]

        # Retrieves employee details from database
        try:
            # Open database cursor as myDataSet to store returned information from the database
            myDataSet = db.cursor()

            # Builds the SQL statement and fires it at the database
            myCommand = f"INSERT INTO employee(firstName, surname, address, email, mobile, startDate, endDate) " + \
                        f"VALUES ('{empFirstName}', '{empSurname}', '{empAddress}', '{empEmail}', '{empMobile}', '{startDate}', '{endDate}');"
            
            myDataSet.execute(myCommand)
            db.commit()
            
            myDataSet.close()

            print("\nNew Employee added to database.")

        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")

        # Ask if user would like to search for another user
        loopAgain = val.yesNoValid("Would you like to add another employee? [Y/N]: ")

# Menu option 3 - User can change details of current employees
def changeEmployeeDetails():
    loopAgain = True

    # Loops until users chooses to exit
    while loopAgain:
        # Retrieves employee number from the user
        empID = val.intValid("\nPlease provide ID of employee's details to change: ", "That employee number was invalid, please try again: ")

        displayDetails(empID)
        edit = val.yesNoValid("\nWould you like to edit this employee's details? [Y/N]: ")

        if edit:
            newDetails = confirmDetails()
            empFirstName = newDetails[0]
            empSurname = newDetails[1]
            empAddress = newDetails[2]
            empEmail = newDetails[3]
            empMobile = newDetails[4]
            startDate = newDetails[5]
            endDate =  newDetails[6]

            myCommand = ("UPDATE employee " + \
                        f"SET firstName = '{empFirstName}', surname = '{empSurname}', address = '{empAddress}', " + \
                        f"email = '{empEmail}', mobile = '{empMobile}', startDate = '{startDate}', endDate = '{endDate}' " + \
                        f"WHERE empID = {empID};")
            
            myDataSet = db.cursor()
            myDataSet.execute(myCommand)
            db.commit()
            
            myDataSet.close()

            print("Details successfully updated...")

        # Ask if user would like to search for another user
        loopAgain = val.yesNoValid("\nWould you like to edit details for another employee? [Y/N]: ")

# Menu option 4 - Deletes an employees details from the database
def deleteEmployee():
    loopAgain = True

    # Loops until users chooses to exit
    while loopAgain:

        # Retrieves employee number from the user
        empID = val.intValid("\nPlease provide ID of employee's details to delete: ", "That employee number was invalid, please try again: ")

        # Separate command needed to confirm that employee exists (DELETE does not return any rows)     
        countCommand = f"SELECT * FROM employee WHERE empID = {empID}"

        # If a matching empID is found
        if countRows(countCommand) != 0:
            displayDetails(empID)

            # User can confirm if they wish to proceed with deletion
            delete = val.yesNoValid("\nAre you sure you would like to delete this employee?\nNOTE: These changes cannot be reversed [Y/N]: ")

            if delete:
                myCommandPayrollTable = f"DELETE FROM payroll WHERE empID = {empID};"
                myCommandEmployeeTable = f"DELETE FROM employee WHERE empID = {empID};"

                # Deletes the employees details
                myDataSet = db.cursor()
                myDataSet.execute(myCommandPayrollTable)
                myDataSet.execute(myCommandEmployeeTable)
                db.commit()
                
                myDataSet.close()
                print(f"\nEmployee {empID} successfully deleted")

        # else no employee with empID is found
        else:
            print("\nThis employee ID is not associated with any current employees")

        # Ask if user would like to search for another user
        loopAgain = val.yesNoValid("\nWould you like to delete another employee? [Y/N]: ")

# Adds new payroll date to database
def addToPayroll(empID, hoursWorked, rateOfPay, taxRate, dateCreated):
    myCommand = f"INSERT INTO payroll(empID, hoursWorked, rateOfPay, taxRate, dateCreated) " + \
                f"VALUES ('{empID}', '{hoursWorked}', '{rateOfPay}', '{taxRate}', '{dateCreated}');"

    try:
        # Open database cursor as myDataSet to store returned information from the database
        myDataSet = db.cursor()
        myDataSet.execute(myCommand)
        db.commit()
        
        myDataSet.close()
        print(f"\nPayroll data for {getEmployeeName(empID)} successfully added to database")

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

# Prints employee payslip to textfile
def printEmployeePayslip(empID, hoursWorked, rateOfPay, grossPay, taxPaid, dateCreated, netPay):
    empName = getEmployeeName(empID)
    
    # Create valid path name for new file
    folder = "c:\\temp\\"
    filename = f"payslip{empName}{dateCreated}.txt"
    filename = filename.replace(" ", "")
    pathName = folder + filename

    # Write payroll details to file
    with open(pathName, "w") as file:
        file.write("Payslip\n\n")
        file.write(f"Employee Name: \t{empName}\n")
        file.write(f"Employee ID: \t{empID}\n")
        file.write(f"Date Created: \t{dateCreated}\n")
        file.write("==============================\n\n")
        file.write(f"\tHours Worked:\t{hoursWorked}\n")
        file.write(f"\tRate of Pay:\t{rateOfPay}\n")
        file.write(f"\tGross Pay:\t\t{grossPay}\n")
        file.write(f"\tTax Paid:\t\t{round(taxPaid, 2)}\n")
        file.write(f"\tNet Pay:\t\t{round(netPay, 2)}\n")

    print("\nPayslip successfully written to file.")
    print(f"File Location = {pathName}")

# Menu option 5 - Retrieves payroll information from user
def enterPayrollDetails():
    loopAgain = True

    # Loops until users chooses to exit
    while loopAgain:
        # Retrieves employee number from the user
        empID = val.intValid("\nPlease provide an employee number: ", "That employee number was invalid, please try again: ")
        
        # Separate command needed to confirm that employee exists (DELETE does not return any rows)     
        countCommand = f"SELECT * FROM employee WHERE empID = {empID}"
        
        # Checks this employee exists
        if countRows(countCommand) != 0:
            displayDetails(empID)

            editPayroll = val.yesNoValid("\nWould you like to create this employee's payroll? [Y/N]: ")

            if editPayroll:
                empName = getEmployeeName(empID)

                # Retrieve details from user
                hoursWorked = val.intValid(f"Input the hours worked by {empName}: ", "Please input a valid integer")
                rateOfPay = val.floatValid(f"Please input {empName}'s rate of pay: ", "Please input a valid number")
                taxRate = val.floatValid(f"Please input {empName}'s tax rate [i.e 0.4 for 40%]: ", "Please input a valid number")

                # Calculate tax & pay details
                grossPay = hoursWorked * rateOfPay
                taxPaid = grossPay * taxRate
                netPay = grossPay - taxPaid

                dateCreated = date.today()

                addToPayroll(empID, hoursWorked, rateOfPay, taxRate, dateCreated)

                # Prints payslip for payroll to text file
                printPayslip = val.yesNoValid("\nWould you like to print this payslip? [Y/N]: ")
                if printPayslip:
                    printEmployeePayslip(empID, hoursWorked, rateOfPay, grossPay, taxPaid, dateCreated, netPay)
        
        else:
            print("\nNo employee associated with this ID.")

        # Ask if user would like to search for another user
        loopAgain = val.yesNoValid("\nWould you like to search for another employee? [Y/N]: ")

# Menu option 6 - Writes text file containing all employees
def reports():
    folder = "c:\\temp\\"
    filename = f"Employees.txt"
    pathName = folder + filename

    # Retrieve all details from database
    myCommand = "SELECT empID, firstName, surname, address, email, mobile, startDate, endDate FROM employee;"
    myDataSet = db.cursor()
    myDataSet.execute(myCommand)

    t = "---------------"

    # Print details to report
    with open(pathName, "w") as file:
            file.write("Company Employees\n")
            file.write("==============================\n\n")
            file.write("{:<16}{:<16}{:<24}{:<24}{:<16}{:<24}{:<24}\n".format("Employee ID","Name","Address","Email","Mobile","Start Date", "End Date"))
            file.write("{:<16}{:<16}{:<24}{:<24}{:<16}{:<24}{:<24}\n".format(t,t,t,t,t,t,t))

            # Print each employee to their own row
            for x in myDataSet:
                empID = x[0]
                empFirstName = x[1]
                empSurname = x[2]
                empAddress = x[3]
                empEmail = x[4]
                empMobile = x[5]
                endDate = x[6]
                startDate =  x[7]

                empName = empFirstName + " " + empSurname

                file.write("{:<16}{:<16}{:<24}{:<24}{:<16}{:<24}{:<24}\n".format(empID, empName, empAddress, empEmail, empMobile, str(endDate), str(startDate)))

    myDataSet.close()
    print("\nEmployee summary report successfully created.")
    print(f"File location = {pathName}")
    x = input("\nPress enter to continue...")

# Menu option 7 - Export employee and payroll information to excel sheet
def exportToExcel():
    folder = "c:\\temp\\"
    filename = f"payroll.csv"
    pathName = folder + filename

    # Retrieve all details from database
    myCommand = "SELECT * FROM employee, payroll WHERE employee.empID = payroll.empID ORDER BY payroll.empID;"
    myDataSet = db.cursor()
    myDataSet.execute(myCommand)

    # Print details to CSV file
    with open(pathName, "w") as file:
            # Print each employee to their own row
            for x in myDataSet:
                empID = x[0]
                empFirstName = x[1]
                empSurname = x[2]
                empAddress = x[3]
                empEmail = x[4]
                empMobile = x[5]
                endDate = x[6]
                startDate =  x[7]
                hoursWorked =  x[8]
                rateOfPay =  x[9]
                taxRate =  x[10]
                dateCreated =  x[11]

                empName = empFirstName + " " + empSurname

                file.write("{},{},{},{},{},{},{},{},{},{},{},{}\n".format(str(empID), empFirstName, empSurname, empAddress, empEmail, empMobile, str(endDate), str(startDate), str(hoursWorked), str(rateOfPay), str(taxRate), str(dateCreated)))

    myDataSet.close()
    print("\nCSV file successfully created.")
    print(f"File location = {pathName}")
    x = input("\nPress enter to continue...")