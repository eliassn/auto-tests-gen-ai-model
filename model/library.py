"""
library contains books
a book contains : id : int, title : str, contentPerPage : str, pages : int
"""

class Book:
  def __init__(self,title,contentPerPage,pagesCount):
    self.title = title
    self.contentPerPage = contentPerPage
    self.pagesCount = pagesCount
    self.id = 0
    self.lastPage = 0

  def current_page(self):
    return self.lastPage
  def turn_page(self):
    if self.lastPage < self.pagesCount:
       newPage = self.lastPage + 1
    else:
      newPage = "you reached the last page"
    return newPage
  def showTitle(self):
    return self.title
  def id(self):
    return self.id
  


class Library:
  def __init__(self):
    self.book = Book
    self.lib = []
  def add(self):
    return self.lib.append(self.book())
  def remove(self,id):
      index = self.lib.index(id - 1)
      return self.lib.remove(self.lib[index])
    
myBook = Book("titanic","blablabla",23)
library = Library
library.add(myBook)

print(library)

