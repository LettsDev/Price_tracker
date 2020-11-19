from bs4 import BeautifulSoup
from csv import DictReader, DictWriter
import os.path
from os import path
import re, requests 
from datetime import date, time
import ezgmail
# user_data = {}  #{item number = name, email address, item URL, description}
# price_data = {} #line number, item number, date, price
# welcome_message = ""  #TODO create generic welcome message
# help_message = ""   #TODO create help message 
# user_data_headers = ["Item Number","Name","Email Address", "Item URL", "Description"]

# class User:
#     def __init__(self):
#         self.message = message  #message ->  [sender name, email address, command, [list of URLs]]
    
#     def _add(self):
#         items = []
#         if self.message[1] not in user_data.values():
#             welcome_email(self.message[0],self.message[1])
#         for URL in self.message[3]:
#             for information in user_data.values():
#                 if  self.message[1] and URL in information:
#                     ezgmail.send(self.message[1], "Already exists", f"You already have {information[4]} added to your watch list.")
#                     return None
        
#         for item_num in user_data.keys():   #adds item to user_data
#             items.append(item_num)
#         items.sort()
#         user_data[items[len(items) + 1]] = [self.message[0],self.message[1],self.message[2],self.message[3]]
#         #save user data to CSV
#         with open("Users_and_items.csv","w") as file:
#             csv_writer = DictWriter(file,fieldnames = user_data_headers)
#             csv_writer.writerow(user_data)

#     def _purge(self):
#         for  key, information in user_data.items():
#             if self.message[1] in information:
#                 del user_data[key]
            
#     def _help(self):
#         ezgmail.send(self.message[1],"Help using EZ-scrape",help_message)
#     def _summary(self): #TODO create summary email template that can be linked to here
#         pass
#     # def _admin(self):
#     #     pass
#     def _delete(self):
#         counter = 0
#         for key, information in user_data.items():
#             for URL in self.message[3]:
#                 if URL and self.message[1] in information:
#                     del user_data[key]
#                     counter += 1
#         if counter != len(self.message[3]):
#             ezgmail.send(self.message[1], "Unable to process your delete command", f"We were unable to find all the URl(s) ({self.message[3]}) in our records.\n The ones that we could find were deleted. \n Try sending the command: summary\n to see what we have on file.")
#         else:
#             ezgmail.send(self.message[1],"Confirmation", f'Your request to delete the URL(s): {self.message[3]}\n has been completed successfully!')

# # class Scrape(self, user_info):
# #     def __init__(self):
# #         self.user_info = user_info
# #     def _new_scrape(self):
# #         for key, values in user_info.items():
# #             for URL in values[3]:
# #                 response = requests.get(URL)
            

#     def _save(self):
#         pass

# def user_csv_exist():    
#     if path.exists("Users_and_items.csv"):
#         pass
#     else:
#         with open("Users_and_items.csv","w") as file:
            
#             csv_writer = DictWriter(file, fieldnames = user_data_headers)
#             csv_writer.writeheader()

# def price_csv_exist():
#     if path.exists("Prices.csv"):
#         pass
#     else:
#         with open("Prices.csv", "w") as file:
#             price_headers = ["Entry number","Item number", "Date", "Price"]
#             csv_writer = DictWriter(file, fieldnames = price_headers)
#             csv_writer.writeheader()
    
# def load_user_data():
#     user_data = {}
#     with open("Users_and_items.csv","r") as file:
#         csv_reader = DictReader(file)
#         for row in csv_reader:
#             user_data[row["Item Number"]] = [row["Name"], row["Email Address"], row["Item URL"], row["Description"]]
#         return user_data

# def load_price_data():
#     prices = {}
#     with open("Prices.csv", "r") as file:
#         csv_reader = DictReader(file)
#         for row in csv_reader:
#             prices[row["Entry number"]] = [row["Item number"], row["Date"], row["Price"]]
#         return prices

# def email_list(data):
#     unique_addresses = []   #Gets email addresses from CSV
#     for info in data.values():
#         if info[0] not in unique_addresses:
#             unique_addresses.append(info[1])
#     return unique_addresses

# def check_email_inbox():
#     unread_threads = ezgmail.unread()
#     if len(unread_threads) == 0:
#         return None
#     else:
#         return unread_threads

# def get_new_mail(new_mail):
#     num_thread = len(new_mail)
#     message_info = {}
#     email_pattern = re.compile(r"""
#         ([a-z0-9_\.-]+) #Selecting the email address
#         @
#         ([0-9a-z\.-]+)
#         \.
#         ([a-z\.]{2,6}) 
# """, re.VERBOSE | re.IGNORECASE)
    
#     name_pattern = re.compile(r"""
#         (\w{3,}\s)  #selecting the name
#     """, re.VERBOSE)
    
#     for i in range(num_thread):
#             message_info[i] = [(name_pattern.search(new_mail[i].messages[0].sender)).group(0).strip(),  #Extract name 
#             (email_pattern.search(new_mail[i].messages[0].sender)).group(), #Extract email
#             new_mail[i].messages[0].subject,
#             new_mail[i].messages[0].body]
#     return message_info

# def welcome_email(name, email):
#     ezgmail.send(email,f"Hey! Welcome {name}!",
#     f"Hi {name}!\n{welcome_message}\n{help_message}")

# def confirmation_email(email_address):
#     ezgmail.send(email_address, 'Received your email',"Confirmed")  #TODO Add in relelvent information to the confirmation email body

# def command_logic(messages):   #When a user sends a command 

# #**********************************Email Error Checking**********************************
#     commands = ("help", "summary", "delete", "purge", "new user", "add")
#     website_pattern = re.compile(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
#     ,re.IGNORECASE)
    
#     for message in messages.values():   #message -> [sender name, email address, subject, body]
        
#         result = website_pattern.search(message[3]) #looking for URls in the body of the message
#         message[2] = message[2].lower().strip() #formatting the subject
#         message[3] = re.findall(website_pattern, message[3]) #[formatting the URLs]
        
#         if message[2] not in commands:  #Was the correct command used in the subject line?
#             ezgmail.send(message[1], "There was a problem with your request!",
#              f"The command used in your last email: ({message[2]}) was not understood.\n Please use one of the following commands in the subject line of your email: \n{commands}")   #TODO Replace with help message
#             return None #For Error
        
#         elif result == None:    #Are the URLs valid?
#             ezgmail.send(message[1], "There was a problem with your request!",
#             f"Valid URL(s) could not be found in: {message[3]}\nPlease try a different URL!")
#             return None #For error
 
#  #TODO add checking for the URLs that are able to be scraped

# #**********************************Command Sort**********************************
#         else:  
#             mailer = User(message)  #Command logic
#             if message[2] == "add":
#                 mailer._add()
#             elif message[2] == "help":
#                 mailer._help()
#             elif message[2] == "summary":
#                 mailer._summary()
#             elif message[2] == "delete":
#                 mailer._delete()
#             elif message[2] == "purge":
#                 mailer._purge()
#     return True

# def scraping_schedule():    #TODO 
#     update_scrape = Scrape(user_data)


# def main():
#     user_csv_exist()    #Initialization to make sure there are CSV files
#     price_csv_exist()

#     new_mail = check_email_inbox()  #Checking for new mail
#     if new_mail:
#         new_messages = get_new_mail(new_mail)   #Dict format->  Email num: [sender name, email address, subject, body]

#     if command_logic(new_messages):

#         user_data = load_user_data()    
#         price_data = load_price_data()
#         current_email_addresses = email_list(user_data)
#         print(new_messages)
# main()

class Data:
    price_headers = ["Entry number","Item number", "Date", "Price", "Description"]
    user_data_headers = ["Item Number","Email Address", "Name", "Website","Item URL"]
    item_data = {}
    price_data = {}

    def __init__(self):
        pass

    def item_csv_exists (self):
        if path.exists("Users_and_items.csv"):
            pass
        else:
            with open("Users_and_items.csv","w") as file:
                csv_writer = DictWriter(file, fieldnames = Data.user_data_headers)
                csv_writer.writeheader()

    def price_csv_exists (self):
        if path.exists("Prices.csv"):
            pass
        else:
            with open("Prices.csv", "w") as file:
                csv_writer = DictWriter(file, fieldnames = Data.price_headers)
                csv_writer.writeheader()
    
    def load_item_data (self):
        with open("Users_and_items.csv","r") as file:
            csv_reader = DictReader(file, fieldnames=Data.user_data_headers)
            for row in csv_reader:
                Data.item_data[row["Item Number"]] = {
                    "name" : row["Name"],
                    "email" : row["Email Address"],
                    "website" : row["Website"],
                    "URL" : row["Item URL"]
                }
            

    def load_price_data (self):
        with open("Prices.csv", "r") as file:
            csv_reader = DictReader(file,fieldnames= Data.price_headers)
            for row in csv_reader:
                Data.price_data[row["Entry number"]] = {
                   "item_num" : row["Item number"],
                   "date" : row["Date"],
                   "price" : row["Price"],
                   "descrip" : row["Description"]
                }
            return price_data

    def save_item_data (self, name, email, website, URL):
        self.name = name
        self.email = email
        self.website = website
        self.URL = URL
        
        counter = 0
        new_data = {}
        
        with open("Users_and_items.csv", "r") as file:
            csv_reader = DictReader(file, fieldnames= Data.user_data_headers)
            for row in csv_reader:
                counter += 1
            counter += 1
        
        new_data["Item Number" : counter] = {
            "Name" : self.name,
            "Email Address" : self.email,
            "Website" : self.website,
            "URL" : self.URL
        }    
        
        with open("Users_and_items.csv", "a+") as file:
            csv_writer = DictWriter(file, fieldnames = Data.user_data_headers)
            csv_writer.writerow(new_data)

    def save_price_data (self, item_number, price, description):
        self.item_number = item_number
        self.price = price
        self.description = description

        counter = 0
        new_price_data = {}
        today = date.today()

        with open("Prices.csv", "r") as file:
            csv_reader = DictReader(file, fieldnames= Data.price_headers)
            for row in csv_reader:
                counter += 1
            counter += 1
        
        new_price_data["Entry Number" : counter] = {
            "Item number" : self.item_number,
            "Date" : today,
            "Price" : self.price,
            "Description" : self.description
        }

        with open("Prices.csv", "a+") as file:
            csv_writer = DictWriter(file, fieldnames= Data.price_headers)
            csv_writer.writerow(new_price_data)
    
    def del_item_data (self, email_address, item_nums = None):   #TODO
        self.email_address = email_address
        self.item_nums = item_nums
    def del_price_data (self, email_address, item_nums = None):  #TODO
        self.email_address = email_address
        self.item_nums = item_nums


class Email:
    email_data = {}
    commands = ("help", "summary", "remove", "purge", "add")
    
    def __init__(self):
        pass
    
    def check_new_email(self):
        unread_threads = ezgmail.unread()
        if len(unread_threads) == 0:
            return None
        else:
            return unread_threads
    
    def load_email(self, unread_threads):
        self.unread_threads = unread_threads
        email = Email()                             #Why did I do this?
        for i in range(len(unread_threads)):
            email.process_email(unread_threads[i])
    
    def process_email(self, thread):
        self.thread = thread
        
        email_pattern = re.compile(r"""
        ([a-z0-9_\.-]+) 
        @
        ([0-9a-z\.-]+)
        \.
        ([a-z\.]{2,6}) 
        """, re.VERBOSE | re.IGNORECASE)
        
        name_pattern = re.compile(r"""
        (\w{3,}\s)  
        """, re.VERBOSE)
        
        url_pattern = re.compile(r"""(https?:\/\/(?:www\.
        |(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}
        |www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}
        |https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}
        |www\.[a-zA-Z0-9]+\.[^\s]{2,})"""
        , re.IGNORECASE | re.VERBOSE)

        website_pattern = re.compile(r"""(\.+)([a-zA-z0-9+]+)(\.)""")
        
        email_address = email_pattern.search(self.thread.messages[0].sender).group(0).strip()
        name = name_pattern.search(self.thread.messages[0].sender).group(0).strip()
        subject = self.thread.messages[0].subject.strip().lower()
        body = self.thread.messages[0].body 
        URLs = re.findall(url_pattern,body) #[website URLs]
        websites = []
        for url in URLs:
            websites.append(website_pattern.match(url).group(2))   #TODO 

        
        Email.email_data = {
            "name" : name,
            "subject" : subject,
            "URLs" : URLs,
            "email address" : email_address,
            "body" : body,   
            "websites" : websites
        }
    
    def cmd_error_check(self):
        if Email.email_data["subject"] in Email.commands:
            pass
        else:
            self.send_email("Error", f"Command was not found.\nPlease use one of the following commands in the subject field:\n{Email.commands}")
            return False
    def URL_error_check(self):
        if len(Email.email_data["URLs"]) > 0 and Email.email_data["subject"] in ("help", "summary", "remove", "purge"):
            pass
        else:
            self.send_email("Problem with the URL(s)", f"There was a problem processing the URL(s) that you sent:\n{Email.email_data['body']}\nThey were not formatted correctly.")
            return False

    def command_follow(self):
        if Email.email_data["subject"] == "help":
            self.cmd_help()
        elif Email.email_data["subject"] == "summary":
            self.cmd_summary()
        elif Email.email_data["subject"] == "remove":
            self.cmd_remove()
        elif Email.email_data["subject"] == "purge":
            self.cmd_purge()
        elif Email.email_data["subject"] == "add":
            self.cmd_add() 
    #----------------------Command methods----------------------------
    def cmd_help(self):
        help_message_body = """Hello!\n\nHere is a list of commands (entered into the subject field of your email):\n
        help : Use this command to get this message.\n
        summary : An overview of what items we are looking at for you.\n
        remove : This will remove the item number(s) you put in your email. Please structure: 1,2,3\n
        purge : This will remove all of the items. You will not receive another email (other than a confirmation).\n
        add : The URL(s) that you put in your email body field will be added.\n\n"""

        self.send_email("Help Message",help_message_body)
    
    def cmd_summary(self):
        pass
    def cmd_remove(self):
        email_address = Email.email_data["email address"]
        item_nums = (Email.email_data["body"]).split(",")
        Data.del_item_data(email_address, item_nums)
        Data.del_price_data(email_address, item_nums)
    def cmd_purge(self):
        email_address = Email.email_data["email address"]
        Data.del_item_data(email_address)
        Data.del_price_data(email_address)
    def cmd_add(self):
        name = Email.email_data["name"]
        email_address = Email.email_data["email_address"]
        Email.email_data
        Email.email_data                #TODO
    #----------------------Command methods----------------------------
    
    
    
    
    def erase_email(self):
        pass
    def send_email(self,subject,body):
        self.subject = subject
        self.body = body
        ezgmail.send(email_data['email address'], self.subject, self.body)

class Scrape:
    def __init__(self):
        pass
    def scheduler (self):
        pass
    def website_choice(self, website):
        self.website = website
        if self.website == "amazon":
            Scrape.amazon()
        elif self.website == "bestbuy":
            Scrape.best_buy()
        elif self.website == "homedepot":
            Scrape.HD()
        elif self.website == "staples":
            Scrape.staples()
    
    def retrieve(self):
        headers = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        

        Data.price_data
        pass
    def amazon(self):
        pass
    def best_buy(self):
        pass
    def HD (self):
        pass
    def staples (self):
        pass


