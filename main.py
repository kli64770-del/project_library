import menu

from all_function import display_books,search_book,add_book,Borrow_book,return_book,get_available_books,get_book_by_author

from input_user import get_author,get_name,get_positive_num

from data import books

def main():
    
    is_exist =False
    while not is_exist:
        menu.menu()
        choise_user=input("please enter your choose (1-8):\n or prees 8 for exit ")
        if int(choise_user)>8 or int(choise_user) < 1:
            print("try agian...")
            choise_user=input(" enter your choose (1-8):\n or prees 8 for exit:")

        if choise_user == "1":
            display_books(books)

        elif choise_user =="2":
            print(search_book(books,get_name()))

        elif choise_user =="3":
            print(add_book(books,get_name(),get_author(),get_positive_num()))

        elif choise_user =="4":
            print(Borrow_book(books,get_positive_num()))
        
        elif choise_user =="5":
            print(return_book(books,get_positive_num()))

        elif choise_user =="6":
            print(get_available_books(books))

        elif choise_user =="7":
            print(get_book_by_author(books,get_author()))

        if choise_user == "8":
            print("goodbye!!!!")
            is_exist = True

main()