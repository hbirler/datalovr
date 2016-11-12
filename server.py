from flask import Flask, render_template, jsonify, request
from flask.ext.cache import Cache
from data import CQuery, sample_query, cases, eid, die
import store
import machinel
app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

def perc(flo):
	return int(min(1,max(float(flo),0))*100)

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

@app.route("/set/<key>", methods=['POST'])
def set(key):
	content = request.get_json(silent=True)
	value = content["resp"]
	store.add(key, value)
	return "success"

@app.route("/case/<key>", methods=['GET'])
def case(key):
	kv = machinel.calculate_cases([(key, cases[key])])[0][1]
	edgs = [0] + list(machinel.calculate_edges(cases[key]))
	print edgs
	events = [{"name":die[int(e[0])],"perc":perc(v)} for e,v in zip(cases[key][0],edgs)]
	events[0]["perc"] = -100
	dc = {"key":key, "value":perc(kv), "events":events}
	return render_template("case.html", **dc)

@app.route("/caseempty", methods=['GET'])
def case_empty(key):
	return render_template("case_empty.html")


@app.route("/admin", methods=['GET'])
def admin():
	return render_template("admin.html")



#@cache.cached(timeout=60)
@app.route("/admin", methods=['POST'])
def admin_post():
	content = request.get_json(silent=True)
	fr = 0 if content is None or "from" not in content else int(content["from"])
	to = fr + 500 if content is None or "to" not in content else int(content["to"])
	to = min(to, len(cases))
	group = {"list":machinel.sample_group(fr, to)}
	#print group
	return jsonify(**group)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)