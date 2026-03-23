class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

    def display(self):
        print(f"Name: {self.name} | Salary: {self.get_salary()}")

    def __str__(self):
        return f"Employee: {self.name} | Salary: {self.base_salary}"


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus

    def display_team(self, team_list):
        print(f"Team under {self.name}:")
        for member in team_list:
            if isinstance(member, Employee):
                print(f"  * {member.name}")
            else:
                print(f"  * {member}")

    def __str__(self):
        return f"Manager: {self.name} | Total Salary: {self.get_salary()}"


class Intern(Employee):
    def __init__(self, name, base_salary, duration_months):
        super().__init__(name, base_salary)
        self.duration = duration_months

    def get_salary(self):
        return self.base_salary * 0.5

    def time_left(self, months_done):
        remaining = max(0, self.duration - months_done)
        print(f"{self.name} has {remaining} months remaining")

    def __str__(self):
        return f"Intern: {self.name} | Duration: {self.duration} months"


if __name__ == "__main__":
    m = Manager("Sara", base_salary=80000, bonus=20000)
    i = Intern("Ali", base_salary=30000, duration_months=6)

    print(m.get_salary())    # 100000
    print(i.get_salary())    # 15000.0

    m.display()
    i.display()

    print(m)
    print(i)

    m.display_team(["Noman", "Ahmed", "Zara"])
    i.time_left(2)