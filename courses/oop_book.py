from json import JSONEncoder




# we defined the class named Book
class Book(dict):
    def __init__(self, name, author, pages):
        self.name = name # we create an object variabile in self.name
        self.author = author
        self.pages = pages
        self.pages_read = 0
        self.update_json_value()

    def update_json_value(self):
        super().__init__(name=self.name, author=self.author, pages=self.pages, pages_read=self.pages_read)

    def add_pages_read(self, pages_read):
        self.pages_read += pages_read
        self.update_json_value()


if __name__ == "__main__":
    pass
