from app.validation.validation import validate,ARGS,KWARGS
import json

__db_items__ = "db/items"

class Item:
    def __init__(self):
        pass

    @validate(4, ARGS)
    def save(self,id, name, price, qty):
        with open(f"{__db_items__}/{id}-{name}.json",'w') as f:
            data = {
                'id':id,
                'name':name,
                'price':price,
                'qty':qty
            }
            json.dump(data,f)
        print("Item Saved successfully.!")
