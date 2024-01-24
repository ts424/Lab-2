class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employees(employees, sort_key):
    if sort_key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return employees


def main():
    # Creating instances for each employee in the provided table
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    # Get the sorting parameter from the user
    sort_param = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))

    # Sort the employees based on the chosen parameter
    sorted_employees = sort_employees(employees, sort_param)

    # Print the sorted data
    print("Sorted Employee Table:")
    print("Employee ID Name Age Salary(PM)")
    for emp in sorted_employees:
        print(emp)


if __name__ == "__main__":
    main()
