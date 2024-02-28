from expense import Expense


def main():
    print(f"Is this running?") #Test method
    expense_file_path = "expenses.csv"
    # get user to input an expense
   # expense = get_user_expense()
    # print(expense) Another test method
    # Write their expense to a file
   # save_expense_to_file(expense, expense_file_path)
    #Read file and summerize expenses

    summarize_expenses(expense_file_path)

    pass

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    # print(f"You've entered {expense_name}, {expense_amount}")  Debugging Line


    expense_categories = [
        "🎂Food", 
        "🏡Home", 
        "🏬Work", 
        "😀Fun", 
        "🎈Misc"

    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1 

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]

            new_expense = Expense(name=expense_name, category= selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid selection. Please try another!")




        break

    

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
 
def summarize_expenses(expense_file_path):
    print(f"Summarizing expenses")
    expenses: list[Expense]= []
    with open(expense_file_path, "r",encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount)
                , category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print(amount_by_category)



if __name__ == "__main__":
    main()
