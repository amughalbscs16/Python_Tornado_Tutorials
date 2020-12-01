from controllers.base_controller import BaseController
from model import User
import json


class UserController(BaseController):
    def __init__(self, data):
        # init parent constructor for parent attributes
        super().__init__()
        self.data = data
        # maintain a list of functions in the controller to check
        self.methods = ["get_all_users"]

    def get_all_users(self):
        users = self.gdb.query(User).all()
        users_dict = []
        for user in users:
            users_dict.append({
                'medicine_name': user.medicine_name,
                'dosage_unit': user.dosage_unit
            })
            print(user.medicine_name)

        return json.dumps(users_dict)
