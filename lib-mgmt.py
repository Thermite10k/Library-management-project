from os import closerange, name, read
import pickle
import datetime
import Screens as view


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

    def return_as_list(self):

        temp_list = []
        File = open (f"{self.path_to_file}", "r")
        #print(f"path is {self.path_to_file}")
        for line in File:
            # [0:-2] removes \n
            temp_list.append(line[0:-1]) 
        File.close()
        return temp_list




    def add(self, name, type, path_to_history):
        temp_list = []
        temp_list.append(name)
        print("reached 1 ________")
        File = open(f"{self.path_to_file}", "a")
        File.write(f"{name}\n")
        File.close()
        if type == 'book':
            print("reached 3 ________")
            booksANDusersDict.update({name:''})
        elif type == 'member':
            print("reached 2 ________")
            membersANDbooksDict.update({name:''})
        File.close()
        self.make_history(path_to_history, temp_list)            

    def make_history(self,path_to_history, memberlist):
        for member in memberlist:
            File = open(f'{path_to_history}/{member}.txt', 'w')
        File.close()




    def return_history_as_list(self, name,path_to_history):
        temp_list = []
        File = open(f"{path_to_history}/{name}.txt", 'r')

        for line in File:
            temp_list.append(line[0:-1]) 
        File.close()
        return temp_list


    def save_as_dictonary(self, booksList, membersList):

        for member in membersList:
            membersANDbooksDict.update({member:''})
        for book in booksList:
            booksANDusersDict.update({book:''})
        #print(booksANDusersDict.keys())
    
    def save_dic(self,filename,path):
        
        if filename == "members":
            member_dict = membersANDbooksDict
            
            File = open(f'{path}/{filename}', 'wb')
            pickle.dump(member_dict, File)
            print("sacing done_________________")
        elif filename == "books":
            book_dict = booksANDusersDict

            File = open(f'{path}/{filename}', 'wb')
            pickle.dump(book_dict, File)
            print("sacing done_________________")

    def load_dict(self,filename,path):
        
        
        if filename == "members":
            
            File = open(f'{path}/{filename}', 'rb')
            data = pickle.load(File)
            return data
            
            
        elif filename == "books":
            
            File = open(f'{path}/{filename}', 'rb')
            data = pickle.load(File)
            return data
            
            
            
def is_avilable(book,booksANDusersDict):
    
    value = booksANDusersDict.get(book)
    if value != '':
        return False
    else:
        return True              



class book_user_mgmt(manage_files):    

        
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


   
    def  loan(self, books,member,path_to_user_history,path_to_book_history,path_to_user_history_log,path_to_book_history_log):
        current_books = self.return_history_as_list(member,path_to_user_history)
        total_books = books+current_books
        print(total_books)
        
        membersANDbooksDict.update({member: total_books})
        
        for book in books:
            booksANDusersDict.update({book: member})
            self.add_book_to_user(book, path_to_user_history, member)
            self.add_book_to_user_log(book, path_to_user_history_log, member)
            self.add_user_to_book(book, path_to_book_history, member)
            self.add_user_to_book_log(book, path_to_book_history_log, member)

    def return_book(self, books, member, path_to_user_history, path_to_book_history,path_to_user_history_log,path_to_book_history_log):

        current_books = self.return_history_as_list(member,path_to_user_history)
        print(current_books)

        for book in books:
            booksANDusersDict.update({book: ''})
            current_books.remove(str(book)) 
            self.remove_book_from_user(book.strip("\n"), path_to_user_history, member.strip("\n"))
            self.remove_user_from_book(book.strip("\n"), path_to_book_history, member.strip("\n"))
            self.add_user_return_to_book_log(book, path_to_book_history_log, member)
            self.add_book_to_user_retuen_log(book,path_to_user_history_log,member)
        membersANDbooksDict.update({member: current_books})      

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
    manager.loan(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
def Return_book(listOfBooks, member):
    manager.return_book(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
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
# objects
books = manage_files("./Data/Books.txt", membersANDbooksDict, booksANDusersDict)
members = manage_files("./Data/Members.txt", membersANDbooksDict, booksANDusersDict)
manager = book_user_mgmt(None, membersANDbooksDict, booksANDusersDict)
# after methods that update the dictionary, save_as_dictionary
# 

#this lists are used in other methods, execute first
booksList = books.return_as_list()
membersList = members.return_as_list()

membersANDbooksDict = members.load_dict('members',"./Data/dict-pickle")
booksANDusersDict = members.load_dict('books',"./Data/dict-pickle")

          

state = True

while state:
    choice = str(input(view.home))



    if choice == '1':
        Name = input('enter the name: \n')
        Books1 = input("""Enter the name of the books. put a ',' in between \n Books: """ )+ ','
        list_of_books = str_to_list(Books1)
        Loan_book(list_of_books, Name)
        Static_save()
        

    elif choice == '2':
        Name = input('Enter the name: \n')
        Books1 = input("""Enter the name of the boosk. put a ',' in between \n Books : """)+ ','
        list_of_books = str_to_list(Books1)
        Return_book(list_of_books, Name)
        Static_save()


    elif choice == '3':        
        Name = input('Enter the name: \n')
        add_member(Name)

    elif choice == '4':
        Name = input('Enter the name of the book: \n')
        add_book(Name)
    elif choice == '5':
        Choice = input('ALL DATA WILL BE DELETED! \n ARE YOU SURE? Y/N').lower()
        if choice == 'y':
            booksANDusersDict = {

            }
            membersANDbooksDict = {

            }
            Define_dictionary()
            Make_history_files()
            Static_save()

    elif choice == '6':
        books.read()
    elif choice == '7':
        members.read()
    elif choice == '8':
        pass                        
print (membersANDbooksDict)
print (booksANDusersDict)    