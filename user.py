from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    }
]

def add_user():
    infos = prompt(user_questions)

    row = [infos.get("name")]

    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)

    print("User Added !")
    return