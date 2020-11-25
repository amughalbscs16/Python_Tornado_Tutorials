from controllers.base_controller import BaseController
from model import Medicine
import json


class MedicineController(BaseController):
    def __init__(self):
        super().__init__()
        self.methods = ["get_all_medicines"]

    def get_all_medicines(self):
        medicines = self.gdb.query(Medicine).all()
        medicines_dict = []
        for medicine in medicines:
            medicines_dict.append({
                'medicine_name': medicine.medicine_name,
                'dosage_unit': medicine.dosage_unit
            })
            print(medicine.medicine_name)
        return json.dumps(medicines_dict)



print(MedicineController().get_all_medicines())
