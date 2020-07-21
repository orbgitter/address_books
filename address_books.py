# The program manages address books in folders

import json
import os
import unittest


class AddressBookException(Exception):
    pass

    def __init__(self, txt):
        self.message = txt


class Contact:

    def __init__(self, firstname, lastname, telephone):
        if not firstname.isalpha():
            raise AddressBookException("Invalid first name input in: " + firstname)
        else:
            self.firstname = firstname

        if not lastname.isalpha():
            raise AddressBookException("Invalid last name input in: " + lastname)
        else:
            self.lastname = lastname

        if not telephone.isdigit():
            raise AddressBookException("Invalid telephone input in: " + telephone)
        else:
            self.telephone = telephone


class AddressBook:

    i = 0

    def __init__(self, foldername):
        self.foldername = foldername
        self.home = os.getcwd()
        self.dir = os.path.join(os.getcwd(), foldername) # join the foldername argument to the path
        if not os.path.exists(self.dir):                 # check if the directory at the end of the path doesn't exist
            os.mkdir(self.dir)                           # if it doesn't exists, then creat a new directory w/ that name

        os.chdir(self.dir)     # change current directory to the one including 'dir'
        self.cwd = os.getcwd() # get the current directory
        os.chdir(self.home)

    def add_contact(self, contact):

        contact_list = [{"firstname": contact.firstname,
                         "lastname": contact.lastname,
                         "telephone": contact.telephone
                         }]
        try:
            with open(self.cwd + '\\' + 'contact_' + str(self.i) + '.json', 'w') as contact_json:
                json.dump(contact_list, contact_json)
                self.i = self.i + 1
        except AddressBookException:
            print("There was a problem converting python to json")

    def get_contacts(self):
        # Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)
        for root, directory, files in os.walk(self.cwd, onerror=AddressBookException, followlinks=True):
            if len(files) > 0:
                print("\nThe contacts on " + self.foldername + " folder are:")
                for file in files:
                    try:
                        with open(root + '\\' + file) as f:
                            data = json.load(f)  #convert json back to python
                    except AddressBookException:
                        print("There was a problem converting json back to python")
                    print(data)

    def find_contact(self, firstname, lastname, telephone):
        find_results = []
        for root, directory, files in os.walk(self.cwd, onerror=AddressBookException, followlinks=True):
            if len(files) > 0:  #as long as there are files of contacts
                for file in files:
                    try:
                        with open(root + '\\' + file) as f:
                            data = json.load(f)  # convert json back to python
                    except AddressBookException:
                        print("There was a problem converting json back to python")
                    if firstname == data[0].get("firstname") and lastname == data[0].get("lastname")\
                            and telephone == data[0].get("telephone"):
                        find_results.append(data[0])   #if all 3 conditions are met, then add contact to reference list
        print(str(find_results))
        # return find_results

# class TestMyFunctions(unittest.TestCase):
#
#     def test_contact(self):
#
#         person71 = Contact("ronen", "macabi", "246544523")
#
#         self.assertEqual(person71.firstname, 'ronen')
#         self.assertEqual(person71.lastname, 'macabi')
#         self.assertEqual(person71.telephone, '246544523')
#
#     def test_addressbook(self):
#
#         abook3 = AddressBook("michal")
#
#         self.assertEqual(abook3.foldername, "michal")
#
#         # self.assertEqual(abook3.find_contact("david","levi","353464234"), "[{'david', 'levi', '353464234'}]")
#
# if __name__ == '__main__':
#     unittest.main()


try:
    person1 = Contact("moshe", "cohen", "23523523")
    person2 = Contact("david", "levi", "246544523")
    person3 = Contact("david", "levi", "246544523")

    abook1 = AddressBook("orbar")

    abook1.add_contact(person1)
    abook1.add_contact(person2)
    abook1.add_contact(person3)
    abook1.find_contact("david", "levi", "246544523")

    person4 = Contact("moshe", "macabi", "23523523")
    person5 = Contact("david", "macabi", "246544523")
    person6 = Contact("david", "macabi", "246544523")

    abook2 = AddressBook("tomermisk")

    abook2.add_contact(person4)
    abook2.add_contact(person5)
    abook2.add_contact(person6)

    person7 = Contact("davidadadgsg", "macabi", "246544523")
    person8 = Contact("davidaffff", "macabi", "246544523")
    person9 = Contact("davidggggg", "levi", "246544523")
    person10 = Contact("davidhhhh", "levi", "246544523")

    abook3 = AddressBook("michal")

    abook3.add_contact(person7)
    abook3.add_contact(person8)
    abook3.add_contact(person9)
    abook3.add_contact(person10)

    abook4 = AddressBook("sivan")

    person11 = Contact("davidadadgsg", "macabi", "246544523")
    person12 = Contact("davidaffff", "macabi", "246544523")
    person13 = Contact("davidggggg", "levi", "246544523")
    person14 = Contact("davidhhhh", "levi", "246544523")

    abook4.add_contact(person11)
    abook4.add_contact(person12)
    abook4.add_contact(person13)
    abook4.add_contact(person14)

    abook1.get_contacts()
    abook2.get_contacts()
except AddressBookException as e:
    print(e.message)
