from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://bootRoot90:MsObongo1990@myFirstCluster-lw6no.mongodb.net/DataCentricLocksProject.Locks?retryWrites=true&w=majority'
app.config['MONGO_DBNAME'] = 'DataCentricLocksProject'
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    context = mongo.db.Locks.find()
    print(context)

    return render_template('index.html', locks=context)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
