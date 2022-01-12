home = """
_______________________

1 = Loan a book
2 = Return a book
3 = Add a new Member
4 = Add a new Book
5 = Clear database
6 = Show a list of books
7 = Show a list of members
8 = show log

lib mgmt v1.01   2022
_______________________
"""

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

print(str_to_list('afafad,gfhsb,cvgmip,'))