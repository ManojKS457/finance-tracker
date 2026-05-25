from database.db import cursor, conn

def insert_income(source, amount, date):

    cursor.execute(
        "INSERT INTO income (source, amount, date) VALUES (?, ?, ?)",
        (source, amount, date)
    )

    conn.commit()

def insert_expense(category, amount, date):

    cursor.execute(
        "INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
        (category, amount, date)
    )

    conn.commit()