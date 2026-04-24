class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount_withdraw, description =''):
        if not self.check_funds(amount_withdraw):
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        return True

    def get_balance(self):
        current_money = 0
        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value
        return current_money

    def transfer(self, amount_transfer, destination):        
        if not self.check_funds(amount_transfer):
            print(f"Cannot transfer amount {amount_transfer} because the balance is insufficient.\n")
            return False
        
        description = f"Transfer to {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        description = f"Transfer from {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        return True
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        text_lines = [f"{self.name:*^30}"]
        
        for entry in self.ledger:
            description_text = entry['description'][:23]
            amount_value = entry['amount']

            text_lines.append(f"{description_text:<23}{amount_value:>7.2f}")
            
        text_lines.append(f"Total: {self.get_balance():.2f}")
            
        return "\n".join(text_lines)

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent -= item["amount"]
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)

    percentages = []
    for amount in spent_amounts:
        if total_spent > 0:
            percent = int((amount / total_spent) * 100)
            percentages.append(percent - (percent % 10))
        else:
            percentages.append(0)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = 0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart


# ------------------------------ Boundary ------------------------------
# My way of slowly thinking a solution for this problem
print(f"\n\n{'='*5} Practice or Experiment {'='*5}")

list_of_dict = [{
    'money': 10000,
    'description': "first data item"
}]

print('\n')
print(list_of_dict)
print('\n')
list_of_dict.append({
    'money2': 10000,
    'description': "second data item"
})
print(list_of_dict)

# How can the amount in the first data item be reduced?
# The initial idea is to focus on the first list index before updating its value.
print('\n')
print(list_of_dict[0])
print('\n')


# Example using only one dictionary.
sample_dictionary = {
    'name' : 'Muhammad Zaenal Abidin Abdurrahman',
    'money': 20000
}
print(sample_dictionary['money'])

print('\n')
print(list_of_dict[0]['money']) # i could do this i guess?

# can you do like subtraction?
list_of_dict[0]['money'] -= list_of_dict[0]['money']
print(list_of_dict[0]['money']) # hmm interesting, idk i feel like this the approach u know 

# so the class Category the method of deposit and withdraw should be have something that can connect each other u know. But how?? Let see


print(f"\n\n{'-'*10} first experiment {'-'*10}\n")

class CategoryExperimentOne:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": amount, "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}")
    
    def withdraw(self, amount_withdraw, description =''):
        print(f"'amount withdraw': {amount_withdraw}, 'description': {description}")
        self.ledger[0]['amount'] -= amount_withdraw


    def __str__(self):
        return f"Current data details: {self.ledger}"

drink = CategoryExperimentOne("Milk")
drink.deposit(100000)
drink.withdraw(50000)
print(drink)

# It is works but idk feels weird, there should be a better solution


print(f"\n\n{'-'*10} second experiment {'-'*10}\n")
class ImprovedCategoryExperiment:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": amount, "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}")
    
    def withdraw(self, amount_withdraw, description =''):
        self.ledger.append({"amount": -amount_withdraw, "description": description})

        print(f"'amount withdraw': {-amount_withdraw}, 'description': {description}")


    def __str__(self):
        return f"\nCurrent data details: {self.ledger}"

drink2 = ImprovedCategoryExperiment("Milk")
drink2.deposit(100000, 'initial deposit')
drink2.withdraw(50000, 'buy milk')
print(drink2)

# The ledger keeps the transaction history, so balance calculations can focus on entries with the "amount" key.


print(f"\n\n{'-'*10} third experiment {'-'*10}\n")
class ImprovedCategoryExperimentWithTransfer:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        print(f"Deposit process for {self.name} is running...")
        self.ledger.append({"amount": float(amount), "description": description})
        print(f"'amount deposit': {amount}, 'description': {description}\n")
    
    def withdraw(self, amount_withdraw, description =''):
        print(f"Withdrawal process for {self.name} is running...")
        if not self.check_funds(amount_withdraw):
            print(f"Cannot withdraw amount {amount_withdraw} because the balance is insufficient.\n")
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        print(f"'amount withdraw': {-amount_withdraw}, 'description': {description}")
        print(f"Withdrawal completed successfully\n")
        return True

    def get_balance(self):
        current_money = 0

        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value

        print(f"Current balance for {self.name}: {current_money}")
        return current_money

    def transfer(self, amount_transfer, destination):
        print(f"Transfer process from {self.name} to {destination.name} is running...")
        
        # Transfer from one category to another requires balance checks and ledger updates for both categories.
        if not self.check_funds(amount_transfer):
            print(f"Cannot transfer amount {amount_transfer} because the balance is insufficient.\n")
            return False
            
        # After validation, update both category ledgers.
        
        # Subtract the transferred balance from the source category.
        description = f"Transfer money to category {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        # Add the received balance to the destination category.
        description = f"Receive money from category {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        
        print(f"Transfer from {self.name} to {destination.name} with amount: {amount_transfer}")
        print(f"Transfer completed successfully\n")
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        print(f"{f'{self.name}':*^30}")
        for description_text, amount_value in [(entry['description'], entry['amount']) for entry in self.ledger]:
            print(f"{description_text[:23]:<23}{amount_value:>7.2f}")
        print(f"")
        return f"Current data details: {self.ledger}\n"


drink3 = ImprovedCategoryExperimentWithTransfer("Milk")
drink3.deposit(100000, 'Initial deposit')
drink3.withdraw(20000, 'buy')
drink3.get_balance()
print()
print(drink3)


food3 = ImprovedCategoryExperimentWithTransfer("Food")
food3.deposit(200000, "Initial deposit")
food3.get_balance()
print()
food3.transfer(50000, drink3)
food3.get_balance()
print()
drink3.get_balance()
print()
print(drink3)
print()
print(food3)


# This is the final version of the code, written as cleanly as possible for this exercise.
print(f"\n\n{'-'*10} fourth experiment {'-'*10}\n")
class CategoryBestPractice:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description =''):
        self.ledger.append({"amount": float(amount), "description": description})
    
    def withdraw(self, amount_withdraw, description =''):
        if not self.check_funds(amount_withdraw):
            return False
        
        self.ledger.append({"amount": float(-amount_withdraw), "description": description})
        return True

    def get_balance(self):
        current_money = 0
        # This is kind of not the best way, but it's okay
        for dictionary in self.ledger:
            for value in dictionary.values():
                if isinstance(value, float):
                    current_money += value
        return current_money

    def transfer(self, amount_transfer, destination):        
        if not self.check_funds(amount_transfer):
            print(f"Cannot transfer amount {amount_transfer} because the balance is insufficient.\n")
            return False
        
        # Both can use the method of withdraw and desposit (DRY), but it is okay
        description = f"Transfer to {destination.name}"
        self.ledger.append({"amount": float(-amount_transfer), "description": description})
        
        description = f"Transfer from {self.name}"
        destination.ledger.append({"amount": float(amount_transfer), "description": description})
        
        return True
        
    def check_funds(self, amount):
        current_money = self.get_balance()
        if amount > current_money:
            return False
        return True

    def __str__(self):
        # Build a list of output lines, starting with the title.
        text_lines = [f"{self.name:*^30}"]
        
        # Format each ledger entry into a fixed-width text line.
        for entry in self.ledger:
            description_text = entry['description'][:23]
            amount_value = entry['amount']
            
            # Add the formatted result to the output list.
            text_lines.append(f"{description_text:<23}{amount_value:>7.2f}")
            
        text_lines.append(f"Total: {self.get_balance():.2f}")
            
        # Join all output lines with newline characters.
        return "\n".join(text_lines)

food_category = CategoryBestPractice('Food')
food_category.deposit(1000, 'initial deposit')
food_category.withdraw(10.15, 'groceries')
food_category.withdraw(15.89, 'restaurant and more food for dessert')
clothing = CategoryBestPractice('Clothing')
food_category.transfer(50, clothing)
print(food_category)
