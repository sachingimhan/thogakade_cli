from app.validation.validation import validate, ARGS, KWARGS
import json
import os

__db_items__ = "db/items"


class Item:
    def __init__(self):
        pass

    @validate(4, ARGS)
    def save(self, id, name, price, qty):
        with open(f"{__db_items__}/{name}.json", 'w') as f:
            data = {
                'id': id,
                'name': name,
                'price': price,
                'qty': qty
            }
            json.dump(data, f)
        print("Item Saved successfully.!")

    def __get_item_list(self, name):
        try:
            item_list = os.listdir(__db_items__)
            return [x for x in item_list if x == f"{name}.json"][0]
        except Exception as e:
            return None

    @validate(1, ARGS)
    def find(self, name):
        item = self.__get_item_list(name)
        if item != None:
            with open(f"{__db_items__}/{item}", "r") as f:
                data = json.load(f)
                return data
        else:
            return None

    @validate(1, ARGS)
    def is_item_exist(self, name):
        item = self.__get_item_list(name)
        if item != None:
            return item.__contains__(name)
        else:
            return False

    def getAll(self):
        files = os.listdir(__db_items__)
        all_items = []
        if len(files) > 0:
            for fs in files:
                with open(f"{__db_items__}/{fs}", "r") as f:
                    data = json.load(f)
                    all_items.append(data)
            return all_items
        else:
            return None
