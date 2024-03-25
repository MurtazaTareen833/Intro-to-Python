class Library:
    def __init__(self):
        self.books = []

    def print_all_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("The library is empty.")

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def get_number_of_books(self):
        return len(self.books)


# Example usage
library = Library()

library.print_all_books()  # The library is empty.

library.add_book("THE LORD OF THE RINGS")
library.add_book("LIFE OF PI")
library.add_book("PABLO ESCOBAR")

library.print_all_books()
# Books in the library:
# Book 1
# Book 2
# Book 3

num_books = library.get_number_of_books()
print("Number of books:", num_books)  # Number of books: 3
