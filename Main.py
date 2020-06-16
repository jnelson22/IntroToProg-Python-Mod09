# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# JNelson, 2020-06-14,Added main body script
# JNelson, 2020-16-14, Add some error handeling
# Jnelson, 2020-06-15, Add comment and cleaned up formatting
# ------------------------------------------------------------------------ #
# TODO: Import Modules
# Import Modules
if __name__ == "__main__": # Check to make sure this is the main program
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as eIO
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
else:
    raise Exception("This file was not created to be imported")

# Data
strFileName = "EmployeeData.txt"  # File to store user input data
lstOfEmployeeObjects = []  # List of employee objects
strChoice = ""  # Captures the user option selection


# Main Body of Script  ---------------------------------------------------- #
#
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #

# Read in current file and build a list of objects
lstFileData = Fp.read_data_from_file(strFileName)
lstOfEmployeeObjects.clear()
for line in lstFileData:
    lstOfEmployeeObjects.append(Emp(line[0], line[1], line[2].strip()))

while(True):
    eIO.print_menu_items() # show user the menu
    strChoice = eIO.input_menu_options()

    # Process user's menu choice
    if strChoice.strip() == '1':  # Show Current list of products
        eIO.print_current_list_items(lstOfEmployeeObjects)
        continue  # to show the menu

    elif strChoice == '2':  # Add new employee data
        try:
            lstOfEmployeeObjects.append(eIO.input_employee_data())
        except Exception as e:
            raise print(e)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        Fp.save_data_to_file(strFileName, lstOfEmployeeObjects)
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit