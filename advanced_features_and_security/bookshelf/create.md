# command
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year="1949-01-01"
)                

book

# results
<Book: Book object (1)>