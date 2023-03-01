import datetime

# Validates integer inputs from the user
def intValid(inputPrompt, errorMessage):
     # Loops until a valid integer has been received
     while True:
        inputInt = input(inputPrompt)
        try:
            if inputInt == "":             # Ensures a value has been entered
                print("Please ensure you enter an integer")
            else:
                return int(inputInt)     # If value is found it is returned
        except:                              # Thrown if input cannot be converted to integer
            print(f"Integer expected but not provided, {inputInt} is invalid")
            print(errorMessage)

# Validates double inputs from the user
def floatValid(inputPrompt, errorMessage):
     # Loops until a valid float has been received
     while True:
        inputFloat = input(inputPrompt)
        try:
            if inputFloat == "":             # Ensures a value has been entered
                print("Please ensure you enter an decimal")
            else:
                return float(inputFloat)     # If value is found it is returned
        except:                              # Thrown if input cannot be converted to float
            print(f"Decimal expected but not provided, {inputFloat} is invalid")
            print(errorMessage)

# Validates the string inputs by the user
def stringValid(inputPrompt, errorMessage):
    # Loops until a valid string has been received
    while True:
        inputString = input(inputPrompt)
        if inputString != "":            # Ensures a value has been entered
            return inputString 
        else: 
            print(errorMessage) 

# Validates Yes/No questions to the user
def yesNoValid(inputPrompt):
    while True:
        userChoice = stringValid(inputPrompt, "Input must be 'Y' or 'N': ")
        if userChoice == 'y' or userChoice == 'Y':
            return True
        elif userChoice == 'n' or userChoice == 'N':
            return False
        else:
            print("Invalid input. Please choose Y or N")

# Validates date inputs from the user
def dateValid(inputPrompt):
    # Loops until a valid date has been received
    while True:
        inputDate = input(inputPrompt)
        try:
            dateCheck = datetime.date.fromisoformat(inputDate)           # Ensures a value has been entered
            return dateCheck 
        except: 
            print("Date must be in format: YYYY-MM-DD") 