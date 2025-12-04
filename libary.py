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
    users_dict ={}

    try:
        with open('user.txt','r')as f:
            for line in f:
                line = line.strip()
                if line:
                    username,password = line.split(',')
                    users_dict[username]= password

    except FileNotFoundError:

        print("file not found!")
        
        return users_dict  
 #book_id,title,author,quantity

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
        """create a set to store all the ids of the books"""
        book_ids = set()
        for book in books_list:
            #dictionary
            book_ids.add(book['id'])
        return book_ids 


    ###user registration
    def register_user(user_dict):
        """register a new user""" 
        print("\n --- Register a New user ---") 
        username = input("enter the username:").strip()
        password = input("enter the password:").strip()    
if username in users_dict:
        print(f"username alrealy exists!")
        return False
        if not username or not password:
         print("Username and password cannot be empty")
        return False
        users_dict[username] = password

    # save the registered user to the file 'users.txt'
        with open('users.txt', 'a') as f:
         f.write(f"{username},{password}\n")

        print("registration successfull!")
        return True

#users_dict = load_user()
#print(users_dict)
#register_user(users_dict)

def login_users(users_dict):
    print("\n------login user-----")
    username = input("enter username:").strip()
    password = input("enter password:").strip()


    if username in users_dict and users_dict[username]== password:
        print(f"welcome!{username .capitalize ()}")
        return username
    else:
        print("invalid username or password!")
        return None
    
login_user(users_dict)

### now book operation start
### main menu function

def main_menu():
    """display main menu option"""
    print("="*55)
    print("\ libary managment system")
    print("="*55)
    print






