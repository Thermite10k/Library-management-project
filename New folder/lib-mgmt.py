from os import closerange, read
import pickle
import datetime


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
    manager.return_book(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
def Return_book(listOfBooks, member):
    manager.loan(listOfBooks,member, path_to_user_history,path_to_book_history, path_to_user_history_log,path_to_book_history_log)
def add_member(name):
    members.add(name, 'member', path_to_user_history)
def add_book(name):
    books.add(name,'book', path_to_book_history)




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
#


#books.make_history(path_to_book_history, booksList)
#members.make_history(path_to_user_history, membersList)

#books.save_as_dictonary(booksList, membersList)
#manager.loan(['One Hundred Years of Solitude by Gabriel Garcia Marquez','Moby Dick by Herman Melville'],'Shaun Howard', path_to_user_history,path_to_book_history)
membersANDbooksDict = members.load_dict('members',"./Data/dict-pickle")
booksANDusersDict = members.load_dict('books',"./Data/dict-pickle")


#print(is_avilable('Ulysses by James Joyce',booksANDusersDict))
#(membersANDbooksDict)
#books.save_as_dictonary(booksList,membersList)
#members.save_as_dictonary(booksList,membersList)

#books.load_dict("members",'./Data/dict-pickle', booksList,membersList)


#members.save_dic('members','./Data/dict-pickle')
#books.save_dic('books','./Data/dict-pickle')
#manager.remove_book_from_user('One Hundred Years of Solitude by Gabriel Garcia Marquez',path_to_user_history,'Shaun Howard')
#manager.remove_user_from_book('One Hundred Years of Solitude by Gabriel Garcia Marquez',path_to_book_history,'Shaun Howard ')
#books.save_as_dictonary(booksList,membersList)

print(membersANDbooksDict)
print(booksANDusersDict)

#members.save_dic('members',"./Data/dict-pickle")
#books.save_dic('books',"./Data/dict-pickle")



#books.add("added book 24.")
#books.make_history(path_to_book_history,booksList)
#members.make_history(path_to_user_history,membersList)
#books.read()
#print(books.return_as_list())

'''members = manage_files("./Data/Members.txt")
members.add("Ali Batashi2")
members.read()'''