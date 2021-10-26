"""Example object-oriented programming script."""
class Employee:
    """Class containing employee info."""
    def __init__(self, name, salary):
        self.name = [] 
        self.salary = [] 
        if isinstance(name, list):
            for i in range(len(name)):
                self.name.append(name[i])
                self.salary.append(salary[i])
        else:
            self.name.append(name)
            self.salary.append(salary)

    def __len__(self):
        """Make iterable by defining the length."""
        return len(self.name)

    def new_employee(self, name, salary):
        """Add a new employee."""
        self.name.append(name)
        self.salary.append(salary)

    def give_raise(self, idx, amount):
        """Give an employee a raise."""
        self.salary[idx] += amount

    def view_info(self, idx):
        """View employee info."""
        print(f"{self.name[idx]} makes ${self.salary[idx]}")

# Add employees to object, then give them a raise
raise_amount = 10000

employees = Employee(["Bob", "Jim"], [150000, 100000])
employees.new_employee("Joe", 123000)

print(f"After ${raise_amount} raises:")
for person in range(len(employees)):
    employees.give_raise(person, raise_amount)
    employees.view_info(person)
