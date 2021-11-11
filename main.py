from app.Order import Order
import sys
import os
from app.Item import Item
from app.User import User
from app.Order import Order
from app.validation.validation import get_inputs
from beautifultable import BeautifulTable

banner = """
██████  ██    ██     ██████   ██████  ███████ 
██   ██  ██  ██      ██   ██ ██    ██ ██      
██████    ████       ██████  ██    ██ ███████ 
██         ██        ██      ██    ██      ██ 
██         ██        ██       ██████  ███████ 
                                              
"""
user_help = """
-------------------------------------------------------------------------
| Section  |   Commend   |   Description                                |
-------------------------------------------------------------------------
|   db     |    system   |   This will initialize system with db folder.|
|-----------------------------------------------------------------------|
|   user   |    reg      |   This will allows user to register.         |
|          |    login    |   This will allows user to login.            |
-------------------------------------------------------------------------

"""


user = User()
item = Item()
order = Order()


def init():
    if not os.path.exists('db/'):
        os.makedirs('db/items')
        os.makedirs('db/users')
        os.makedirs('db/orders')
    else:
        print('Already initialized the System')


@get_inputs(params=['email', 'password'])
def user_reg_inputs(email, password):
    user.registration(email, password)


@get_inputs(params=['email', 'password'])
def user_login_inputs(email, password):
    user.login(email, password)


def user_view_session():
    user.view_session()


def item_get_all():
    data = item.getAll()
    if data!= None:
        table = BeautifulTable()
        table.columns.header = ["ID","Name","Price","Qty"]
        for i in data:
            table.rows.append([i['id'],i['name'],i['price'],i['qty']])
        table.rows.sort('ID')
        print(table)
    else:
        print("No Items found.!")


@get_inputs(params=['id', 'name', 'price', 'qty'])
def item_add(id, name, price, qty):
    item.save(id, name, price, qty)


@get_inputs(params=['name'])
def item_find(name):
    data = item.find(name)
    if(data!= None):
        table = BeautifulTable()
        table.columns.header=["ID","Name","Price","Qty"]
        table.rows.append([data['id'],data['name'],data['price'],data['qty']])
        table.rows.sort('ID')
        print(table)
    else:
        print("No Items found.!")


def order_all():
    order.all()


def error_commend():
    print("Invalid commend. for help run program with `help` parameter ex: main.py help")


def order_place():
    item_list = []
    item_get_all()
    while True:
        item_name = input('\nPlease Enter Your Item Name: ')
        qty = input('\nPlace Enter Qty: ')
        if item.is_item_exist(item_name):
            item_list.append([item_name, qty])
        else:
            print("Sorry Item can not found. please check again.", end="\n")
        is_continue = input("Do you want to add more items (Yes/No): ")
        if is_continue.lower() == "no":
            break
        else:
            continue
    result = order.place(item_list)
    if result == True:
        print("\nYour order has been placed. Thank you.!")
    else:
        print("\nPlease Try again.!")


if __name__ == "__main__":
    print(banner)
    args = sys.argv[1:]

    if len(args) <= 0:
        print(
            user_help, "\nArguments Not Found! Please Provide arguments <section> <commend>")
    elif args[0] == "system" and args[1] == "init":
        init()
    elif not os.path.exists('db'):
        print('Please initialize the system before use.!\nuse main.py system init')
    elif args[0] == "help":
        print(user_help)
    else:
        section = args[0]
        commend = args[1]

        if section == "item":
            if commend == "add":
                item_add()
            elif commend == "all":
                item_get_all()
            elif commend == "find":
                item_find()
            else:
                error_commend()
        if section == "user":
            if commend == "reg":
                user_reg_inputs()
            elif commend == "login":
                user_login_inputs()
            elif commend == "session":
                user_view_session()
            else:
                error_commend()
        if section == "order":
            if commend == "place":
                order_place()
            if commend == "all":
                order_all()
