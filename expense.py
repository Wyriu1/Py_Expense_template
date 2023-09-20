from PyInquirer import prompt
import csv

def new_expense(*args):
    list_users = []
    checkbox_users = []

    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in spamreader:
            list_users.append(row[0])
            checkbox_users.append({"name": row[0], "checked": True})

    expense_questions = [
        {
            "type": "input",
            "name": "amount",
            "message": "New Expense - Amount: ",
        },
        {
            "type": "input",
            "name": "label",
            "message": "New Expense - Label: ",
        },
        {
            "type": "list",
            "name": "spender",
            "message": "New Expense - Spender: ",
            "choices": list_users
        },
        {
            "type": "checkbox",
            "name": "payback",
            "message": "New Expense - Payback users: ",
            "choices": checkbox_users
        }
    ]

    infos = prompt(expense_questions)
    paybacks = infos.get("payback")

    if infos.get("spender") in paybacks:
        paybacks.remove(infos.get("spender"))

    row = [infos.get("spender"), infos.get("label"), infos.get("amount")]

    for payback in paybacks:
        row.append(payback)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)

    print("Expense Added !")
    return True


