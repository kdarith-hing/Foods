from foodsearch import lookup
from database import connectToDB

if __name__ == '__main__':
    connectToDB()
    lookup('073007107034')