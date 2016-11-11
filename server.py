from flask import Flask, render_template, jsonify
from data import CQuery, sample_query
app = Flask(__name__)

@app.route("/")
def index():
	return get_get()
	#return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_get():
	mq = sample_query()
	print mq.get_dict()
	return render_template("index.html",**mq.get_dict())

@app.route("/get", methods=['POST'])
def get_post():
	mq = sample_query()
	return mq.get_json()

@app.route("/set/<int:id>")
def set(id):
	return "success"

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)