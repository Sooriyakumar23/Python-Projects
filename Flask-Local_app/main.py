from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ("Hello Sooriyakumar's World !!!!!")

@app.route('/ai', methods=['GET'])
def office():
    return(render_template("index.html"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return (render_template("login.html"))
    else:
        user = request.form["username"]
        passcode = request.form["password"]

        if user == "Sooriyakumar" and passcode == "1234":
            message = "Login successful"
        else:
            message = "Login failed !"

        return (render_template("status.html", message=message))

if __name__ == '__main__':
    app.run(port=2305, debug=True)
