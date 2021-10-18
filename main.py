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

def init():
    if not os.path.exists('db/'):
        os.makedirs('db/items')
        os.makedirs('db/users')
    else:
        print('Already initialized the System')


@get_inputs(params=['userName', 'password'])
def user_reg(userName, password):
    user.registration(userName, password)


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
            item = Item()
            if commend == "add":
                item.save(10, 10, 10)
        if section == "user":
            if commend == "reg":
                user_reg()
