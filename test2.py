#below is the program to view the data in mysql from any browser with get method

from flask import Flask , request , jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route("/get_data")
def get_data():
    db = request.args.get('db')
    tn = request.args.get("tn")
    try:
        con = conn.connect(host='localhost',user='root',passwd='@Gmgaurav7' ,database= "{}".format(db))
        cur = con.cursor()
        cur.execute("select * from {}".format(tn))
        data = cur.fetchall()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(str(data))

if __name__ == '__main__':
    app.run(port=5004)