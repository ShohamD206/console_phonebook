print("\n                                     * SHOHAM'S PYTHON PHONEBOOK PROJECT *                                     ")
print("________________________________________________________________________________________________________________\n")
import json

class Contact_details:
    def __init__(self, FullName, Address, PhoneNumber):
        self.FullName = FullName
        self.Address = Address
        self.PhoneNumber = PhoneNumber

    def view_Contact(self):
        print(" Full Name:", self.FullName, "\n", "Address:", self.Address, "\n", "Phone Number:", self.PhoneNumber)

    def editName(self, newContactName):
        self.FullName = newContactName

    def editAddress(self, newAddress):
        self.Address = newAddress

    def editPhoneNum(self, newPhone):
        self.PhoneNumber = newPhone

    def updateContact(self, newContact):
        self.FullName = newContact.FullName
        self.Address = newContact.Address
        self.PhoneNumber = newContact.PhoneNumber


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_New(self, newContact):
        self.contacts.append(newContact)

    def save_To_Json(self, jsonFileName):
        contactsInJson = []
        for contact in self.contacts:
            contactsInJson.append({"Full Name": contact.FullName, "Address": contact.Address, "Phone Number": contact.PhoneNumber})

        with open(jsonFileName, 'w') as jsonData:
            addData = json.dumps(contactsInJson, indent=3)
            jsonData.write(addData)

    def read_Json(self, jsonFileName):
        with open(jsonFileName, 'r') as viewJson:
            contactInFile = json.load(viewJson)
            contactsList = []

            for contactData in contactInFile:
                newContact = Contact_details(contactData['Full Name'], contactData['Address'], contactData['Phone Number'])
                contactsList.append(newContact)
            self.contacts = contactsList

    def viewContact(self):
        if (len(self.contacts) == 0):
            print('\tYour Contact List Is Empty...')
        else:
            print("\tFull Name, Address, Phone Number")
            for contact in self.contacts:
                print("\t" + contact.FullName + ",", contact.Address + ",", contact.PhoneNumber)

    def search_Contact(self, contactToSearch):
        contactExists = False
        for contact in self.contacts:
            if (contactToSearch == contact.FullName):
                contact.view_Contact()
                contactExists = True
        if (contactExists == False):
            print("\tError!! >>> The Requested Contact Was Not Found")

    def update_Contact(self):
        selectedContact = input("\t>>> Enter Full Name Of Contact To Update: ")
        selectedContact = selectedContact.title()
        ifFound = False
        for contact in self.contacts:
            if contact.FullName == selectedContact:
                edited = Contact_details(input("\t>>> Enter New Full Name: "),
                                 input("\t>>> Enter New Address: "),
                                 input("\t>>> Enter New Phone Number: "))
                contact.updateContact(edited)
                ifFound = True
                print("\tContact Update Successfully!")
        if ifFound == False:
            print("\t**ERROR!! >>> The Requested Contact Was Not Found")

    def delete_Contact(self, contactToDelete):
        ifFound = False
        for contact in self.contacts:
            if contact.FullName == contactToDelete:
                ifFound = True
                self.contacts.remove(contact)
                print('\tSelected Contact Deleted Successfully!')
        if ifFound == False:
            print("\tERROR!!!\n\tThe Requested Contact Was Not Found")

    def clear_Phonebook(self):
        self.contacts.clear()
        print("\tTHE REQUEST WAS SUCCESSFUL!")
        print("\tAll Contacts In PhoneBook Has Been Deleted...")




def menu():
    phoneBook = PhoneBook()
    print('\n')
    print('\n')

    phoneBook.read_Json('Contacts_Data.json')

    print("\t\tMAIN MENU")
    print("\t      ~~~~~~~~~~~~~")


    print("\t1. Add New Contact")
    print("\t2. View Contacts In Memory")
    print("\t3. Search Contact")
    print("\t4. Update Contact Info By Full Name")
    print("\t5. Delete Contact")
    print("\t6. Reset All")
    print("\t7. EXIT\n")

    cp = input("\tChoose By Option Number: ")
    print('\n')

    if cp == '1':
        newContact = Contact_details(input("\t>>> Contact Full Name: ").title(),
                             input("\t>>> Contact Address: ").title(),
                             input("\t>>> Contact Phone Number: "))
        phoneBook.add_New(newContact)
        print("\tNew Contact Has Been Added Successfully!")
        phoneBook.save_To_Json('Contacts_Data.json')
        print('\n')
        menu()

    elif cp == '2':
        phoneBook.viewContact()
        print('\n')
        menu()

    elif cp == '3':
        searchFullName = input("\t>>> Enter Contact Full Name: ")
        searchFullName = searchFullName.title()
        phoneBook.search_Contact(searchFullName)
        print("\n")
        menu()

    elif cp == '4':
        phoneBook.update_Contact()
        phoneBook.save_To_Json('Contacts_Data.json')
        print("\n")
        menu()

    elif cp == '5':
        delContact = input("\t>>> Enter The Contact's Full Name Who You Want To Delete: ")
        checking = input("\t>>> Are You Sure You Want To Delete " + delContact + "?\n" + "\tAnswer By YES/NO: ")
        if checking == "no":
            print('\tOperation Canceled, Contact Not Deleted!')
            print("\n")
            menu()
        elif checking == "yes":
            phoneBook.delete_Contact(delContact)
            phoneBook.save_To_Json('Contacts_Data.json')
            print("\n")
            menu()
        else:
            print("\tSomething Went Wrong, You Remove To MAIN MENU...")
            print("\n")
            menu()

    elif cp == '6':
        checking = input("\t>>> Are You Sure You Want To Reset Your PhoneBook Memory?\n" + "\tAnswer By YES/NO: ")
        if checking == "no":
            print('\tOperation Canceled!')
            print("\n")
            menu()
        elif checking == "yes":
            phoneBook.clear_Phonebook()
            phoneBook.save_To_Json('Contacts_Data.json')
            print("\n")
            menu()
        else:
            print("\tSomething Went Wrong, You Remove To MAIN MENU...")
            print("\n")
            menu()

    elif cp == '7':
        for i in range(0,1):
            break

    else:
        print("\t> > ERROR by selecting option, Try Again Now < <\n\n")
        menu()



if __name__ == '__main__':
    menu()
