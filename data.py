from flask import jsonify
import csv
from itertools import groupby
import cPickle as pickle
import random

class CQuery:
	def __init__(self, mid = "", title = "", text = "", opts = []):
		self.id = mid
		self.title = title
		self.text = text
		self.opts = opts
	@staticmethod
	def from_case(mid, case):
		print case
		return CQuery(mid,"Title",str(case),["a","b","c"])
	
	def get_dict(self):
		return {"id":self.id, "title":self.title, "text":self.text, "opts": self.opts}
	
	def get_json(self):
		return jsonify(self.get_dict())

def read_data():
	cases = None
	kis = None
	with open("cases.csv") as f:
		cases = [row for row in csv.reader(f.readlines(), delimiter=";")]
	#with open("throughput.csv") as f:
	#	through = [row for row in csv.reader(f.readlines(), delimiter=";")]
	with open("kis.csv") as f:
		kis = [row for row in csv.reader(f.readlines(), delimiter=";")]
	#print through
	return cases[1:], kis[1:]

def process_data():
	cases, kis = read_data()
	pid = dict(reversed(x) for x in enumerate(set(e[1] for e in kis)))
	
	ks = dict((t[0], (pid[t[1]],int(t[2]),int(t[3]),int(t[4]),int(t[5]) )) for t in kis if t[2] != '')
	cases = [c for c in cases if c[0] in ks]
	es = list(set(e[1] for e in cases))
	
	eid = dict(reversed(x) for x in enumerate(es))
	
	
	ckeys = list(set(e[0] for e in cases))
	
	ces = dict((key, [(s[1], s[2]) for s in sorted([g for g in group], key = lambda x: x[2])]  ) for key, group in groupby(((c[0], eid[c[1]], c[2]) for c in cases), lambda c: c[0]))
	
	cs = [(key, ces[key], ks[key]) for key in ckeys] 
	
	#print cs
	return cs, eid, pid
	
def save_data():
	cs, eid, pid = process_data()
	data = (cs, eid, pid)
	pickle.dump(data, open("data.p", "wb"))
	pass

def load_data():
	data = pickle.load(open("data.p", "rb"))
	cs, eid, pid = data
	#print cs
	return cs, eid, pid

#save_data()
cs, eid, pid = load_data()

lolol = CQuery.from_case("123",random.choice(cs))
print eid

def sample_query():
	return CQuery.from_case("123",random.choice(cs))
	#return CQuery("123","Topkek","Ayy lmaoo",["Topkek","Tanzen","Oww yeah"])
	
	
	









"""

class Env:
	def __init__(self, events, edges, cases):
		self.events = events
		self.edges = edges
		self.cases = cases
		pass

class Event:
	def __init__(self, key, name):
		self.key = key
		self.name = name
		pass

class Edge:
	def __init__(self, fr, to):
		self.fr = fr
		self.to = to
		pass

class Case:
	def __init__(self, key, events, value):
		self.key = key
		self.events = events
		self.value = value
		pass
"""