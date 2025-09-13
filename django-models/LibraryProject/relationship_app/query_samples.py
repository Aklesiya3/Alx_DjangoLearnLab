from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # get the author
        return Book.objects.filter(author=author)     # filter books by that author
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage (only when running this file directly)
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':", books_by_author("J.K. Rowling"))
    print("Books in 'Central Library':", books_in_library("Central Library"))
    print("Librarian of 'Central Library':", librarian_of_library("Central Library"))

