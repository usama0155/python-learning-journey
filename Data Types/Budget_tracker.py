def main():
    expenses =[{'name': 'Flour', 'type': 'Grocery', 'amount': 1000},
               {'name': 'Rice', 'type': 'Grocery', 'amount':500},
               {'name': 'Bus', 'type': 'Transport', 'amount': 800}]
    print("Welcome to Budget Tracker")
    print("--------------------------")
    while True:
        choice = menu()
        if choice == 1:
            name = expense_name()
            types = expense_type()
            amount = expense_amount()
            results = store(expenses,name, types, amount)
            
        elif choice == 2:
            if len(expenses) == 0:
                print("No Expenses Yet!!!")
            else:
                for i, expense in enumerate(expenses,start=1):
                    print(f"{i}) {expense['name']} | {expense['type']} | {expense['amount']}")
                print(f"Total Items: {len(expenses)}")

        elif choice == 3:
            if len(expenses) == 0:
                print("No Expenses Yet!!!")
            else:
                total_expense = calulate_total(expenses)
                print(f"Total Expense: {total_expense}")

        elif choice == 4:
            average = calulate_average(expenses)
            print(f"Average Expense: {average:.2f}")
        elif choice == 5:
            category_wise_total(expenses)
        elif choice == 6:
            print("Exiting...")
            break

def menu():
        try:
            choice = int(input("\n1. Add Expense\n2. Show Expenses\n3. Total Expense\n4. Average Expense\n5. Category Wise Total \n6. Exit\nEnter choice: "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Enter Number From 1 - 6")
        except ValueError:
            print("Enter Valid number!")


def expense_name():
    while True:
        expense_name = input("Name of Expense: ")
        try:
            if expense_name != "":
                return expense_name
        except ValueError:
            pass
def expense_type():
        while True:
            expense_type = input("Type of Expense: ")
            try:
                if expense_type != "":
                    return expense_type
            except ValueError:
                pass
def expense_amount():
    while True:
        expense_amount = input("Enter Amount: ")
        try:
            expense_amount = int(expense_amount)
            if not expense_amount < 0:
                return expense_amount
        except ValueError:
            print("Amount Must be Positive Digit")
            pass
def store(expenses,name, types, amount):
    expense = {
        'name' : name,
        'type' : types,
        'amount' : amount
    }
    expenses.append(expense)
    return expenses

def calulate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def calulate_average(expenses):
    if len(expenses) == 0:
        return 0
    else:
        average = calulate_total(expenses)/len(expenses)
        return average

def category_wise_total(expenses):
    category_total = {}
    for expense in expenses:
        expense_type = expense['type']
        expense_amount = expense['amount']
        if expense_type in category_total:
            category_total[expense_type] += expense_amount
        else:
            category_total[expense_type] = expense_amount
    for expense_type,expense_amount in category_total.items():
        print(f"{expense_type} : {expense_amount}")
    

    

if __name__ == "__main__":
    main()