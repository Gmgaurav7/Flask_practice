from flask import Flask , request , jsonify
import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",passwd="@Gmgaurav7")
cursor = mydb.cursor()

app = Flask(__name__)
@app.route("/insert",methods=['POST'])
def insert_data():
    if request.method == "POST":
        name = request.json["name"]
        number = request.json["num"]
        cursor.execute("insert into mysqltask.mysqltable values (%s , %s)",(name,number))
        mydb.commit()
        return jsonify(str("Inserted Successfully"))



@app.route('/update',methods = ['POST'])
def update_data():
    if request.method == 'POST':
        n_name = request.json['name']
        n_num = request.json['num']
        cursor.execute("update mysqltask.mysqltable set number = %s where name = %s " , (n_num , n_name))
        mydb.commit()
        return jsonify(str("Updated Successfully"))


if __name__ == "__main__":
    app.run()