from Employee import employee

class employeeManager:
    def __init__(self):
        self.employee = []
        self.emp_count = 0
    def add_emp(self):
        name = input("Enter name of the employee to add:")
        id = input("Enter id of the employee:")
        age = int(input("Enter age of the employee:"))
        salary =  int(input("Enter salary of the employee:"))
        self.employee.append(employee(name,id,age,salary))
        self.emp_count += 1 
    def del_emp(self):
        emps = self.employee 
        id = input("Enter id of the employee to delete:")
        if self.emp_count == 0:
             print("No employees are added")
             
        for emp in emps:
            if emp.id ==  id:
                emps.remove(emp)
                print(f"Employee with id {emp.id} has been deleted")
                break
    def list_emps(self):
        if self.employee.__len__() == 0:
            print("No employees are added") 
        for emp in self.employee:
            print(emp)

    def find_emp(self):
        id = input("Enter id of the employee to find:")
        for emp in self.employee:
            if emp.id == id:
                print(emp)
    
    def upt_emp(self):
        id = int(input("Enter the id of that employee:"))
        upt_info = input("Enter which one you want to update:")
        upt = input(f"Enter updated {upt_info} of that employee")
        for emp in self.employee:
            if emp.id == id:
                if upt_info == "name":
                    emp.name = upt
                    break
                elif upt_info == "age":
                    emp.age = upt
                    break
                elif upt_info == "salary":
                    emp.salary = upt
                    break
                else:
                    print("No such information")
                    return
        return 
                
       

