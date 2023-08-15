from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Welcome to Home page<h1>"

@app.route("/add", methods=["POST"])
def addition():
    if request.method =="POST":
        result = int(request.json["num1"]) + int(request.json["num2"])
        return jsonify(f"The summarion of two number is {result}")



if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5002)