"""
libary managment system
(register,login)---> user
(add book ,issue book ,return book,view book ,search book)

"""



### creting two file named user.txt and book.txt to store user 
#information and book information permanently inside the file .

import os
print(os.path.exists('user.txt'))

if not os.path.exist('user.txt'):
    with open('users.txt','w')as f:
        pass
if not os.path.exist('book.txt'):
    with open('book.txt','w')as f:

### load data from the file
def load_user():
    """ load all the user from the user.txt into dictonary"""
    user_dict ={}

    try:
        with open('user.txt','r')as f:
            for line in f:
                line = line.strip()
                if line:
                    username,password = password
    except FileNotFoundError:

        print("file not found!")

    return user_dict  

def load_books():
    books_list = []
    try:
        with open("books.txt",'r')as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id,title,author,quantity = line.split()

                    book ={
                        'id': book-id,
                        'title': title,
                        'author': author,
                        'quantity':int(quantity)
                    }  
                    books_list.append(book)

    except FileNotFoundError:
        print("file not found!")
    return books_list



    def get_existing_books_id(books_list): 
        """create a set to store all the ids pf the books"""
        book_ids + set()
        for book in books_list:
            #dictionary
            book_ids.add(book['id'])
        return book_ids 


    ###user registration
    def register_user(user_dict):
        """register a new user""" 
        print("\
              --- Register a New user ---") 
        username = input("enter the username:").strip()
        password = input("enter the password:").strip()    






