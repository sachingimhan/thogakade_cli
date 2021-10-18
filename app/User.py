import os
import json
from app.validation.validation import validate, KWARGS, ARGS


__uid_file__ = "db/uid.json"
__db_user__ = "db/users"


class User:

    def __init__(self):
        if os.path.isfile(__uid_file__):
            with open(__uid_file__, 'r') as f:
                self.uid = json.load(f)
        else:
            self.uid = 0

    # @validate(2, ARGS)

    def registration(self, userName, password):
        self.uid += 1
        with open(f"{__db_user__}/{userName}.json", 'a') as f:
            data = {
                'uid': self.uid,
                'userName': userName,
                'password': password
            }
            json.dump(data, f)
        with open(__uid_file__, 'w') as f:
            self.uid += 1
            json.dump(self.uid, f)
