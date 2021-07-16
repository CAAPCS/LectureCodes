

class Book(object):
    def __init__(self, title, author, text):
        self.title = title
        self.text = text
        self.author = author

class Client(object):
    def __init__(self, name):
        self.name = name

class Library(object):
    def __init__(self):
        self.listOfBooks = []
        self.listOfClients = [] # contain Client(s)

    def addBook(self, book):
        self.listOfBooks.append(book)

    def addClient(self, client):
        self.listOfClients.append(client)

    def printLibraryClients(self):
        for client in self.listOfClients:
            print(">>", client.name)

    def printLibraryBooks(self):
        for book in self.listOfBooks:
            print(">>", book.title)

    def numberOfBooks(self):
        return len(self.listOfBooks)


if __name__ == '__main__':
    print("Welcome to the library")
    websterLibrary = Library()
    client1 = Client("Austin")

    # line 42 instantiates a book, and it sets its atrributes
    book1 = Book("Think Python", "Allen Downey", "it says lot of things...")

    #line below  instantiates another different book, and it sets its atrributes
    book2 = Book("Theory of Communicative Action", "Jurgen Habermas", "speech acts blah blah...")

    websterLibrary.addBook(book1)
    websterLibrary.addBook(book2)
    websterLibrary.addClient(client1)

    print("this is the list of clients")
    websterLibrary.printLibraryClients()

    print("this is the list of books we have:", websterLibrary.numberOfBooks())
    websterLibrary.printLibraryBooks()