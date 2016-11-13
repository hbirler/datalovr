import learn
from data import cases, edges, eid, ci
from numpy import array, concatenate, random
from learn import nonlinear_transform, log_reg, check_w, sigmoid
import store
from itertools import chain

#print cases

def get_edge(edge, limit):
	for i, e in enumerate(edges):
		if i >= limit:
			return None
		if e[0] == edge:
			return i
	return None

def transform_case(case, edallow = 24):
	nods = [0 for i in xrange(len(eid))]
	meds = [0 for i in xrange(edallow + 1)]
	vals = list(case[1])
	for i,e in enumerate(case[0]):
		#print e
		nods[e[0]] = 1
		
		if i == 0:
			continue
		mk = (case[0][i-1][0], case[0][i][0])
		pos = get_edge(mk, edallow)
		if pos is None:
			meds[edallow] = 1
		else:
			meds[pos] = 1
	return array(nods+meds+vals)
	#return array( nonlinear_transform(nods + meds + vals) )
	#return array( concatenate((nonlinear_transform(nods), nonlinear_transform(meds), nonlinear_transform(vals))) )


def transform_edge(edge, vals):
	nod1 = [0 for i in xrange(len(eid))]
	nod2 = [0 for i in xrange(len(eid))]
	vals = [v for v in vals]
	nod1[edge[0]] = 1
	nod2[edge[1]] = 1
	return array(nod1 + nod2 + vals)
	#return array(nod1 + nod2 + vals)

def transform_edges(case, val):
	retv = []
	for i,e in enumerate(case[0]):
		if i == 0:
			continue
		mk = (case[0][i-1][0], case[0][i][0])
		#retv.append(nonlinear_transform(transform_edge(mk, case[1])))
		retv.append((val, transform_edge(mk, case[1])))
	return retv


last_wc = None
last_we = None
last_N = 0

def calculate_we():
	db = store.all()
	kk = db.keys()
	Xy = []
	for key in kk:
		Xy += transform_edges(cases[key], db[key])
	print Xy[0]
	X = array([v[1] for v in Xy])
	y = array([v[0] for v in Xy])
	print db
	print y
	
	print X.shape
	print y.shape
	
	w = log_reg(X, y)
	
	global last_we
	global last_N
	
	last_we = w
	last_N = len(kk)

def calculate_wc():
	db = store.all()
	kk = db.keys()
	X = array([transform_case(cases[key]) for key in kk])
	y = array([db[key] for key in kk])
	print db
	print y
	
	print X.shape
	print y.shape
	
	w = log_reg(X, y)
	
	global last_wc
	global last_N
	
	last_wc = w
	last_N = len(kk)

def calculate_cases(checkcases):
	db = store.all()
	kk = db.keys()
	N = len(kk)
	
	if N - last_N >= 1 or last_wc is None:
		calculate_wc()
	
	rez = array([(key, check_w(last_wc, transform_case(case))) for key, case in checkcases])
	return rez

def calculate_edges(case):
	db = store.all()
	kk = db.keys()
	N = len(kk)
	
	if N - last_N >= 1 or last_we is None:
		calculate_we()
	
	mx = [v[1] for v in transform_edges(case, 0)]
	rez = array([check_w(last_we, edge) for edge in mx])
	return rez

def sample_group(fr=0, to=500):
	return [{"key":t[0], "val":t[1]} for t in calculate_cases(ci[fr:to])]

#print sample_group()
#print calculate_cases()
#print calculate_cases()
#print calculate_cases()
#print calculate_cases()
#print calculate_cases()

#mit = cases.items()[0][1]
#print mit
#print len(transform_case(mit))
#print len(transform_edges(mit)[0])

