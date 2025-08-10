class emp_salary :
    def __init__(self, emp, salary):
        self.emp=emp
        self.salary=salary

    def show_emp(self):
        print("ชื่อพนักงาน: ", self.emp)

    def show_salary(self):
        print("เงินเดือน: ",self.salary)

emp_1 = emp_salary("สายชล","18,500")
emp_2 = emp_salary("ปิง","19,000")
emp_3 = emp_salary("นทกร","18,000")

print("show name and salary:")
emp_1.show_emp()
emp_1.show_salary()

emp_2.show_emp()
emp_2.show_salary()

emp_3.show_emp()
emp_3.show_salary()