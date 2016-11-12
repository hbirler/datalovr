import numpy, random
from numpy import  array, random, exp, seterr, dot, copy, log
from numpy.linalg import norm
from itertools import combinations,combinations_with_replacement, chain
from operator import mul

def sigmoid(s):
	return exp(s) / (1+exp(s))

def check_w(w,p):
	return sigmoid(dot(w,p))
	
def nonlinear_transform(v, deg=2):
	n = len(v)
	ss = ((i,) for i in xrange(n))
	for i in range(2, deg+1):
		nn = combinations_with_replacement(xrange(n), i)
		ss = chain(ss, nn)
	
	retv = chain((1,) ,(reduce(mul, (v[i] for i in tup)) for tup in ss))
	return array(list(retv))

print nonlinear_transform([1,2])

def log_reg(X, y, eta = 0.01, eps = 0.001):
	N = len(X)
	w = array(np.zeros(N))
	wp = array(np.ones(N))
	
	eco = 0
	while True:
		Xi = random.permutation(len(X))
		for i in Xi:
			decay = 2 * eta * lamb / N
			w = w*(1 - decay) + eta * (y[i] * X[i] * (1 / (1+exp(y[i] * dot(w.T, X[i])) ) ) )
		eco += 1
		if norm(wp - w) < eps:
			break
		wp = copy(w)
	
	return w