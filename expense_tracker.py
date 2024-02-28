from expense import Expense


def main():
   ## print(f"Is this running?")

    # get user to input an expense
    expense = get_user_expense()
    print(expense)
    # Write their expense to a file
    save_expense_to_file()
    #Read file and summerize expenses

    summarize_expenses()

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

    

def save_expense_to_file():
    print(f"Writing to file")

 
def summarize_expenses():
    print(f"Summarizing expenses")
    


if __name__ == "__main__":
    main()
