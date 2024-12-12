class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
novel = Book("PROJECT: Loki", "akosiibarra")
novel2nd = Book("PROJECT: Loki", "akosiibarra")
print(f"Original : {novel.title} {novel.author}")
print(f"Original : {novel2nd.title} {novel2nd.author}")

del novel.author

print(f"Updated : {novel.title} {novel.author}")
print(f"Updated : {novel2nd.title} {novel2nd.author}")
