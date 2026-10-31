import json



def get_status(score):

    if score >= 80:
        return "Hot"

    elif score >= 60:
        return "Warm"

    else:
        return "Cold"


def get_new_lead():

    name = input("Enter name: ").strip()

    email = input("Enter email: ").strip()

    message = input("Enter message: ").strip()

    try:

        score = int(input("Enter score (0-100): "))

        if score < 0 or score > 100:

            print("Score must be between 0 and 100!")

            return None

    except ValueError:

        print("Invalid score!")

        return None

    status = get_status(score)

    lead = {
        "name": name,
        "email": email,
        "message": message,
        "score": score,
        "status": status
    }

    return lead





def save_lead(lead):

    try:

        with open("leads111.json", "r") as file:

            leads = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        leads = []

    for old_lead in leads:

        if old_lead.get("email", "").strip().lower() == lead["email"].strip().lower():
            print("This email already exists!")

            return

    leads.append(lead)

    with open("leads111.json", "w") as file:

        json.dump(leads, file, indent=4)

    print("Lead saved successfully!")



def show_leads():

    try:

        with open("leads111.json", "r") as file:

            leads = json.load(file)

        for lead in leads:

            print("----------------")

            print("Name:", lead.get("name","no name"))

            print("Email:", lead.get("email","no email"))

            print("Score:", lead.get("score","no score"))

            print("Status:", lead.get("status","no status"))

    except FileNotFoundError:

        print("No leads found!")

    except json.JSONDecodeError:

        print("JSON file is corrupted!")



def main():

    while True:

        print("\n===== LEAD CLASSIFIER =====")

        print("1. Add New Lead")

        print("2. Show All Leads")

        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            lead = get_new_lead()

            if lead is not None:

                save_lead(lead)

        elif choice == "2":

            show_leads()

        elif choice == "3":

            print("Goodbye!")

            break

        else:

            print("Invalid choice!")


main()