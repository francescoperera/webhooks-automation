from flask import json
from flask import request
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Home"



@app.route("/github", methods=["POST"])
def read_event():
    if request.headers["Content-Type"] == "application/json":
        payload = json.dumps(request.json)
        print(payload)
        return payload





if __name__ == "__main__":
    app.run(debug=True, port="2001")