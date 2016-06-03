__author__ = 'Paolo Garcia and Conor Cousins'
import sqlite3
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def main():
    print(render_template('index.htm'))
    firstname = ''
    lastname = ''
    age = None
    email = ''
    photo = ''
    bio = ''

    if request.method == 'GET':
        conn = sqlite3.connect('profiles.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        print (row)
        if row:
            firstname = row[0]
            lastname = row[1]
            age = row[2]
            email = row[3]
            photo = row[4]
            bio = row[5]
        conn.close()
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastnmae']
        age = request.form[age]
        email = request.form['email']
        photo = request.form['photo']
        bio = request.form['bio']
        conn = sqlite3.connect('profiles.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row:
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, photo = ?, bio = ?''',
                (firstname, lastname, age, email, photo, bio))
        else:
            c.execute('''INSERT INTO members VALUES(?,?,?,?,?,?)''',
                      (firstname, lastname, age, email, photo, bio))
        conn.commit()
        conn.close()
    return render_template('index.htm')
@app.route('/view')
def view():
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('profiles.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM members''')
    row = c.fetchone()
    print (row)

    if row:
        firstname = row[0]
        lastname = row[1]
        age = row[2]
        email = row[3]
        photo = row[4]
        bio = row[5]

    conn.close()
    return render_template('view_page.htm', firstname = firstname,
                           lastname = lastname, age=age, email=email, photo=photo, bio=bio)

def get(request):
    pass
def post(request):
    pass

if __name__== "__main__":
    app.run(debug=True)