def add_book():
    file = open("books.txt", "a")

    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    book_id = input("Enter book ID: ")

    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book found:", data)
            file.close()
            return

    file.close()
    print("Book not found.")


def issue_book():
    book_id = input("Enter book ID: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id and data[3] == "Available":
            data[3] = "Issued"

        file.write(",".join(data) + "\n")

    file.close()
    print("Book issued successfully.")


def return_book():
    book_id = input("Enter book ID: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"

        file.write(",".join(data) + "\n")

    file.close()
    print("Book returned successfully.")


def display_available():
    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data)

    file.close()


add_book()
search_book()
issue_book()
return_book()
display_available()