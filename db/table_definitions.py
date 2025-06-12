def get_all_table_defs() -> list[str]:
    return [Vocab]

Vocab:str = """
    CREATE TABLE IF NOT EXISTS vocab (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        furigana TEXT,
        meanings TEXT NOT NULL
    )"""