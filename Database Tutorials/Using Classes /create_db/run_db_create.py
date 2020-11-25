from base_engine.engine import create_db_tables, get_session
import asyncio

asyncio.run(create_db_tables())
session = get_session()


