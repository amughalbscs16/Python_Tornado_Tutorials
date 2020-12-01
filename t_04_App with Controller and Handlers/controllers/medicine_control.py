from controllers.base_controller import BaseController
from model import Medicine
import json


class MedicineController(BaseController):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.methods = ["get_all_medicines", "get_medicine_by_id"]

    def get_all_medicines(self):
        medicines = self.gdb.query(Medicine).all()
        medicines_dict = []
        for medicine in medicines:
            medicines_dict.append({
                'medicine_name': medicine.medicine_name,
                'dosage_unit': medicine.dosage_unit
            })
            print(medicine.medicine_name)
        return json.dumps({"data": medicines_dict})

    def get_medicine_by_id(self):
        print(self.data)

        if 'medicine_id' in self.data:

            medicine = self.gdb.query(Medicine).filter(
                Medicine.medicine_id == self.data['medicine_id']
            ).one_or_none()

            if medicine:

                medicine_dict = {
                        'medicine_name': medicine.medicine_name,
                        'dosage_unit': medicine.dosage_unit
                }

                print(medicine.medicine_name)

                return json.dumps({"data": medicine_dict})
            else:
                return json.dumps({"data": {}})
        else:
            return json.dumps({"data": {}})

