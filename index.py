from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", year=datetime.now().year)

@app.route("/api/greet")
def greet():
    name = request.args.get("name", "অতিথি")
    return jsonify({"message": f"হ্যালো, {name}!", "time": datetime.now().isoformat()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
