import sys
import pickle
import json
import os
from app.Item import Item
from app.User import User
from app.validation.validation import get_inputs

banner = """
██████  ██    ██     ██████   ██████  ███████ 
██   ██  ██  ██      ██   ██ ██    ██ ██      
██████    ████       ██████  ██    ██ ███████ 
██         ██        ██      ██    ██      ██ 
██         ██        ██       ██████  ███████ 
                                              
"""


user = User()
item = Item()


def init():
    if not os.path.exists('db/'):
        os.makedirs('db/items')
        os.makedirs('db/users')
    else:
        print('Already initialized the System')


@get_inputs(params=['email', 'password'])
def user_reg_inputs(email, password):
    user.registration(email, password)

@get_inputs(params=['email','password'])
def user_login_inputs(email, password):
    user.login(email,password)

def user_view_session():
    user.view_session()

@get_inputs(params=['id','name','price','qty'])
def item_add(id,name,price,qty):
    item.save(id,name,price,qty)


if __name__ == "__main__":
    print(banner)
    args = sys.argv[1:]

    if len(args) <= 0:
        print("Arguments Not Found! Please Provide arguments <section> <commend>")
    elif args[0] == "system" and args[1] == "init":
        init()
    elif not os.path.exists('db'):
        print('Please initialize the system before use.!\nuse main.py system init')
    else:
        section = args[0]
        commend = args[1]

        if section == "item":
            if commend == "add":
                item_add()
        if section == "user":
            if commend == "reg":
                user_reg_inputs()
            elif commend == "login":
                user_login_inputs()
            elif commend == "session":
                user_view_session()
