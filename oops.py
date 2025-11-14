class DOB:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


class Person:
    # Private constructor
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zip = ""
        self.__phone_no = ""
        self.__dob = DOB()

    # Static factory method to create object
    @staticmethod
    def create_person():
        p = Person()
        p.__first_name = input("Enter First Name: ")
        p.__last_name = input("Enter Last Name: ")
        p.__address = input("Enter Address: ")
        p.__city = input("Enter City: ")
        p.__state = input("Enter State: ")
        p.__zip = input("Enter Zip: ")
        p.__phone_no = input("Enter Phone Number: ")

        print("Enter DOB (day month year): ", end="")
        day, month, year = map(int, input().split())
        p.__dob = DOB(day, month, year)

        return p

    # Getters (Accessors)
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_phone_no(self):
        return self.__phone_no

    def get_dob(self):
        return self.__dob

    # Setters (Mutators)
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zip_code):
        self.__zip = zip_code

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def set_dob(self, dob):
        self.__dob = dob

    # Constant display function
    def display(self):
        print("\n----- Person Details -----")
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"Address: {self.__address}, {self.__city}, {self.__state} - {self.__zip}")
        print(f"Phone: {self.__phone_no}")
        print(f"DOB: {self.__dob.day}/{self.__dob.month}/{self.__dob.year}")


# ---------- Main Function ----------
def main():
    n = int(input("Enter number of persons: "))
    persons = []

    for i in range(n):
        print(f"\nEnter details for person {i + 1}:")
        person = Person.create_person()
        persons.append(person)

    print("\n=== Displaying all persons ===")
    for i, person in enumerate(persons, start=1):
        print(f"\nPerson {i}:")
        person.display()


# Run program
if __name__ == "__main__":
    main()