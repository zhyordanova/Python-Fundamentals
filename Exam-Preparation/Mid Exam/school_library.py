books = input().split("&")
line = input().split(" | ")


def check_book_exist(books_list, book_searched):
    return True if book_searched in books_list else False


while not line[0] == "Done":
    command_type = line[0]
    book = line[1]


    if command_type == "Add Book":
        if not check_book_exist(books, book):
            books.insert(0, book)

    elif command_type == "Take Book":
        if check_book_exist(books, book):
            books.remove(book)

    elif command_type == "Swap Books":
        book_2 = line[2]
        if book in books and book_2 in books:
            book_idx = books.index(book)
            book_2_idx = books.index(book_2)
            books[book_idx], books[book_2_idx] = books[book_2_idx], books[book_idx]


    elif command_type == "Insert Book":
        books.append(book)

    elif command_type == "Check Book":
        index = int(line[1])
        if not index > len(books):
            print(books[index])

    line = input().split(" | ")

print(", ".join(books))