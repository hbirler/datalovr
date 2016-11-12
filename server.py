from flask import Flask, render_template, jsonify, request
from data import CQuery, sample_query
import store
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index_ajax.html")
	#return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_get():
	mq = sample_query()
	#print mq.get_dict()
	return render_template("index.html",**mq.get_dict())

@app.route("/get", methods=['POST'])
def get_post():
	mq = sample_query()
	return mq.get_json()

@app.route("/set/<int:key>", methods=['POST'])
def set(key):
	content = request.get_json(silent=True)
	value = content["resp"]
	store.add(key, value)
	return "success"

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)