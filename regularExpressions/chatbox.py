import re

# Orders in the record
ordersList = ['ABC123', 'ABC456', 'ABC789']


# Starting Chat and getting client's name
def greeting():
    print("Adam: Hello, I'm Agent: Adam!")
    print("Adam: I will ask questions about your order.")

# apply RegEx to check if the input is a valid order number


def orderNumber(name, order):
    p1 = "ABC\d{3}"
    match = re.search(p1, order, flags=re.IGNORECASE)

    while str(match) == 'None':
        print("Adam: I'm sorry, I don't understand your Order Number.")
        print("Adam: Enter your Order Number format ABC000: ")
        order = input(name + ": ")
        match = re.search(p1, order, flags=re.IGNORECASE)
    return match.group()

# match order number with the record


def orderInRecord(name, order):
    if order.upper() in ordersList:
        return order.upper()
    else:
        print("Adam: Your order is not in the record.")
        return False

# get the order number


def getOrderNumber(name):
    print("Adam: Hello " + name + "!")
    print("Adam: What is your Order Number? ")
    order = input(name + ": ")
    order = orderNumber(name, order)

    result = orderInRecord(name, order)
    while result == False:
        print("Adam: Please enter valid Order Number? ")
        order = input(name + ": ")
        orderNumber(name, order)
        order = orderInRecord(name, order)

    return order.upper()

# apply RegEx to check if the input is a valid email address


def checkEmail(name, email):
    p2 = "[\w\.\_\%\$]+@[a-zA-Z]+\.[a-zA-Z]+"
    match = re.search(p2, email, flags=re.IGNORECASE)
    while str(match) == 'None':
        print("Adam: I'm sorry, I don't understand your email address.")
        print("Adam: Enter your valid email address: ")
        email = input(name + ": ")
        match = re.search(p2, email, flags=re.IGNORECASE)
    return match.group()

# get the email address


def getEmail(name):
    print("Adam: What is your email address? ")
    email = input(name + ": ")
    email = checkEmail(name, email)
    return email

# apply RegEx to check if the input is a valid phone number


def checkPhone(name, phone):
    p3 = "\d{10}|\(\d{3}\)-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}"
    match = re.search(p3, phone)
    while str(match) == 'None':
        print("Adam: I'm sorry, I don't understand your phone number.")
        print("Adam: Enter your valid phone number 000-000-0000: ")
        phone = input(name + ": ")
        match = re.search(p3, phone)
    phone = match.group()

    if len(phone) > 10:
        newPhone = ''
        for i in range(0, len(phone)):
            if phone[i].isdigit():
                newPhone += phone[i]
        phone = newPhone
    return phone

# get the phone number


def getPhone(name):
    print("Adam: What is your phone number? ")
    phone = input(name + ":")
    phone = checkPhone(name, phone)
    return phone


# Main function
if __name__ == '__main__':
    client_Info = {'name': 'You', 'phone': 0, 'email': '', 'order': ''}
    greeting()
    client_Info['order'] = getOrderNumber(client_Info['name'])
    client_Info['email'] = getEmail(client_Info['name'])
    client_Info['phone'] = getPhone(client_Info['name'])
    print("Adam: Thank you for details our representative will call you soon.")
    print("\n=== Order Detail ===")
    print(
        'Order Number: ' + client_Info['order'] + '\n' +
        'Email: ' + client_Info['email'] + '\n' +
        'Phone: ' + client_Info['phone'] + '\n\n'
    )
