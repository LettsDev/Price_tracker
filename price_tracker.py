from bs4 import BeautifulSoup
from csv import DictReader, DictWriter
import os.path
from os import path
import re, requests, ezgmail

user_data = {}  #{item number = name, email address, item URL, description}
price_data = {} #line number, item number, date, price
welcome_message = ""  #TODO create generic welcome message
help_message = ""   #TODO create help message 
user_data_headers = ["Item Number","Name","Email Address", "Item URL", "Description"]

class User (self, message):
    def __init__(self):
        self.message = message  #message ->  [sender name, email address, command, [list of URLs]]
    
    def _add(self):
        items = []
        if self.message[1] not in user_data.values():
            welcome_email(self.message[0],self.message[1])
        for URL in self.message[3]:
            for information in user_data.values():
                if  self.message[1] and URL in information:
                    ezgmail.send(self.message[1], "Already exists", f"You already have {information[4]} added to your watch list.")
                    return None
        
        for item_num in user_data.keys():   #adds item to user_data
            items.append(item_num)
        items.sort()
        user_data[items[len(items) + 1]] = [self.message[0],self.message[1],self.message[2],self.message[3]]
        #save user data to CSV
        with open("Users_and_items.csv","w") as file:
            csv_writer = DictWriter(file,fieldnames = headers)
            csv_writer.writerow(user_data)

    def _purge(self):
        for  key, information in user_data.items():
            if self.message[1] in information:
                del user_data[key]
            
    def _help(self):
        ezgmail.send(self.message[1],"Help using EZ-scrape",help_message)
    def _summary(self): #TODO create summary email template that can be linked to here
        pass
    # def _admin(self):
    #     pass
    def _delete(self):
        counter = 0
        for key, information in user_data.items():
            for URL in self.message[3]:
                if URL and self.message[1] in information:
                    del user_data[key]
                    counter += 1
        if counter != len(self.message[3]):
            ezgmail.send(self.message[1], "Unable to process your delete command", f"We were unable to find all the URl(s) ({self.message[3]}) in our records.\n The ones that we could find were deleted. \n Try sending the command: summary\n to see what we have on file.")
        else:
            ezgmail.send(self.message[1],"Confirmation", f'Your request to delete the URL(s): {self.message[3]}\n has been completed successfully!')

class Scrape(self, user_info):
    def __init__(self):
        self.user_info = user_info
    def _new_scrape(self):
        response = requests.get(user_info)

    def _save(self):
        pass

def user_csv_exist():    
    if path.exists("Users_and_items.csv"):
        pass
    else:
        with open("Users_and_items.csv","w") as file:
            
            csv_writer = DictWriter(file, fieldnames = user_data_headers)
            csv_writer.writeheader()

def price_csv_exist():
    if path.exists("Prices.csv"):
        pass
    else:
        with open("Prices.csv", "w") as file:
            price_headers = ["Entry number","Item number", "Date", "Price"]
            csv_writer = DictWriter(file, fieldnames = price_headers)
            csv_writer.writeheader()
    
def load_user_data():
    user_data = {}
    with open("Users_and_items.csv","r") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            user_data[row["Item Number"]] = [row["Name"], row["Email Address"], row["Item URL"], row["Description"]]
        return user_data

def load_price_data():
    prices = {}
    with open("Prices.csv", "r") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            prices[row["Entry number"]] = [row["Item number"], row["Date"], row["Price"]]
        return prices

def email_list(data):
    unique_addresses = []   #Gets email addresses from CSV
    for info in data.values():
        if info[0] not in unique_addresses:
            unique_addresses.append(info[1])
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
            message_info[i] = [(name_pattern.search(new_mail[i].messages[0].sender)).group(0).strip(),  #Extract name 
            (email_pattern.search(new_mail[i].messages[0].sender)).group(), #Extract email
            new_mail[i].messages[0].subject,
            new_mail[i].messages[0].body]
    return message_info

def welcome_email(name, email):
    ezgmail.send(email,f"Hey! Welcome {name}!",
    f"Hi {name}!\n{welcome_message}\n{help_message}")

def confirmation_email(email_address):
    ezgmail.send(email_address, 'Received your email',"Confirmed")  #TODO Add in relelvent information to the confirmation email body

def command_logic(messages):   #When a user sends a command 

#**********************************Email Error Checking**********************************
    commands = ("help", "summary", "delete", "purge", "new user", "add")
    website_pattern = re.compile(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    ,re.IGNORECASE)
    
    for message in messages.values():   #message -> [sender name, email address, subject, body]
        
        result = website_pattern.search(message[3]) #looking for URls in the body of the message
        message[2] = message[2].lower().strip() #formatting the subject
        message[3] = re.findall(result, message[3]) #[formatting the URLs]
        
        if message[2] not in commands:  #Was the correct command used in the subject line?
            ezgmail.send(message[1], "There was a problem with your request!",
             f"The command used in your last email: ({message[2]}) was mot understood.\n Please use one of the following commands in the subject line of your email: {commands}")   #TODO Replace with help message
            return None #For Error
        
        elif result == None:    #Are the URLs valid?
            ezgmail.send(message[1], "There was a problem with your request!",
            f"Valid URL(s) could not be found in: {message[3]}\nPlease try a different URL!")
            return None #For error
 
 #TODO add checking for the websites that are able to be scraped

#**********************************Command Sort**********************************
        else:  
            mailer = User(message)  #Command logic
            if message[2] == "add":
                mailer._add()
            elif message[2] == "help":
                mailer._help()
            elif message[2] == "summary":
                mailer._summary()
            elif message[2] == "delete":
                mailer._delete()
            elif message[2] == "purge":
                mailer._purge()
    return True

def scraping_schedule():    #TODO 
    update_scrape = Scrape(user_data)


def main():
    user_csv_exist()    #Initialization to make sure there are CSV files
    price_csv_exist()

    new_mail = check_email_inbox()  #Checking for new mail
    if new_mail:
        new_messages = get_new_mail(new_mail)   #Dict format->  Email num: [sender name, email address, subject, body]

    if command_logic(new_messages):

        user_data = load_user_data()    
        price_data = load_price_data()
        current_email_addresses = email_list(user_data)
        print(new_messages)
main()

