
def classify_issue(issue):
    keywords = {
    "network": "Network",
    "printer": "Printer",
    "software": "Software",
    "hardware": "Hardware",
    "login": "Login",
    "email": "Email",
    "performance": "Performance",
    "other": "Other"
    }

    for i , j in keywords.items():
        if i in issue:
            return j 
    return 'Other'  




def help_desk(issue):
    ticket = {
            "issue_description": issue,
            "category":classify_issue(issue_description)
        }
    print("Ticket submitted successfully!")
    print("Submitted to:", ticket["category"])




print("Welcome to the Help Desk Management System!")

while True:
    print("\nWhat is your issue? (Type 'exit' to quit)")
    issue_description = input("Issue Description: ")

    issue_description =issue_description.lower()

    if issue_description == "exit":
        print("Exiting...")
        break

    help_desk(issue_description)