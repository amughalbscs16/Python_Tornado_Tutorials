
# Import session assign it to self.gdb of Base Controller
# Now use the session to create a user
from base_engine.engine import create_db_tables, get_session


class BaseController:
    def __init__(self):
        self.gdb = get_session()


