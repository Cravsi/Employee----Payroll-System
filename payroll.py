import functions as f

option = 0

f.welcomeMessage()
# Displays menu to user
while option != 8:
    option = f.displayMenu()
    if option == 1:
        f.viewEmployeeDetails()
    elif option == 2:
        f.addEmployee()
    elif option == 3:
        f.changeEmployeeDetails()
    elif option == 4:
        f.deleteEmployee()
    elif option == 5:
        f.enterPayrollDetails()
    elif option == 6:
        f.reports()
    elif option == 7:
        f.exportToExcel()

f.exitMessage()