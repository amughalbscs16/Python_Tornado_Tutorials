from .medicine_control import MedicineController
from .user_control import UserController
from .base_controller import BaseController


registry = {
        'medicine_controller': MedicineController,
        'user_controller': UserController
}
