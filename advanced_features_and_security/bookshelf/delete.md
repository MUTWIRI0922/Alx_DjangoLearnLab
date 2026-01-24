## 📄 delete.md

```md
# Delete Book Record

## Command

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

## Results
<QuerySet []>
