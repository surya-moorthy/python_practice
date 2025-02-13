from EmployeeManager import employeeManager

class employeeFrontend:
    def __init__(self):
        self.Employee_list = employeeManager()

    def run(self):
        while True:
            print("Welcome!")
            print("these are the options on managing employees:")
            print("1.Add Employee\n2.Delete Employee\n3.List all the Employees\n4.find an Employee\n5.Update Employee Information\n6.Exit")
            choice = int(input("Enter your choice:"))

            match choice:
                case 1:
                    self.Employee_list.add_emp()
                case 2:
                    self.Employee_list.del_emp()
                case 3:
                    self.Employee_list.list_emps()
                case 4:
                    self.Employee_list.find_emp()
                case 5:
                    self.Employee_list.upt_emp()
                case 6:
                    exit()
                    break
                
            
