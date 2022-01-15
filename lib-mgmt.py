import imp 
import os
from os import closerange, name, read
import winsound
import pickle
import datetime

from django.forms import ClearableFileInput
import Screens as view

#this class is used to manage .txt files and the Dictionary
class manage_files:
    def __init__(self, path_to_file, member_dict, books_dict):
        self.path_to_file = path_to_file
        membersANDbooksDict = member_dict
        booksANDusersDict = books_dict
       
    def read(self):

        File = open (f"{self.path_to_file}", "r")
        #print(f"path is {self.path_to_file}")
        for line in File:

            print(line)
        File.close()

# test method, not used in the code.
    def read_2(self, path):
        
        File = open(path, 'r')
        return File
        

# returns data form a .txt file as a python list. each line is a new item.
    def return_as_list(self):

        temp_list = []
        File = open (f"{self.path_to_file}", "r")
        #print(f"path is {self.path_to_file}")
        for line in File:
            # [0:-2] removes \n
            temp_list.append(line[0:-1]) 
        File.close()
        return temp_list



# this method adds new members/ books to both the dictionary and the .txt file.
    def add(self, name, type, path_to_history):
        temp_list = []
        temp_list.append(name)
        
        File = open(f"{self.path_to_file}", "a")
        File.write(f"{name}\n")
        File.close()
        if type == 'book':
            print("reached 3 ________")
            booksANDusersDict.update({name:''})
        elif type == 'member':
            
            membersANDbooksDict.update({name:''})
        File.close()
        self.make_history(path_to_history, temp_list)            
# makes .txt files in the given DIR 
    def make_history(self,path_to_history, memberlist):
        for member in memberlist:
            File = open(f'{path_to_history}/{member}.txt', 'w')
        File.close()

# Reads history files.
    def show_history(self, path, name):
        File = self.read_2(f'{path}/{name}.txt')
        for line in File:

            print(line)
        File.close()
# returns data form a .txt file as a python list. each line is a new item. temp_list.append(line[0:-1]) removes \n form each line
    def return_history_as_list(self, name,path_to_history):
        temp_list = []
        File = open(f"{path_to_history}/{name}.txt", 'r')

        for line in File:
            temp_list.append(line[0:-1]) 
        File.close()
        return temp_list

# more like define dictionary, this method adds books and members to the empty dictionary.
    def save_as_dictonary(self, booksList, membersList):

        for member in membersList:
            membersANDbooksDict.update({member:''})
        for book in booksList:
            booksANDusersDict.update({book:''})
        #print(booksANDusersDict.keys())
 # saves dictionary as a file so it can be loaded when the program is restarted   
    def save_dic(self,filename,path):
        
        if filename == "members":
            member_dict = membersANDbooksDict
            
            File = open(f'{path}/{filename}', 'wb')
            pickle.dump(member_dict, File)
            print("saving done_________________")
        elif filename == "books":
            book_dict = booksANDusersDict

            File = open(f'{path}/{filename}', 'wb')
            pickle.dump(book_dict, File)
            print("saving done_________________")
# loads the data when the program is started.
    def load_dict(self,filename,path):
        
        
        if filename == "members":
            
            File = open(f'{path}/{filename}', 'rb')
            data = pickle.load(File)
            return data
            
            
        elif filename == "books":
            
            File = open(f'{path}/{filename}', 'rb')
            data = pickle.load(File)
            return data
            
            
# checks if the book is free by checking the value . if it's empty than it's free.            
def is_avilable(book,booksANDusersDict):
    
    value = booksANDusersDict.get(book)
    if value != '':
        return False
    else:
        return True
# check to see if a book exists.        
def does_exist(book):
    
    value = booksANDusersDict.get(book)
    if value != None:
        return True
    else:
        return False    
            

# Clears consol. works both on windows and mac machines.
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')



class book_user_mgmt(manage_files):    

# the following 8 methods are used to manage history and dictionary files. DateTime is used to keep a log.        
    def add_book_to_user(self,booksName, path_to_user_history, membername):
        
        File = open(f'{path_to_user_history}/{membername}.txt', 'a+')
        File.write(f"{booksName}\n")

    def add_book_to_user_log(self,booksName, path_to_user_history_log, membername):
        
        File = open(f'{path_to_user_history_log}/{membername}.txt', 'a+')
        File.write(f"{booksName} was taken by {membername} at {datetime.datetime.now()}\n")



    def add_user_to_book(self,booksName, path_to_book_history, membername):

        File = open(f'{path_to_book_history}/{booksName}.txt', 'a+')
        File.write(f"{membername}\n")

    def add_user_to_book_log(self,booksName, path_to_book_history_log, membername):

        File = open(f'{path_to_book_history_log}/{booksName}.txt', 'a+')
        File.write(f"{membername} took {booksName} at  {datetime.datetime.now()}\n")
        
    def add_user_return_to_book_log(self,booksName, path_to_book_history_log, membername):

        File = open(f'{path_to_book_history_log}/{booksName}.txt', 'a+')
        File.write(f"{membername} returned {booksName} at {datetime.datetime.now()}\n")

    def add_book_to_user_retuen_log(self,booksName, path_to_user_history_log, membername):

        File = open(f'{path_to_user_history_log}/{membername}.txt', 'a+')
        File.write(f"{booksName} was returned by {membername} at  {datetime.datetime.now()}\n")          

    def remove_book_from_user(self,booksName, path_to_user_history, membername):
        
        with open(f'{path_to_user_history}/{membername}.txt', "r+") as File:
            lines = File.readlines()
        with open(f'{path_to_user_history}/{membername}.txt', "w+") as File:
            for line in lines:
                if line.strip("\n") != booksName.strip("\n"):
                    File.write(line)

    def remove_user_from_book(self,booksName,path_to_book_history, membername):

        with open(f'{path_to_book_history}/{booksName}.txt', "r+") as File:
            lines = File.readlines()
        with open(f'{path_to_book_history}/{booksName}.txt', "w+") as File:
            for line in lines:
                if line.strip("\n") != membername.strip("\n"):
                    File.write(line)


    # this method loans a book. books are given as a list. 
    def  loan(self, books,member,path_to_user_history,path_to_book_history,path_to_user_history_log,path_to_book_history_log):
        
        available_books = []
        # this for loop checks to see if there area any free books among th egiven books, if there are than add them to the list declared above. 
        for book in books:
            if is_avilable(book, booksANDusersDict) & does_exist(book):
                available_books.append(book)
            else:
                input(f'{book} is not available or it does not exist.\nPress Enter to continue...')    
        
        current_books = self.return_history_as_list(member,path_to_user_history)
        total_books = available_books+current_books
        # total books is the books already loaned to the user + the books he requested which are available.
        
        
        membersANDbooksDict.update({member: total_books})
        # this for loop manages history files.
        for book in available_books:
            booksANDusersDict.update({book: member})
            self.add_book_to_user(book, path_to_user_history, member)
            self.add_book_to_user_log(book, path_to_user_history_log, member)
            self.add_user_to_book(book, path_to_book_history, member)
            self.add_user_to_book_log(book, path_to_book_history_log, member)

    def return_book(self, books, member, path_to_user_history, path_to_book_history,path_to_user_history_log,path_to_book_history_log):
        # this method is  to self.loan(args*, kwargs**) but it workes the other way around.
        current_books = self.return_history_as_list(member,path_to_user_history)
        

        for book in books:
            booksANDusersDict.update({book: ''})
            current_books.remove(str(book)) 
            self.remove_book_from_user(book.strip("\n"), path_to_user_history, member.strip("\n"))
            self.remove_user_from_book(book.strip("\n"), path_to_book_history, member.strip("\n"))
            self.add_user_return_to_book_log(book, path_to_book_history_log, member)
            self.add_book_to_user_retuen_log(book,path_to_user_history_log,member)
        membersANDbooksDict.update({member: current_books})      
# this Functions simplify the methods. the also have TRY : except <ERROR> to prevent any errors.
def Make_history_files():

    books.make_history(path_to_book_history, booksList)
    members.make_history(path_to_user_history, membersList)

def Define_dictionary():
    books.save_as_dictonary(booksList,membersList)
    members.save_as_dictonary(booksList,membersList)
    
def Static_save():
    books.save_dic('books','./Data/dict-pickle')
    members.save_dic('members','./Data/dict-pickle')
def Loan_book(listOfBooks, member):
    try:
        manager.loan(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
    except FileNotFoundError:
        input('Member does not exist')
def Return_book(listOfBooks, member):
    try:
        manager.return_book(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
    except FileNotFoundError:
        input('Member/book does not exist')
def add_member(name):
    members.add(name, 'member', path_to_user_history)
def add_book(name):
    books.add(name,'book', path_to_book_history)
def str_to_list(st):
    temp_list  = []
    temp_str = ''
    for i in st:
        
        if i != ',':
            temp_str = temp_str + i
        else:
            temp_list.append(temp_str)
            temp_str = ''    
           

    return temp_list  



membersANDbooksDict = {

        }

booksANDusersDict = {

        }
                   
# Static
path_to_user_history = "./Data/UserHistory"
path_to_book_history = "./Data/BookHistory"
path_to_user_history_log = "./Data/UserHistory/log"
path_to_book_history_log = "./Data/BookHistory/log"
frequency = 800
duration = 250
# objects
books = manage_files("./Data/Books.txt", membersANDbooksDict, booksANDusersDict)
members = manage_files("./Data/Members.txt", membersANDbooksDict, booksANDusersDict)
manager = book_user_mgmt(None, membersANDbooksDict, booksANDusersDict)

 

#this lists are used in other methods, execute first
booksList = books.return_as_list()
membersList = members.return_as_list()
# loading data, executed  only when the program is started.
membersANDbooksDict = members.load_dict('members',"./Data/dict-pickle")
booksANDusersDict = members.load_dict('books',"./Data/dict-pickle")

          

state = True

while state:
    clearConsole()
    choice = str(input(view.home))
    



    if choice == '1':
        Name = input("enter the members's name. \n Name: ")
        Books1 = input("""Enter the name of the books. put a ',' in between \n Books: """ )+ ','
        list_of_books = str_to_list(Books1)
        Loan_book(list_of_books, Name)
        Static_save()
        winsound.Beep(frequency, duration)
        
        

    elif choice == '2':
        Name = input("enter the members's name. \n Name: ")
        Books1 = input("""Enter the name of the boosk. put a ',' in between \n Books : """)+ ','
        list_of_books = str_to_list(Books1)
        Return_book(list_of_books, Name)
        Static_save()
        winsound.Beep(frequency, duration)
        


    elif choice == '3':        
        Name = input('Enter the name: \n')
        add_member(Name)
        winsound.Beep(frequency, duration)
        

    elif choice == '4':
        Name = input('Enter the name of the book: \n')
        add_book(Name)
        winsound.Beep(frequency, duration)
        
    elif choice == '5':
        winsound.Beep(frequency, duration)
        Choice = input('ALL DATA WILL BE DELETED! \n ARE YOU SURE? Y/N').lower()
        if Choice == 'y':
            
            booksANDusersDict = {

            }
            membersANDbooksDict = {

            }
            Define_dictionary()
            Make_history_files()
            Static_save()
            input('Done!\nPress Enter to leave')
            

    elif choice == '6':
        books.read()
        input('Press Enter to leave')
        winsound.Beep(frequency, duration)
        
    elif choice == '7':
        members.read()
        input('Press Enter to leave')
        winsound.Beep(frequency, duration)
        
    elif choice == '8':
        choice = input(view.History_view)
        if choice == '1':
            Name = input("Please Enter the name of the book.\n Name: ")
            books.show_history(path_to_book_history_log, Name)
            input('Press Enter to leave')
            winsound.Beep(frequency, duration)
            
        if choice == '2':
            Name = input('Please Enther the name of the member.\n Name: ')     
            members.show_history(path_to_user_history_log, Name)
            input('Press Enter to leave')
            winsound.Beep(frequency, duration)
        

    elif choice == '9':

        print (membersANDbooksDict)
        print (booksANDusersDict)
        input('Press Enter to leave')
    elif choice.lower() == 'exit':
        clearConsole()
        state = False    

    else:
        print('Choie MUST be a nunber. From 1 to 8')    
