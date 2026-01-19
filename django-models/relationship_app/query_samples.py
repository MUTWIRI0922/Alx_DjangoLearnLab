from models import Author, Book, Library, Librarian
def sample_queries():
    #  Get all books by a specific author
    author = Author.objects.get(name="J.K. Rowling")
    books_by_author = author.books.all()


    # Get the librarian of a specific library
    library = Library.objects.get(name="Central Library")
    librarian_of_library = library.librarian

    # Get all books in a specific library
    books_in_library = library.books.all()

    return {
        "books_by_author": books_by_author,
        "librarian_of_library": librarian_of_library,
        "books_in_library": books_in_library,
    }