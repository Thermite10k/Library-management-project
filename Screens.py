home = """
_______________________

1 = Loan a book
2 = Return a book
3 = Add a new Member
4 = Add a new Book
5 = Clear database
6 = Show a list of books
7 = Show a list of members
8 = show history

lib mgmt v1.01   2022
_______________________
"""

History_view = """ 
1 = Show Book history
2 = Show Member history
"""




test_dict = {

    'a': 'a',
    'b': 'b'
}

def does_exist(book):
    
    value = test_dict.get(book)
    if value != None:
        return True
    else:
        return False 

print(does_exist('d'))        