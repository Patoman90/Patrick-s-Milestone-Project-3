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
    print(context.__dict__)
    return render_template('index.html', locks=context)


# This code adds a lock and render add lock page.
@app.route('/add_lock', methods=['GET', 'POST'])
def add_lock():
    if request.method == 'POST':
        return render_template('add_lock.html')
    return render_template('add_lock.html')


# Create lock in database
@app.route('/insert_lock', methods=['POST'])
def insert_lock():
    lock = mongo.db.Locks
    lock.insert_one(request.form.to_dict())
    return redirect(url_for('/index'))


# Edit lock in database
@app.route('/edit_lock/<lock_id>')
def edit_lock(lock_id):
    the_lock = mongo.db.locks.find_one({'_id': ObjectId(lock_id)})
    all_locks = mongo.db.locks.find()
    return render_template('edit_lock.html', lock=the_lock, locks=all_locks)


# Update lock in database and redirect to index page

@app.route('/update_lock/<lock_id>', methods=["POST"])
def update_lock(lock_id):
    mongo.db.locks.update(
        {'_id': ObjectId(lock_id)},
        {
           'lock_Brand': request.form.get('lock_Brand'),
           'lock_Description': request.form.get('lock_Description'),
           'lock_Pros': request.form.get('lock_Pros'),
           'lock_Cons': request.form.get('lock_Cons')
        }
    )
    return redirect(url_for('/index.html'))


# Remove lock in database and render index page
@app.route('/delete_lock/<lock_id>')
def delete_lock(lock_id):
    mongo.db.locks.remove({'_id': ObjectId(lock_id)})
    return redirect(url_for('index'))


# Find lock in database and render list of locks
@app.route('/get_lock')
def get_lock():
    return render_template('lock_list.html',
                           locks=mongo.db.Locks.find())


# Get lock details
@app.route('/get_single_lock/<lock_id>')
def get_single_lock(lock_id):
    return render_template('lock_detail.html',
                           locks=mongo.db.Locks.find_one({'_id': ObjectId(lock_id)}))


# Edit lock in and render edit database page
@app.route('/edit_data/<lock_id>')
def edit_data(lock_id):
    return render_template('edit_lock.html',
                           locks=mongo.db.locks.find_one({'_id': ObjectId(lock_id)}))


# if statement with the app.run method.
if __name__ == '__main__':

    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
