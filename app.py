import sqlite3
import datetime

DATABASE = 'testdb.db' # pointing to the db file
current_dateTime = datetime.datetime.now() # current date and time

def get_time():
    global time
    hour = current_dateTime.hour
    minute = current_dateTime.minute
    time = f"{hour}:{minute}"
    return time

def create_table():
    +    """
    +    Creates a table in the SQLite database to store grocery items.
    +
    +    Parameters:
    +        None
    +
    +    Returns:
    +        None
    +    """
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS groceries 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, grocery TEXT, time_added TEXT, date_added TEXT, 
                 category TEXT, amount INTEGER, unit TEXT, notes TEXT, store TEXT, deleted INTEGER)''')
    conn.commit()
    conn.close()


def delete_checked_items():
    +    """
    +    Deletes the checked items from the 'groceries' table in the SQLite database.
    +
    +    Parameters:
    +    None
    +
    +    Returns:
    +    None
    +    """

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM groceries WHERE id IN (?)")
    conn.commit()
    conn.close()



def add_item(id, date_added, category, amount, unit, notes, shop, grocery, user, deleted):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    get_time() # calling the get_time function, which returns the current time
    c.execute("INSERT INTO groceries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, user, shop, grocery, time, date_added, category, amount, unit, notes, deleted))
    conn.commit()
    conn.close()



# manually setting variables and calling add_item function
date_added = current_dateTime.strftime("%m/%d/%Y")
category = "Food"
amount = 2
unit = "l"
notes = "the good Milk"
shop = "Whole Foods"
grocery = "Bananas"
user = "testuser"
deleted = 0
id = 3
add_item(id, date_added, category, amount, unit, notes, shop, grocery, user, deleted)
