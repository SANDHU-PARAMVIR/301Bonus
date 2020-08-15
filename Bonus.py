print("Would you like to enter a new contact?")
ans = input("Yes or No: ")

contact_data = []
while ans == "YES" or "Yes" or "yes":
    print("Insert their information.")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")
    if len(phone) != 10:
        phone = input("The phone number provided does not have"
                      "the proper length. Please Re-enter: ")
    contact = []+[name]+[phone]+[email]+[address]
    contact_data.append(contact)
    ans = input("Would you like to continue adding info: ")
    if ans == "NO" or "No" or "no":
        break
    if ans == "YES" or "Yes" or "yes":
        print("Ok Great")
        continue

print(contact_data)
