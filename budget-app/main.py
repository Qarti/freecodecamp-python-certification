class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({'amount': -1 * amount, 'description': description})

        return True
    
    def get_balance(self):
        result = 0

        for item in self.ledger:
            result += item["amount"]

        return result

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        # Withdraws the amount of this instance
        self.withdraw(amount, f"Transfer to {category.name}")

        # Deposits the amount into the other category
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if self.ledger[0]["amount"] - amount < 0:
            return False
        
        return True

    def __str__(self):
        stars = "*" * int((30 - len(self.name)) / 2)

        text = f"{stars}{self.name}{stars}"

        for item in self.ledger:
            desc = item["description"][0:23]
            text += f"\n{desc}{' ' * (24 - len(desc))}{item['amount']:.2f}"
            pass

        text += f"\nTotal: {self.get_balance()}"
        return text
        

def create_spend_chart(categories):
    dot = "o"
    chart = ""
    title = "Percentage spent by category\n"
    
    spent_by_category = []

    for category in categories:
        counter = 0
        for value in category.ledger:
            if value["amount"] < 0:
                counter += value["amount"] * - 1
        spent_by_category.append(round(counter, 2))

    total_spent = sum(spent_by_category)

    spent_by_category = list(map(lambda x: int(((x/total_spent)*100) // 10) * 10 , spent_by_category))

    y_axis_labels = [str(x) for x in range(100, -10, -10)]

    categories_names = [category.name for category in categories]
    max_name = len(max(categories_names, key=len))

    x_axis_labels = [f"{name}{' ' * (max_name - len(name))}" for name in categories_names]


    matrix = [f"{' ' * (11 - len(dot * (perc//10 + 1)))}{dot * (perc//10 + 1)}" for perc in spent_by_category]

    


    chart += title

    for i in range(11):
        chart += f"{' ' * (3 - len(y_axis_labels[i]))}{y_axis_labels[i]}| "
        for j in range(len(matrix)):
            chart += f"{matrix[j][i]}  "
        chart += "\n"

    chart += f"    -{'---' * len(matrix)}"

    
    for i in range(max_name):
        chart +="\n     "
        for j in range(len(x_axis_labels)):
            chart += f"{x_axis_labels[j][i]}  "
        #chart += "\n"
        


    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

categories = [food]
print(create_spend_chart(categories))
