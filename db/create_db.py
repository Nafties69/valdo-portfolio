import sqlite3

conn = sqlite3.connect('C:\dev\Piculator\db\piculator.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE images (
        id INTEGER PRIMARY KEY,
        filename TEXT,
        filepath TEXT,
        metadata TEXT,
        style TEXT,
        group_id TEXT,
        source_model TEXT
    )
''')
conn.commit()
conn.close()
