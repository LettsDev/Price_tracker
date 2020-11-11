import ezgmail
from csv import DictReader, DictWriter
import os.path
from os import path
import re

# class User (self, email_address):
#     def __init__(self):
#         pass
#     def _add(self):
#         pass
#     def _purge(self):
#         pass
#     def _help(self):
#         pass
#     def _status(self):
#         pass
#     def _admin(self):
#         pass
#     def _delete(self):
#         pass

# class Scrape(self, item_url):
#     def __init__(self):
#         pass
#     def _new_scrape(self):
#         pass
#     def _update(self):
#         pass
#     def _save(self):
#         pass
#     def _delete(self):
#         pass

def user_csv_exist():    #Is there a csv file 
    if path.exists("Users_and_items.csv"):
        pass
    else:
        with open("Users_and_items.csv","w") as file:
            headers = ["Item Number","Email Addresses", "Item URL", "Description"]
            csv_writer = DictWriter(file, fieldnames = headers)
            csv_writer.writeheader()

def price_csv_exist():
    if path.exists("Prices.csv"):
        pass
    else:
        with open("Prices.csv", "w") as file:
            price_headers = ["Line number","Item number", "Date", "Price"]
            csv_writer = DictWriter(file, fieldnames = price_headers)
            csv_writer.writeheader()
    
def load_user_data():
    user_data = {}
    with open("Users_and_items.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            user_data[row["Item Number"]] = [row["Email Addresses"], row["Item URL"], row["Description"]]
        return user_data

def load_price_data():
    prices = {}
    with open("Prices.csv") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            prices[row["Line number"]] = [row["Item number"], row["Date"], row["Price"]]
        return prices

def email_list(data):
    unique_addresses = []
    for info in data.values():
        if info[0] not in unique_addresses:
            unique_addresses.append(info[0])
    return unique_addresses

def check_email_inbox():
    unread_threads = ezgmail.unread()
    if len(unread_threads) == 0:
        return None
    else:
        return unread_threads

def get_new_mail(new_mail):
    num_thread = len(new_mail)
    message_info = {}
    email_pattern = re.compile(r"""
        ([a-z0-9_\.-]+) #Selecting the email address
        @
        ([0-9a-z\.-]+)
        \.
        ([a-z\.]{2,6}) 
""", re.VERBOSE | re.IGNORECASE)
    
    name_pattern = re.compile(r"""
        (\w{3,}\s)  #selecting the name
    """, re.VERBOSE)
    
    for i in range(num_thread):
            message_info[i] = [(name_pattern.search(new_mail[i].messages[0].sender)).group(0).strip(),
            (email_pattern.search(new_mail[i].messages[0].sender)).group(),
            new_mail[i].messages[0].subject,
            new_mail[i].messages[0].body]
    return message_info

def confirmation_email(email_address):
    ezgmail.send(email_address, 'Received your email',"Confirmed")  #TODO Add in relelvent information to the confirmation email body

def validation(messages):   #If valid information was sent in an email
    for message in messages.values():
        message[1]
    pass

def main():
    user_csv_exist()
    price_csv_exist()
    user_data = load_user_data()
    price_data = load_price_data()
    current_email_addresses = email_list(user_data)
    
    new_mail = check_email_inbox()
    if new_mail:
        new_messages = get_new_mail(new_mail)   #Dict format->  Email num: [sender name, email address, subject, body]
    
    print(new_messages)
main()

