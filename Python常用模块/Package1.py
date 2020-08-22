# coding-utf8

class Book:
    lang = 'learn python with wayne'

    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author


def new_book():
    return "数据准备和特征工程"


if __name__ == '__main__':  # 程序入口
    python = Book('wayne')
    author_name = python.get_name()
    print(author_name)
    published = new_book()
    print(published)
