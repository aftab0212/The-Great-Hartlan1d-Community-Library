import platform

# Initialize listlab with sample book data
listlab = [
    {"title": "Book1", "author": "Author1", "year": "2023", "status": "available"},
    {"title": "Book2", "author": "Author2", "year": "2021", "status": "available"},
    {"title": "Book3", "author": "Author3", "year": "2020", "status": "available"}
]

def managelab():
    print(""" 
  ------------------------------------------------------
 |======================================================| 
 |======== The Great Hartlan1d Community Library	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View book List 
Enter 2 : To Add New book
Enter 3 : To Search for a book 
Enter 4 : To Remove a book
Enter 5 : To Check out a book
Enter 6 : To Check in a book
Enter 7 : To Exit

    """)

    try:
        userInput = int(input("Please select an option: "))
    except ValueError:
        exit("\nHey! That's Not A Number")
    else:
        print("\n")

    if userInput == 1:
        print("List of books\n")
        for book in listlab:
            print("Title: {}, Author: {}, Year: {}, Status: {}".format(book["title"], book["author"], book["year"], book["status"]))
        print()

    elif userInput == 2:
        new_book = {}
        new_book["title"] = input("Enter book title: ")
        new_book["author"] = input("Enter author name: ")
        new_book["year"] = input("Enter publication year: ")
        new_book["status"] = "available"  # New books are initially available
        listlab.append(new_book)
        print("\n=> New book '{}' successfully added \n".format(new_book["title"]))

    elif userInput == 3:
        search_title = input("Enter book title to search: ")
        found = False
        for book in listlab:
            if book["title"].lower() == search_title.lower():
                print("\n=> Record Found:\nTitle: {}, Author: {}, Year: {}, Status: {}".format(book["title"], book["author"], book["year"], book["status"]))
                found = True
                break
        if not found:
            print("\n=> No Record Found of book '{}' \n".format(search_title))

    elif userInput == 4:
        remove_title = input("Enter book title to remove: ")
        found = False
        for book in listlab:
            if book["title"].lower() == remove_title.lower():
                listlab.remove(book)
                print("\n=> Book '{}' Successfully Deleted \n".format(remove_title))
                found = True
                break
        if not found:
            print("\n=> No Record Found of book '{}' \n".format(remove_title))

    elif userInput == 5:
        check_out_title = input("Enter title of the book to check out: ")
        found = False
        for book in listlab:
            if book["title"].lower() == check_out_title.lower():
                if book["status"] == "checked out":
                    print("\n=> Book '{}' is already checked out \n".format(check_out_title))
                else:
                    book["status"] = "checked out"
                    print("\n=> Book '{}' Successfully Checked Out \n".format(check_out_title))
                found = True
                break
        if not found:
            print("\n=> Book '{}' Not Found \n".format(check_out_title))

    elif userInput == 6:
        check_in_title = input("Enter title of the book to check in: ")
        found = False
        for book in listlab:
            if book["title"].lower() == check_in_title.lower():
                if book["status"] == "checked out":
                    book["status"] = "available"
                    print("\n=> Book '{}' Successfully Checked In \n".format(check_in_title))
                else:
                    print("\n=> Book '{}' is not checked out \n".format(check_in_title))
                found = True
                break
        if not found:
            print("\n=> Book '{}' Not Found or Not Checked Out \n".format(check_in_title))

    elif userInput == 7:
        print("\nExiting the Library Management System. Goodbye!\n")
        quit()

    else:
        print("Please Enter Valid Option\n")


def runAgain():
    run_again = input("\nWant to continue (y/n)?: ")
    if run_again.lower() == 'y':
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        managelab()
        runAgain()
    else:
        quit()


# Entry point of the program
if __name__ == "__main__":
    managelab()
    runAgain()









