import json, os
import cPickle as pickle

DBLog = "data/db.txt"
DBPick = "data/db.p"
data = dict()

def load_data():
	global data
	if not os.path.exists(DBPick):
		data = dict()
	else:
		data = pickle.load(open(DBPick, "rb"))
	if not os.path.exists(DBLog):
		open(DBLog, 'w').close()
	
	with open(DBLog, "r") as myfile:
		for l in myfile.readlines():
			dat = json.loads(l)
			act = dat["action"]
			if act == "add":
				add(dat["key"], dat["value"], False)
			elif act == "remove":
				remove(dat["key"], False)
	
	pickle.dump(data, open(DBPick, "wb"))
	
	os.remove(DBLog)
	myfile = open(DBLog, "w").close()
	return myfile
	
def write_f(mstr):
	with open(DBLog, 'a') as file:
		file.write(mstr + "\n")

def all():
	return data

def get(key):
	return data[key]

def add(key, value, store = True):
	data[key] = value
	if store:
		#print json.dumps({"key":key, "action":"add", "value":value })
		write_f(json.dumps({"key":key, "action":"add", "value":value }))

def remove(key, store = True):
	if key not in data:
		return
	del data[key]
	if store:
		write_f(json.dumps({"key":key, "action":"remove" }))


file = load_data()