import learn
import data
import store

def get_edge(edge, limit):
	for i, e in enumerate(edges):
		if i >= limit:
			return None
		if e[0] == edge:
			return i
	return None

def transform_case(case):
	pass

def transform_edge(case):
	pass