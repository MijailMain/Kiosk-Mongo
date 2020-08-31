# Mongo
from pymongo import MongoClient
# Flask
from flask import Flask, request
from flask import render_template
from flask import jsonify

# Cors
from flask_cors import CORS

# FecHa
from datetime import date
from datetime import datetime

# Cors access
app=Flask(__name__)
cors = CORS(app)

Server = '192.168.100.3'
ServerMongo = '192.168.100.14'

# Setting Mongo
client = MongoClient(ServerMongo, username='Admin', password='Admin')
db = client['Kiosk']
collections = db['Kiosk']

print ("/aggregator/length/")
print ("/aggregator/data/<Id>")

#//////////////////////////////////////////////////////////////////////////
# Index
#//////////////////////////////////////////////////////////////////////////
@app.route('/')
def hello_world():

    return render_template('index.html')
    

#***************************************************************************
#//////////////////////////////////////////////////////////////////////////
# LOGIN
#//////////////////////////////////////////////////////////////////////////
#***************************************************************************
#######################################
# Login User
#######################################
@app.route('/aggregator/data/<Id>', methods=[ 'Get'])
def CustomRule(Id):

    print ("   - New Request Aggregator data: ",Id)
    
    # resulT
    Data = []
    value = db.KioskData.count(); 
    value2 = db.KioskData.find({}, {"_id":0})

    print (db)
    print (value)

    for registro in value2:
            Data.append(registro)

    return jsonify(Data[int(Id)])
    
#######################################
# length User
#######################################
@app.route('/aggregator/length/', methods=[ 'Get'])
def length():
    
    value = db.KioskData.count(); 
    print ("   - New Request Aggregator length: ",value)

    return jsonify({"length": value})
    


#***************************************************************************
#//////////////////////////////////////////////////////////////////////////
# Host Api
#//////////////////////////////////////////////////////////////////////////
#***************************************************************************
if __name__ == '__main__':
    app.run(host=Server, port=5080, debug=True)


