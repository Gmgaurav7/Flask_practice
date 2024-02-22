from flask import Flask , request , jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Gmgaurav7:Swizzler007@gaurav123.xzfouhd.mongodb.net/?retryWrites=true&w=majority&appName=Gaurav123")
db = client['taskdb']
collection = db['taskcollection']

@app.route('/minsert' , methods = ['GET' , 'POST'])
def insert_data():
    if request.method == "POST":
        name = request.json["name"]
        number = request.json["num"]
        collection.insert_one({name:number})
        return jsonify(str("Inserted Successfully"))

if __name__ == '__main__':
    app.run(port= 5001)

