# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as eIO
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
else:
    raise Exception("This file was not created to be imported")

# Test data module -----
try:
    objP1 = D.Person("Bob", "Smith")
    objP2 = D.Person("Sue", "Jones")
    lstTable = [objP1, objP2]
    for row in lstTable:
        print(row.to_string(), type(row))
except Exception as e:
    raise print(e)

# Test employee class -----
try:
    objP1 = Emp(1, "Bob", "Smith")
except Exception as e:
    print(e)
except Exception:
    print('Sorry Error')
    objP2 = Emp(2, "Sue", "Jones")
    lstTable = [objP1, objP2]
    for row in lstTable:
        print(row.to_string(), type(row))

# Test processing module -----
# P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
# lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
# for row in lstFileData:
#     p = D.Person(row[0], row[1])
#     print(p.to_string().strip(), type(p))

# Test Employee processing module
# Fp.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = Fp.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))



# print()
# objP2.first_name = 'Susan'
# print(objP2.first_name)

# Test IO classes
# eIO.print_menu_items()
# eIO.print_current_list_items(lstTable)
# print(eIO.input_employee_data())
# print(eIO.input_menu_options())
