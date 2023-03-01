# Employee and payroll program

## Setup

* Download payroll.py/ functions.py/ validations.py
* Place all files in the same folder.

## Database setup

1. Table 1:
    * Name: employee
    * Columns: empID, firstName, surname, address, email, mobile, startDate, endDate
    * Types: INT, VARCHAR, VARCHAR, VARCHAR, VARCHAR, VARCHAR, DATETIME, DATETIME
2. Table 2:
    * Name: payroll
    * Columns: payID, empID(from employee table), hoursWorked, rateOfPay, taxRate, dateCreated
    * Types: INT, INT, INT, DECIMAL, DECIMAL, DATETIME

## To Run

Run payroll.py
