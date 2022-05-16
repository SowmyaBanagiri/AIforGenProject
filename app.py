
from flask import (
Flask, 
g,
render_template, 
redirect, 
url_for, 
request, 
session,
url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def _repr_(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password123'))
users.append(User(id=2, username='Bethany', password='password'))


app = Flask(__name__)
app.secret_key = 'somesecretkey'

@app.before_request
def before_request():
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['userName']
        password = request.form['userPassword']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            print(user.password,user.username)
            return redirect(url_for('profile'))

        return redirect(url_for('login')) 
        '''redirect back to login page if username is wrong'''

    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')





    