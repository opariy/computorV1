
from modules.Polynome import *

def maxPower(pols):
	maxPol = 0

	for x in pols:
		if x.power > maxPol:
			maxPol = x.power

	return maxPol

def isPol(pols, cur):
	for x in pols:
		if x.power == cur:
			return True
	return False

def minimize(pols):
	maxPol = maxPower(pols)
	count = 0;
	res = []

	while (count <= maxPol):
		if isPol(pols, count):
			tmp = Polynome("0*X^{0}".format(count))
			for x in pols:
				if x.power == count:
					tmp.coef += x.coef
			if (tmp.coef) != 0:
				res.append(tmp)
		count += 1
	pols = res
	res = ""

	for i, x in enumerate(pols):
		if x.coef < 0:
			res += " {0}".format(x)
		# elif i == 0:
		# 	res += "0"
		else:
			if (i != 0):
				res += " + {0}".format(x)
			else:
				res += " {0}".format(x)
	if not pols:
		res += "0"
	res += " = 0"
	print("Reduced form: " + res)
	return pols
