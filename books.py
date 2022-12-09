from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Titulo 1', 'author': 'Author 1' },
    'book_2': {'title': 'Titulo 2', 'author': 'Author 2' },
    'book_3': {'title': 'Titulo 3', 'author': 'Author 3' },
    'book_4': {'title': 'Titulo 4', 'author': 'Author 4' },
}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS
# Original
"""@app.get("/")
async def read_all_books():
    return BOOKS """    
#Doing like this, I catched the book's data
@app.get("/{book_name}")
def read_book(book_name: str):
    return BOOKS[book_name]


#Using class parameters, then they will apear in DOCS, like AVAILABLE
"""
@app.get("/directions/{direction_name}")
def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up" }
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down" }
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left" }
    return {"Direction": direction_name, "sub": "Right" }
"""


"""
Testando alguns get 

@app.get("/books/mybook")
def read_favorite_book():
    return {"book_title": "My Favorite Book"}

@app.get("/book/{book_id}")
def read_book (book_id: int ):
    return {"book_title": book_id}

"""