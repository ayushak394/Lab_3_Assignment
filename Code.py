class Emp:
    def __init__(self, EMPID, name, age, salary):
        self.EMPID = EMPID
        self.name = name
        self.age = age
        self.salary = salary

class EmpDB:
    def __init__(self):
        self.emp = []

    def add_emp(self, empl):
        self.emp.append(empl)

    def s_age(self, age):
        result = []
        for employee in self.emp:
            if employee.age == age:
                result.append(employee)
        return result

    def s_name(self, name):
        result = []
        for employee in self.emp:
            if employee.name == name:
                result.append(employee)
        return result

    def s_salary(self, operat, salary):
        result = []
        for employee in self.emp:
            if operat == ">" and employee.salary > salary:
                result.append(employee)
            elif operat == "<" and employee.salary < salary:
                result.append(employee)
            elif operat == ">=" and employee.salary >= salary:
                result.append(employee)
            elif operat == "<=" and employee.salary <= salary:
                result.append(employee)
        return result

    def print_d(self, employees):
        if not employees:
            print("Your selected record was not found")
        else:
            for employee in employees:
                print(f"Employee ID: {employee.EMPID}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

if __name__ == "__main__":

    DatB = EmpDB()

    DatB.add_emp(Emp("161E90", "Raman", 41, 56000))
    DatB.add_emp(Emp("161F91", "Himadri", 38, 67500))
    DatB.add_emp(Emp("161F99", "Jaya", 51, 82100))
    DatB.add_emp(Emp("171E20", "Tejas", 30, 55000))
    DatB.add_emp(Emp("171G30", "Ajay", 45, 44000))

    print("Which Parameter would you like to access:")
    print("1. Employee Age")
    print("2. Employee Name")
    print("3. Employee Salary")
    ch = input("Input your Choice in either 1/2/3: ")

    if ch == "1":
        age = int(input("Enter the age that you would like to search: "))
        result = DatB.s_age(age)
    elif ch == "2":
        name = input("Enter the name you would like to search: ")
        result = DatB.s_name(name)
    elif ch == "3":
        operat = input("Choose one of the following operators: (>, <, >=, <=): ")
        salary = int(input(" Enter the salary you would like to search for: "))
        result = DatB.s_salary(operat, salary)
    else:
        print("Your choice is invalid.")
        result = []

    DatB.print_d(result)
