import learn
from data import cases, edges, eid
from numpy import array, concatenate
from learn import nonlinear_transform
import store

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
		print e
		nods[e[0]] = 1
		
		if i == 0:
			continue
		mk = (case[0][i-1][0], case[0][i][0])
		pos = get_edge(mk, edallow)
		if pos is None:
			meds[edallow] = 1
		else:
			meds[pos] = 1
	return array( nonlinear_transform(nods + meds + vals) )
	#return array( concatenate((nonlinear_transform(nods), nonlinear_transform(meds), nonlinear_transform(vals))) )


mit = cases.items()[0][1]
print mit
print len(transform_case(mit))

def transform_edge(edge, vals):
	nod1 = [0 for i in xrange(len(eid))]
	nod2 = [0 for i in xrange(len(eid))]
	vals = [v for v in vals]
	nod1[edge[0]] = 1
	nod2[edge[1]] = 1
	
	return array(nod1 + nod2 + vals)

def transform_edges(case):
	retv = []
	for i,e in enumerate(case[0]):
		if i == 0:
			continue
		mk = (case[0][i-1][0], case[0][i][0])
		retv.append(nonlinear_transform(transform_edge(mk, case[1])))
	return array(retv)


print len(transform_edges(mit)[0])

