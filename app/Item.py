from app.validation.validation import validate,ARGS,KWARGS
import json
import os

__db_items__ = "db/items"

class Item:
    def __init__(self):
        pass

    @validate(4, ARGS)
    def save(self,id, name, price, qty):
        with open(f"{__db_items__}/{name}.json",'w') as f:
            data = {
                'id':id,
                'name':name,
                'price':price,
                'qty':qty
            }
            json.dump(data,f)
        print("Item Saved successfully.!")
    
    def getAll(self):
        files = os.listdir(__db_items__)
        if len(files) > 0:
            for fs in files:
                with open(f"{__db_items__}/{fs}","r") as f:
                    data = json.load(f)
                    print(f"ID: {data['id']} Name: {data['name']} Price: {data['price']} QTY: {data['qty']}",end='\n')
        else:
            print("No Items found.!")
