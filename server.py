from flask import Flask, render_template, jsonify
from data import CQuery, sample_query
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/get")
def get():
	mq = sample_query()
	return mq.get_json()

@app.route("/set/<int:id>")
def set(id):
	return "success"

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)