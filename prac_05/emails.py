def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

def main():
    email_detail = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_detail[email] = name
        email = input("Email: ")

    for email, name in email_detail.items():
        print("{name} ({email})".format(name=name, email=email))

main()