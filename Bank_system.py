import re


EMAIL_PATTERN = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-z]+$"
PHONE_PATTERN = r"^[6-9][0-9]{9}$"
AADHAAR_PATTERN = r"^[0-9]{12}$"
PAN_PATTERN = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
IFSC_PATTERN = r"^[A-Z]{4}0[A-Z0-9]{6}$"
MICR_PATTERN = r"^[0-9]{9}$"
PINCODE_PATTERN = r"^[0-9]{6}$"
NAME_PATTERN = r"^[a-zA-Z]+$"
ACCOUNT_PATTERN = r"^[0-9]{4,18}$"
PLACE_PATTERN = r"^[a-zA-Z ]+$"
TEXT_PATTERN = r"^[a-zA-Z0-9 ,./-]+$"


class Customer:
    count = 0

    def __init__(self, first_name, middle_name, last_name, account_no, email,
                 phone, aadhaar_no, pan_no, address, balance=0.0):
        Customer.count = Customer.count + 1
        self.id = Customer.count

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.account_no = account_no
        self.address = address
        self.balance = balance
        self.transactions = []

        if re.match(EMAIL_PATTERN, email) == None:
            raise ValueError("Email is not valid")

        if re.match(PHONE_PATTERN, phone) == None:
            raise ValueError("Phone number is not valid")

        if re.match(AADHAAR_PATTERN, aadhaar_no) == None:
            raise ValueError("Aadhaar number is not valid")

        if re.match(PAN_PATTERN, pan_no) == None:
            raise ValueError("PAN number is not valid")

        if re.match(PINCODE_PATTERN, address["pin_code"]) == None:
            raise ValueError("Pin code is not valid")

        self.email = email
        self.phone = phone
        self.aadhaar_no = aadhaar_no
        self.pan_no = pan_no

    def __repr__(self):
        return "Customer(" + str(self.id) + ", " + self.full_name + ", " + self.account_no + ", " + str(self.balance) + ")"

    @property
    def full_name(self):
        if self.middle_name == "":
            return self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.middle_name + " " + self.last_name

    def get_details(self):
        details = {}
        details["id"] = self.id
        details["name"] = self.full_name
        details["account_no"] = self.account_no
        details["email"] = self.email
        details["phone"] = self.phone
        details["aadhaar_no"] = self.aadhaar_no
        details["pan_no"] = self.pan_no
        details["address"] = self.address
        details["balance"] = self.balance
        return details

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")
        self.balance = self.balance + amount
        self.transactions.append(["deposit", amount])

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be greater than 0")

        if amount > self.balance:
            raise ValueError("Not enough balance")
        self.balance = self.balance - amount
        self.transactions.append(["withdraw", amount])

    def edit_details(self, email=None, phone=None, address=None):
        if email != None:
            if re.match(EMAIL_PATTERN, email) == None:
                raise ValueError("Email is not valid")
            self.email = email

        if phone != None:
            if re.match(PHONE_PATTERN, phone) == None:
                raise ValueError("Phone number is not valid")
            self.phone = phone

        if address != None:
            self.address = address


class Bank:
    def __init__(self, name, initial, address, phone_nos, branch, ifsc, micr,
                 email, website):
        if re.match(IFSC_PATTERN, ifsc) == None:
            raise ValueError("IFSC is not valid")

        if re.match(MICR_PATTERN, micr) == None:
            raise ValueError("MICR is not valid")

        if re.match(PINCODE_PATTERN, address["pin_code"]) == None:
            raise ValueError("Pin code is not valid")

        self.name = name
        self.initial = initial
        self.address = address
        self.phone_nos = phone_nos
        self.branch = branch
        self.ifsc = ifsc
        self.micr = micr
        self.email = email
        self.website = website
        self.customers = []

    def __repr__(self):
        return "Bank(" + self.name + ", " + self.branch + ", " + self.ifsc + ")"

    def create_customer(self, first_name, middle_name, last_name, account_no,
                        email, phone, aadhaar_no, pan_no, address, balance=0.0):
        new_customer = Customer(first_name, middle_name, last_name, account_no,
                                email, phone, aadhaar_no, pan_no,
                                address, balance)
        self.customers.append(new_customer)
        return new_customer

    def find_customer_by_account_no(self, account_no):
        for customer in self.customers:
            if customer.account_no == account_no:
                return customer

        return None

    def filter_customers_by_name(self, name):
        result = []
        for customer in self.customers:
            if name.lower() in customer.full_name.lower():
                result.append(customer)
        return result

    def find_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def delete_customer(self, id):
        customer = self.find_customer_by_id(id)
        if customer == None:
            print("Customer not found")
            return False
        self.customers.remove(customer)
        print("Customer deleted")
        return True

    def get_total_balance(self):
        total = 0
        for customer in self.customers:
            total = total + customer.balance
        return total


def ask_with_pattern(message, pattern, error_message, allow_empty=False):
    while True:
        value = input(message).strip()
        if allow_empty and value == "":
            return value
        if re.match(pattern, value):
            return value
        print("Error:", error_message)


def ask_first_name():
    return ask_with_pattern("First name: ", NAME_PATTERN,
                            "Name should have only letters, no spaces or numbers")


def ask_middle_name():
    return ask_with_pattern("Middle name (press enter to skip): ", NAME_PATTERN,
                            "Name should have only letters, no spaces or numbers",
                            allow_empty=True)


def ask_last_name():
    return ask_with_pattern("Last name: ", NAME_PATTERN,
                            "Name should have only letters, no spaces or numbers")


def ask_new_account_no(bank):
    while True:
        account_no = ask_with_pattern("Account number: ", ACCOUNT_PATTERN,
                                      "Account number should be 4 to 18 digits")
        if bank.find_customer_by_account_no(account_no) != None:
            print("Error: This account number already exists")
        else:
            return account_no


def ask_email(allow_empty=False):
    return ask_with_pattern("Email: ", EMAIL_PATTERN,
                            "Email is not valid, example - name@gmail.com",
                            allow_empty)


def ask_phone(allow_empty=False):
    return ask_with_pattern("Phone: ", PHONE_PATTERN,
                            "Phone should be 10 digits and start with 6, 7, 8 or 9",
                            allow_empty)


def ask_aadhaar():
    return ask_with_pattern("Aadhaar number: ", AADHAAR_PATTERN,
                            "Aadhaar should be exactly 12 digits")


def ask_pan():

    while True:
        pan_no = input("PAN number: ").strip().upper()
        if re.match(PAN_PATTERN, pan_no):
            return pan_no
        print("Error: PAN should be like ABCDE1234F (5 letters, 4 digits, 1 letter)")


def ask_address():

    print("Enter address")
    address = {}
    address["street"] = ask_with_pattern("  Street: ", TEXT_PATTERN,
                                         "Street cannot be empty (letters, numbers , . / - allowed)")
    address["building"] = ask_with_pattern("  Building: ", TEXT_PATTERN,
                                           "Building cannot be empty (letters, numbers , . / - allowed)")
    address["landmark"] = ask_with_pattern("  Landmark (press enter to skip): ", TEXT_PATTERN,
                                           "Landmark can have only letters, numbers , . / -",
                                           allow_empty=True)
    address["city"] = ask_with_pattern("  City: ", PLACE_PATTERN,
                                       "City should have only letters")
    address["pin_code"] = ask_with_pattern("  Pin code: ", PINCODE_PATTERN,
                                           "Pin code should be exactly 6 digits")
    address["state"] = ask_with_pattern("  State: ", PLACE_PATTERN,
                                        "State should have only letters")
    address["country"] = ask_with_pattern("  Country: ", PLACE_PATTERN,
                                          "Country should have only letters")
    return address


def ask_amount(message):

    while True:
        text = input(message).strip()
        try:
            amount = float(text)
        except ValueError:
            print("Error: Please enter a number")
            continue
        if amount <= 0:
            print("Error: Amount should be greater than 0")
        else:
            return amount


def ask_opening_balance():

    while True:
        text = input("Opening balance: ").strip()
        try:
            balance = float(text)
        except ValueError:
            print("Error: Please enter a number")
            continue
        if balance < 0:
            print("Error: Balance cannot be negative")
        else:
            return balance


def ask_id(message):
    while True:
        text = input(message).strip()
        if text.isdigit():
            return int(text)
        print("Error: Id should be a number")


def ask_customer(bank):

    account_no = input("Enter account number: ").strip()
    customer = bank.find_customer_by_account_no(account_no)
    if customer == None:
        print("Error: No customer found with this account number")
    return customer


def show_menu():
    print()
    print("===== BANK MENU =====")
    print("1. Create customer")
    print("2. Find customer by account number")
    print("3. Find customer by id")
    print("4. Search customer by name")
    print("5. Deposit")
    print("6. Withdraw")
    print("7. Check balance")
    print("8. Total balance of bank")
    print("0. Exit")


def main():

    bank_address = {
        "street": "MG Road",
        "building": "Tower A",
        "landmark": "Near Metro",
        "city": "Pune",
        "pin_code": "411001",
        "state": "Maharashtra",
        "country": "India"
    }
    bank = Bank("State Bank of India", "SBI", bank_address, ["9876543210"],
                "Pune Main", "SBIN0001234", "411002001",
                "pune@sbi.com", "www.sbi.com")
    print("Welcome to", bank.name)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            first_name = ask_first_name()
            middle_name = ask_middle_name()
            last_name = ask_last_name()
            account_no = ask_new_account_no(bank)
            email = ask_email()
            phone = ask_phone()
            aadhaar_no = ask_aadhaar()
            pan_no = ask_pan()
            address = ask_address()
            balance = ask_opening_balance()

            c = bank.create_customer(first_name, middle_name, last_name,
                                     account_no, email, phone, aadhaar_no,
                                     pan_no, address, balance)
            print("Customer created:", c)

        elif choice == "2":
            c = ask_customer(bank)
            if c != None:
                print(c.get_details())

        elif choice == "3":
            id = ask_id("Enter customer id: ")
            c = bank.find_customer_by_id(id)
            if c == None:
                print("Error: No customer found with this id")
            else:
                print(c.get_details())

        elif choice == "4":
            name = input("Enter name to search: ").strip()
            if name == "":
                print("Error: Name cannot be empty")
            else:
                result = bank.filter_customers_by_name(name)
                if len(result) == 0:
                    print("No customer found")
                for c in result:
                    print(c)

        elif choice == "5":
            c = ask_customer(bank)
            if c != None:
                amount = ask_amount("Enter amount to deposit: ")
                c.deposit(amount)
                print("Deposit done. New balance:", c.get_balance())

        elif choice == "6":
            c = ask_customer(bank)
            if c != None:
                amount = ask_amount("Enter amount to withdraw: ")
                try:
                    c.withdraw(amount)
                    print("Withdraw done. New balance:", c.get_balance())
                except ValueError as e:
                    print("Error:", e)

        elif choice == "7":
            c = ask_customer(bank)
            if c != None:
                print("Balance:", c.get_balance())

        elif choice == "8":
            print("Total balance:", bank.get_total_balance())

        elif choice == "0":
            print("Thank you, bye!")
            break

        else:
            print("Error: Wrong choice, please enter a number from 0 to 8")


if __name__ == "__main__":
    main()
