# command
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.id, book.title, book.author, book.publication_year

# results
(1, '1984', 'George Orwell', datetime.date(1949, 1, 1))

