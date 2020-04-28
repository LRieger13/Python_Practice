readFile = open("FroggyBooks.txt", "r")
books = readFile.readlines()

bookList = []

for item in books:
    item = item.strip()
    bookItem = item.split(",")
    print (bookItem)
readFile.close()
