from controllers.base_controller import BaseController
from model import Medicine


class MedicineController(BaseController):
    def __init__(self):
        super.__init__()
        pass

    def get_all_medicines(self):
        medicines = self.gdb.query(Medicine).all()
        for medicine in medicines:
            print(medicine)


print(MedicineController().get_all_medicines())
