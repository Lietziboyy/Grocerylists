import sqlite3
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
DATABASE = 'testdb.db'
current_dateTime = datetime.datetime.now()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_time', methods=['POST'])
def get_time():
    hour = current_dateTime.hour
    minute = current_dateTime.minute
    time = f"{hour}:{minute}"
    return jsonify({'time': time})  # Return the time as JSON

def get_date():
    date_added = current_datetime.strftime('%Y-%m-%d')


@app.route('/api/create_table', methods=['POST'])
def create_table():
    """
    Creates a table in the SQLite database to store grocery items.
    """
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS groceries 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 grocery TEXT, 
                 time_added TEXT, 
                 date_added TEXT, 
                 category TEXT, 
                 amount INTEGER, 
                 unit TEXT, 
                 notes TEXT, 
                 store TEXT, 
                 deleted INTEGER)''')
    conn.commit()
    conn.close()
    return jsonify({'message': 'Table created successfully'})

@app.route('/api/delete_checked_item', methods=['POST'])
def delete_checked_item():
    try:
        data = request.get_json()
        id = data['id']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("DELETE FROM groceries WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Item deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add_item', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        required_keys = ['id', 'category', 'amount', 'unit', 'notes', 'shop', 'grocery', 'user']
        for key in required_keys:
            if key not in data:
                return jsonify({'error': f'Missing required key: {key}'}), 400

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        get_time()
        c.execute("INSERT INTO groceries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            data['id'],
            data['user'],
            data['shop'],
            data['grocery'],
            get_time,
            date['date_added'],
            data['category'],
            data['amount'],
            data['unit'],
            data['notes'],
            data['deleted']
        ))
        conn.commit()
        conn.close()

        result = {'result': 'Item added successfully'}
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
