# importing the flask library requirements.
from flask import Flask, render_template, redirect, request, url_for

# importing the flask pymongo.
from flask_pymongo import PyMongo

# From the bson library we import ObjectId.
from bson.objectid import ObjectId

# Importing the Operating System.
import os

# Os path if function.
if os.path.exists("env.py"):
    import env

# Defining app, app configuration and mongo.
app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
app.config['MONGO_DBNAME'] = 'DataCentricLocksProject'
mongo = PyMongo(app)

# This code looks for the index page and finds mongodb data.
@app.route('/')
@app.route('/index')
def index():
    context = mongo.db.Locks.find()
    print(context)
    return render_template('index.html', locks=context)

# This code adds a lock to the database.
@app.route('/add_lock', methods=['GET', 'POST'])
def add_lock():
    if request.method == 'POST':
        # Grab content of form and push to database
        return render_template('add_lock.html')


@app.route('/insert_lock', methods=['POST'])
def insert_lock():
    lock = mongo.db.Locks
    lock.insert_one(request.form.to_dict())
    return redirect(url_for('/index'))


@app.route('/edit_lock/<Locks_id>')
def edit_lock(lock_id):
    the_lock = mongo.db.locks.find_one({'_id': ObjectId(lock_id)})
    all_locks = mongo.db.locks.find()
    return render_template('edit_lock.html', lock=the_lock, locks=all_locks)


# if statement with the app.run method.
    if __name__ == '__main__':

        app.run(host='0.0.0.0',
                port=(os.environ.get('PORT')),
                debug=True)
