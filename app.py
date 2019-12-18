from flask import Flask, render_template
from flask_pymongo import PyMongo
from config import Config

import os

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://bootRoot90:MsObongo1990@myfirstcluster-lw6no.mongodb.net/test?retryWrites=true&w=majority"
app.config['MONGO_DBNAME'] = 'DataCentricLocksProject'
app.config.from_object(Config)
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    context = mongo.db.Locks.find()
    print(context)

    return render_template('index.html', locks=context)



if __name__ == '__main__':
    app.run()
