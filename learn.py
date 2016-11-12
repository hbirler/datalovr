import numpy, random
from numpy import  array, random, exp, seterr, dot, copy, log, vectorize, tanh
from numpy.linalg import norm
from itertools import combinations,combinations_with_replacement, chain
from operator import mul
from sklearn.neural_network import MLPRegressor


from sklearn import svm


def log_reg(X, y):
	y = y.reshape((-1, 1))
	#clf = svm.SVC(probability = True)
	clf = MLPRegressor(hidden_layer_sizes=(30,10), activation="tanh")
	clf.fit(X, y)
	return clf


def check_w(w,p):
	return w.predict((p,))[0]

def sigmoid(s):
	return 1 / (1+1/exp(s))

def sigmoid_v(s):
	return 1 / (1+1/exp(s))

sigmoid_v = vectorize(sigmoid_v)
"""
def check_w(w,p):
	return sigmoid(dot(w,p))
"""
def nonlinear_transform(v, deg=2):
	n = len(v)
	ss = ((i,) for i in xrange(n))
	for i in range(2, deg+1):
		nn = combinations_with_replacement(xrange(n), i)
		ss = chain(ss, nn)
	
	retv = chain((1,) ,(reduce(mul, (v[i] for i in tup)) for tup in ss))
	return array(list(retv))

print nonlinear_transform([1,2])
"""
def log_reg(X, y, eta = 0.1, eps = 0.01, lamb = 0.01):
	N = len(X)
	w = numpy.random.uniform(-1,1,len(X[0]))
	#w = numpy.zeros(len(X[0]))
	wp = w - array(numpy.ones(len(X[0])))
	sigmoid_v(X)
	eco = 0
	while True:
		Xi = random.permutation(len(X))
		for i in Xi:
			decay = 2 * eta * lamb / N
			#print y[i]
			#print w
			#print i, y[i] * dot(w.T, X[i])
			w = w*(1 - decay) + eta * (y[i] * X[i] * (1.0 / (1+exp(y[i] * dot(w.T, X[i])) ) ) )
		eco += 1
		#print eco
		if norm(wp - w) < eps or eco > 100000:
			break
		wp = copy(w)
	
	return w
"""