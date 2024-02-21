#first we do all the imports neede to perform the task
from flask import Flask , request , jsonify
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",passwd="@Gmgaurav7")
cursor = mydb.cursor()

app = Flask(__name__)

#below is the program to insert a data into a given sql database using flask api
@app.route("/insert",methods=['POST'])
def insert_data():
    if request.method == "POST":
        name = request.json["name"]
        number = request.json["num"]
        cursor.execute("insert into mysqltask.mysqltable values (%s , %s)",(name,number))
        mydb.commit()
        return jsonify(str("Inserted Successfully"))


#below is the program to update data into a given sql database using flask api
@app.route('/update',methods = ['POST'])
def update_data():
    if request.method == 'POST':
        n_name = request.json['name']
        n_num = request.json['num']
        cursor.execute("update mysqltask.mysqltable set number = %s where name = %s " , (n_num , n_name))
        mydb.commit()
        return jsonify(str("Updated Successfully"))

#below is the program to delete a data into a given sql database using flask api
@app.route('/delete', methods=['POST'])
def delete_entry():
    if request.method == 'POST':
        del_name = request.json['del_name']
        cursor.execute("delete from mysqltask.mysqltable where name = %s " , (del_name ,))
        mydb.commit()
        return jsonify(str("Successfully Deleted"))

#below is the program to fetch the data available in given sql database using flask api
@app.route('/fetch', methods=['POST'])
def fetch_data():
    if request.method == 'POST':
        cursor.execute("select * from mysqltask.mysqltable")
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(str(l))

#below code is used for running the flask app it Starts the Flask web server if the script is executed directly.
if __name__ == "__main__":
    app.run()