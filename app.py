"""importing the flask library requirements."""

"""import forms"""
from flask import Flask, render_template, redirect, request, url_for
from forms import CreateLockForm, UpdateLockForm, ConfirmDelete

"""importing the flask pymongo."""
from flask_pymongo import PyMongo

"""From the bson library we import ObjectId."""
from bson.objectid import ObjectId

"""Importing the Operating System."""
import os

"""Os path if function."""
if os.path.exists("env.py"):
    import env

"""Defining app, app configuration and mongo."""
app = Flask(__name__)
app.config[
    'MONGO_URI'] = 'mongodb+srv://bootRoot90:MsObongo1990@myFirstCluster-lw6no.mongodb.net/DataCentricLocksProject.Locks?retryWrites=true&w=majority'
app.config['MONGO_DBNAME'] = 'DataCentricLocksProject'
mongo = PyMongo(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


"""This code looks for the index page and finds mongodb data."""
@app.route('/')
@app.route('/index')
def index():
    context = mongo.db.Locks.find()
    return render_template('index.html', locks=context)


"""This code adds a lock and render add lock page."""
@app.route('/add_lock', methods=['GET', 'POST'])
def add_lock():
    form = CreateLockForm(request.form)
    if form.validate_on_submit():
        lock = mongo.db.Locks
        lock.insert_one({
            'brand': request.form['brand'],
            'description': request.form['description'],
            'pros': request.form['pros'],
            'cons': request.form['cons']
        })
        return redirect(url_for('index'))
    return render_template('add_lock.html', form=form)


"""Edit lock in database"""
@app.route('/edit_lock/<lock_id>', methods=['GET', 'POST'])
def edit_lock(lock_id):
    lock = mongo.db.Locks
    lock_db = lock.find_one_or_404({'_id': ObjectId(lock_id)})
    if request.method == 'GET':
        form = UpdateLockForm(data=lock_db)
        return render_template('edit_lock.html', lock=lock_db, form=form)
    form = UpdateLockForm(request.form)
    if form.validate_on_submit():
        locks_db = mongo.db.Locks
        locks_db.update_one({
            '_id': ObjectId(lock_id),
        }, {
            '$set': {
                'brand': request.form['brand'],
                'description': request.form['description'],
                'pros': request.form['pros'],
                'cons': request.form['cons'],
            }
        })
        return redirect(url_for('index'))
    return render_template('edit_lock.html', lock=lock_db, form=form)


"""Remove lock in database and render index page"""
@app.route('/delete_lock/<lock_id>', methods=['GET', 'POST'])
def delete_lock(lock_id):
    lock_db = mongo.db.Locks.find_one_or_404({'_id': ObjectId(lock_id)})
    if request.method == 'GET':
        form = ConfirmDelete(data=lock_db)
        return render_template('delete_lock.html', form=form)
    form = ConfirmDelete(request.form)
    if form.validate_on_submit():
        locks_db = mongo.db.Locks
        locks_db.delete_one({
            '_id': ObjectId(lock_id),
        })
        return redirect(url_for('index'))
    return render_template('delete_lock.html', lock=lock_db, form=form)


"""Get lock details"""
@app.route('/get_single_lock/<lock_id>')
def get_single_lock(lock_id):
    return render_template('lock_detail.html',
                           locks=mongo.db.Locks.find_one({'_id': ObjectId(lock_id)}))

"""Lock listing"""
@app.route('/get_all_locks/<locks_id>')
def get_all_locks(locks_id):
    return render_template('lock_list.html', locks=mongo.db.Locks.find())


"""if statement with the app.run method."""
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
