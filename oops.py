class Person:
    # ----- PRIVATE CONSTRUCTOR -----
    def __init__(self):
        self.__firstName = None
        self.__lastName = None
        self.__address = None
        self.__city = None
        self.__state = None
        self.__zip = None
        self.__phoneNo = None

        # struct-like DOB
        self.__dob = {
            "day": None,
            "month": None,
            "year": None
        }

    # ----- STATIC FUNCTION TO CREATE OBJECT -----
    @staticmethod
    def create_person():
        p = Person()  # constructor is still technically private by convention

        p.__firstName = input("Enter First Name: ")
        p.__lastName = input("Enter Last Name: ")
        p.__address = input("Enter Address: ")
        p.__city = input("Enter City: ")
        p.__state = input("Enter State: ")
        p.__zip = input("Enter Zip: ")
        p.__phoneNo = input("Enter Phone Number: ")

        d = int(input("Enter DOB Day: "))
        m = int(input("Enter DOB Month: "))
        y = int(input("Enter DOB Year: "))
        p.__dob = {"day": d, "month": m, "year": y}

        return p

    # ----- GETTERS -----
    def getFirstName(self): return self.__firstName
    def getLastName(self): return self.__lastName
    def getAddress(self): return self.__address
    def getCity(self): return self.__city
    def getState(self): return self.__state
    def getZip(self): return self.__zip
    def getPhoneNo(self): return self.__phoneNo
    def getDOB(self): return self.__dob

    # ----- SETTERS -----
    def setFirstName(self, v): self.__firstName = v
    def setLastName(self, v): self.__lastName = v
    def setAddress(self, v): self.__address = v
    def setCity(self, v): self.__city = v
    def setState(self, v): self.__state = v
    def setZip(self, v): self.__zip = v
    def setPhoneNo(self, v): self.__phoneNo = v
    def setDOB(self, d, m, y): self.__dob = {"day": d, "month": m, "year": y}

    # ----- CONSTANT (READ-ONLY) DISPLAY METHOD -----
    def display(self):
        print("\n--- Person Details ---")
        print("Name:", self.__firstName, self.__lastName)
        print("Address:", self.__address)
        print("City:", self.__city)
        print("State:", self.__state)
        print("Zip:", self.__zip)
        print("Phone:", self.__phoneNo)
        dob = self.__dob
        print(f"DOB: {dob['day']}-{dob['month']}-{dob['year']}")


# -------------------- MAIN --------------------
def main():
    n = int(input("Enter number of persons: "))

    persons = []

    for i in range(n):
        print(f"\nEnter details for person {i+1}")
        persons.append(Person.create_person())

    print("\nDisplaying all persons:")
    for p in persons:
        p.display()


main()