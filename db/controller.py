import sqlite3
import sys, os
from enum import Enum

sys.path.append(os.path.abspath("."))

from db.util.logger import log
from db.table_definitions import get_all_table_defs


class Connection(Enum):
    """Idea is to have the possibility of running tests on a different db connection as to not touch the run environment.
    This is however not yet implemented @TODO"""
    TEST = "test.sqlite"
    FILE = "db.sqlite"


#* ********************************************* DB INIT *********************************************
def db_init(conn:Connection=Connection.FILE) -> None:
    """Initializes the database connection

    Args:
        conn (Connection, optional): Connection to be connected. Defaults to Connection.FILE.
    """
    for table in get_all_table_defs():
        try:
            cx = sqlite3.connect(conn.value)
            log.info("Creating table: " + str(table))
            cx.execute(table)
        except sqlite3.Error as e:
            log.error(f"Failed to create table {table}: {e}")


def db_drop_all(conn:Connection=Connection.FILE) -> None:
    """temporary function used to test/debug, currently only called in populate_debug_data.py"""
    cx = sqlite3.connect(conn.value)
    log.info("Dropping all tables")
    tables_to_drop:list[str] = ["user", "habit_data", "habit_subscription", "completion"]
    for table in tables_to_drop:
        try:
            cmd = str("DROP TABLE IF EXISTS " + table)
            cx.execute(cmd)
        except sqlite3.Error as e:
            log.error(f"Failed to drop table {table}: {e}")
    cx.commit()
    cx.close()


#* ********************************************* VOCAB *********************************************
def db_create_vocab(wrd_kanji:str, wrd_furigana:str, meanings:str, conn:Connection=Connection.FILE) -> bool:
    """"""
    cx = sqlite3.connect(conn.value)
    try:
        result = cx.execute(
            """
            INSERT INTO vocab (word, furigana, meanings)
            VALUES (?, ?, ?)
            """,
            (wrd_kanji, wrd_furigana, meanings)
        )
        return True
    except sqlite3.Error as e:
        log.error(f"Error creating vocab entry: {e}")
        return False
    finally:
        cx.commit()
        cx.close()