class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

novel = Book("PROJECT: Loki Vol 1", "akosiibarra")
print(f"Original : {novel.title} {novel.author}")
del novel.author
print(f"Updated : {novel.title} {novel.author}")

novel2nd = Book("PROJECT: Loki Vol 2 ", "akosiibarra")
print(f"Original : {novel2nd.title} {novel2nd.author}")
print(f"Updated : {novel2nd.title} {novel2nd.author}")
