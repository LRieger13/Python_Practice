
'''
AUTHOR: Leah Rieger
DATE: November 29, 2018
PROGRAM: Froggy's Bookstore
'''

readFile = open("FroggyBooks.txt", "r")
books = readFile.readlines()
shoppingCart = []

def start(): #opening statement
    name = input("Welcome to Froggy's Bookstore! What is your name?\n")
    print(f"Hello {name}! Our items for the day are: ")
    print("==============================================================")
    return name

def getBookList(display): #list of choices
    bookList = []
    itemNumber = 0
    for item in books:
        itemNumber += 1
        if(display):
            print(f"{itemNumber}) {item}")
        item = item.strip()
        bookItem = item.split(",")
        bookList.append(bookItem)
    if(display):
        print("==============================================================")

    return bookList

def userChoice(): #shoppers choices to shopping cart
   bookList = getBookList(True)
   usrSelection = int(input("Please select your item: \n"))
   qty = input(f"You chose {bookList[usrSelection - 1][1]}, How many would you like? \n")
   ary = [usrSelection - 1, qty]

   return ary

def cart(boughtItems):
    masterBookList = getBookList(False)#won't print entire book ary
    
    qty = int(boughtItems[1])
    book = masterBookList[boughtItems[0]]
    bookTitle = book[1]
    price = float(book[2])
    subtotal = price * qty
    
    print(f"Item: {bookTitle}\n Qty: {qty}\n Price: {price}\n Subtotal: {subtotal}\n")
    orderArray = [qty, book, bookTitle, price]
    shoppingCart.append(orderArray)


def totalOutShoppingCart(username):
    myString = "" #var to concat lines into write file
    subTotal = 0
    myString += "**********************************************************"
    myString += f"\nThank you {username} for your purchase at Froggy's Book Store\n"
    myString += "**********************************************************\n"
    myString += f"Qty\t Item\t \tPrice\n"
    for order in shoppingCart: #to print
        myString += f"{order[0]}\t {order[2]}\t {order[3]}\n"
    subTotal += (round(order[0] * order[3], 2))
    tax = (round(subTotal * 0.076, 2))
    total = (round(subTotal + tax, 2))
    myString += f"Sub Total:\t{subTotal}\n"
    myString += f"Tax:\t{tax} \n"
    myString += f"Total:\t{total} \n"
    myString += f"**********************************************************\n"
    receipt(myString) #writes to txt
    print(f"{myString}")

def receipt(myString):

    write_file = open("Receipt.txt", "w")
    write_file.write(myString)
    write_file.close()


def order(username): #store the users selection in an array
    boughtItems = userChoice() #shopping cart
    cart(boughtItems)
    print("==============================================================")
    shopping = input("Would you like to add more? \n")
    print("==============================================================")
    if (shopping == "y"):
        order(username)
    else:
        print("Let's get your total! \n")
        totalOutShoppingCart(username)
            

  
username = start()
order(username)








