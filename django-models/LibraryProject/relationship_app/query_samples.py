from models import Author, Book, Library, Librarian
def sample_queries():
    #  Get all books by a specific author
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    # Get the librarian of a specific library
    library = Library.objects.get(name="library_name")
    librarian_of_library = Librarian.objects.get(library=library)

    # Get all books in a specific library
    
    books_in_library = Library.objects.get(name=library_name)

    return {
        "books_by_author": books_by_author,
        "librarian_of_library": librarian_of_library,
        "books_in_library": books_in_library,
    }