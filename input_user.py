def get_name():
    is_exist=False
    while not is_exist:
        user_input=input("please enter name:")
        if user_input:
            is_exist = True
        else:
            print("\ntry agian...")
    return user_input


def get_author():
    is_exist=False
    while not is_exist:
        user_input=input("please enter author:").strip()
        if user_input:
            is_exist = True
        else:
            print("\ntry agian...")
    return user_input


def get_positive_num():
    is_positive=False
    while not is_positive:
        user_input=input("please enter positive number: " ).strip()
    
        if user_input.isdigit() and int(user_input) > 0  :
            is_positive = True
        else:
            print("\ntry agian enter positive number...")
    return int(user_input)


