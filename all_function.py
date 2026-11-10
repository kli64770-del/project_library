from data import books
from input_user import get_name,get_author


def display_books(books):
    for book in books:
        print(book)


def search_book( books , name):
    for book in books:
        if name in book["name"].lower().strip() or name in book["name"]:
            return book
    
            
def add_book(books,name,author,year):
    new_book={}

    for book in books:
        
        if name.lower().strip().replace(" ","") == book["name"].lower().strip().replace(" ","")  and author.lower().strip().replace(" ","")  == book["author"].lower().strip().replace(" ","")  :
            return False
    new_book["id"]= get_next_book_id(books)
    new_book["name"] = name
    new_book["author"] = author
    new_book["year"] = year
    new_book["available"] = True

    books.append(new_book)
    
    print("The book add to the library!")
    
    return True

def Borrow_book(books,book_id):
    for book in books:
        if book ["id"] == book_id and book["available"] == True:
            book["available"] = False
            return True

    return False


def return_book(books , book_id):
    for book in books:
        if book["id"] == book_id and book["available"] == False:
            book["available"] = True
            print("the book is returned")
            return True
    return False 

def get_available_books(books):
    available_books=[]
    for book in books:
        if book["available"] == True:
            available_books.append(book)
    return available_books

def get_book_by_author(books,author):
    books_list=[]
    for book in books:
        if book["author"].lower().strip().replace(" ","") == author.lower().strip().replace(" ",""):
            books_list.append(book)
    return books_list


def get_next_book_id(books):
    return books[-1]["id"]+1


# print(search_book(books,"Hrry"))



# print(Borrow_book(books,1))

# print(return_book(books,1))

# print(get_available_books(books))
        

# print(get_book_by_author(books,"Robert Martin"))
