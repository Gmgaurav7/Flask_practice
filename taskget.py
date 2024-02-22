from flask import Flask , request

app = Flask(__name__)

@app.route('/test')
def flaskget():
    name = request.args.get("name")
    email = request.args.get("email")
    mobile = request.args.get("Num")
    return " Name = {} , E-mail = {}, Mobile No. = {}".format(name , email , mobile)

if __name__ == '__main__':
    app.run(port=5002)