from flask import Flask, render_template, request
import sqlite3 
import json
app = Flask(__name__)

""" 
con = sqlite3.connect("meter.db")  
print("Database opened successfully")  
con.execute("create table Meters (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
con.execute("create table Meter (id INTEGER PRIMARY KEY AUTOINCREMENT, meter_id INTEGER, timestamp TEXT DEFAULT CURRENT_TIMESTAMP, value INTEGER, CONSTRAINT fk_meters FOREIGN KEY (id)  REFERENCES meters(id))")  
print("Table created successfully")  
"""

@app.route("/meters/")  
def view():  
    con = sqlite3.connect("meter.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from meters")  
    rows = cur.fetchall()  
    return render_template("list_meters.html",rows = rows) 
 
@app.route('/meter/<int:meter_id>/')
def meter(meter_id):  
    con = sqlite3.connect("meter.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor() 
    query= "select s.name, m.timestamp, m.value from meter m, meters s where m.meter_id =s.id and m.meter_id= ?"
    print(query)
    print(meter_id,type(meter_id))
    cur.execute(query,[meter_id])   
    json_list = []
    for row in cur.fetchall():
        json_dict = {'name': row[0], 'timestamp': row[1], 'value': row[2]}
        json_list.append(json_dict)
    print(json.dumps(json_dict))
    return (json.dumps(json_dict))

 
if __name__ == '__main__':
    app.run(debug = True)