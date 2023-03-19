import pickle
import os
class Contact:
     def __init__(self,name,email,phone):
         self.name=name
         self.email=email
         self.phone=phone
     def __str__(self):
         return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)
     def change_name(self,name):
         self.name=name
     def change_email(self,email):
         self.email=email
     def change_phone(self,phone):
         self.phone=phone

def add_contact():
     address_book_file = ''
     try:
         address_book_file=open("address_book_file","rb")
     except FileNotFoundError:
         address_book_file=open("address_book_file","wb+")
     is_file_empty=os.path.getsize("address_book_file")<1
     if is_file_empty:
         list_contacts=[]
     else:
         list_contacts=pickle.load(address_book_file)
     try:
         contact=get_contact_info_from_user()
         address_book_file=open("address_book_file","wb")
         list_contacts.append(contact)
         pickle.dump(list_contacts,address_book_file)
         print("Contact added")
     except KeyboardInterrupt:
         print("Contact not added")
     except EOFError:
         print("Contact not added")
     finally:
         address_book_file.close()

def get_contact_info_from_user():
     try:
         contact_name=input("Enter contact name\n")
         contact_email=input("Enter contact email\n")
         contact_phone=input("Enter contact phone number\n")
         contact=Contact(contact_name,contact_email,contact_phone)
         return contact
     except EOFError as e:
         raise e
     except KeyboardInterrupt as e:
         raise e

def search_contact():
     address_book_file=open("address_book_file","rb")
     is_file_empty=os.path.getsize("address_book_file")<1
     if is_file_empty:
         print("Address book is empty")
     else:
         search_name=input("Enter the name\n")
         is_contact_found=False
         list_contacts=pickle.load(address_book_file)
         for each_contact in list_contacts:
             contact_name=each_contact.name
             search_name=search_name.lower()
             contact_name=contact_name.lower()
             if(contact_name==search_name):
                 print(each_contact)
                 is_contact_found=True
                 return 1
         if is_contact_found != True:
             print("No contact found with the search name")
     address_book_file.close()

print("Enter 'a' to add a contact, 'b' to search the contacts, and 'q' to quit")
# Enter 'a' to add a contact, 'b' to search the contacts, and 'q' to quit
while True:
     choice=input("Enter your choice\n")
     if (choice=='q'):
         break
     elif (choice=='a'):
         add_contact()
     elif (choice=='b'):
         search_contact()
     else:
         print("Incorrect choice")