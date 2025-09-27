from flask import Flask, render_template, request, url_for, redirect
import psycopg2
from dotenv import load_dotenv
import os
app = Flask(__name__)

load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')


@app.route('/')
@app.route('/<name>')
def hello(name=None, data=None):
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection to PostgreSQL successful!")
    if conn:
        cur = conn.cursor()
        print("Cursor created.")
        if conn and cur:
            cur.execute("SELECT * FROM guestbook;")
            data = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
    return render_template('hello.html', name=name, data=data)

# `read-form` endpoint 
@app.route('/handleSubmit', methods=['POST'])
def handleSubmit():

    # Get the form data as Python ImmutableDict datatype 
    name = request.form.get('name')
    content = request.form.get('why')
    print(content)

    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connection to PostgreSQL successful!")
        if conn:
            cur = conn.cursor()
            print("Cursor created.")
            if conn and cur:
                sql = f"INSERT INTO guestbook (name, content) VALUES (%s, %s);"
                cur.execute(sql, (name, content)) 
                conn.commit()
                cur.close()
                conn.close()
                return redirect(url_for('hello'))
                
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        conn = None


        return redirect(url_for('hello'))