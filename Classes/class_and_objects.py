
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.title} has {self.pages} pages."
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.pages == other.pages
        return NotImplemented
    
book1 = Book("The Great Gatsby", 180)
book2 = Book("To Kill a Mockingbird", 281)

print(len(book1))  # Output: 180
print(str(book1))  # Output: The Great Gatsby has 180 pages.
print(book1 == book2)  # Output: False

