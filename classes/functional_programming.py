"""Example functional programming script."""
def new_employee(employees, name, salary):
    """Add a new employee."""
    employees.append([name, salary])
    return employees

def give_raise(employees, idx, amount):
    """Give an employee a raise."""
    employees[idx][1] += amount
    return employees

def view_info(employees, idx):
    """View employee info."""
    print(f"{employees[idx][0]} makes ${employees[idx][1]}")

# Add employees to array, then give them a raise
raise_amount = 10000

employees = []
name = ["Bob", "Jim"]
salary = [150000, 100000]

if isinstance(name, list):
    for i in range(len(name)):
        employees = new_employee(employees, name[i], salary[i])
else:
    employees = [name, salary]

employees = new_employee(employees, "Joe", 123000)

print(f"After ${raise_amount} raises:")
for person in range(len(employees)):
    employees = give_raise(employees, person, raise_amount)
    view_info(employees, person)
