from modules.Polynome import *

# perepisat

class colors:
	OKGREEN = '\033[92m'
	OKBLUE = '\033[94m'
	ENDC = '\033[0m'


def square_root(a):
	i = 0
	while (i * i) <= a:
		i += 0.1
	x1 = i
	x2 = i
	j = 0
	while j < 10:
		x2 = a
		x2 /= x1;
		x2 += x1;
		x2 /= 2;
		x1 = x2
		j += 1
	return x2

def calculate_d(a, b , c):
	d = b ** 2 - 4 * a * c
	print("D = b² - 4ac = {0:g}² - 4 * {1:g} * {2:g} = {3:g}".format((b), a, c, d))
	return d

def zero_d(a, b, c):
	result = -b / (2 * a)
	print("-b / (2 * a) = {0:g} / (2 * {1:g}) = {2:g}".format(-b, a, result))
	# print ("x = {0:g}".format(result))
	print ("{1}x = {0:g}{2}".format(result, colors.OKGREEN, colors.ENDC))
	return ([0, result])


def negative_d(a,b,c,d):
	x1 = (-b + d ** (0.5)) / (2 * a)
	x2 = (-b - d ** (0.5)) / (2 * a)
	print("x1 = (-b + √D) / (2 * a) = ({0:g} + √{3:g}) / (2 * {1:g}) = {2:g}".format(-b, a, x1, d))
	print("x2 = (-b - √D) / (2 * a) = ({0:g} - √{3:g}) / (2 * {1:g}) = {2:g}".format(-b, a, x2, d))
	print ("{1}x1 = {0:g}{2}".format(x1, colors.OKGREEN, colors.ENDC))
	print ("{1}x2 = {0:g}{2}".format(x2, colors.OKGREEN, colors.ENDC))
	return ([-1, x1, x2])


def positive_d(a,b,c,d):
	x1 = (-b + square_root(d)) / (2 * a)
	x2 = (-b - square_root(d)) / (2 * a)
	print("x1 = (-b + √D) / (2 * a) = ({0:g} + √{3:g}) / (2 * {1:g}) = {2:g}".format(-b, a, x1, d))
	print("x2 = (-b - √D) / (2 * a) = ({0:g} - √{3:g}) / (2 * {1:g}) = {2:g}".format(-b, a, x2, d))
	print ("{1}x1 = {0:g}{2}".format(x1, colors.OKGREEN, colors.ENDC))
	print ("{1}x2 = {0:g}{2}".format(x2, colors.OKGREEN, colors.ENDC))
	return ([1, x1, x2])


def solve_quardatic(pols):
	a = b = c = 0
	for p in pols:
		if (p.power == 2):
			a = p.coef
		elif (p.power == 1):
			b = p.coef
		elif (p.power == 0):
			c = p.coef
			
	d = calculate_d(a, b , c)

	print ("{1}Discriminant is: {0:g}{2}".format(d, colors.OKBLUE, colors.ENDC))

	if (d > 0):
		print ("Discriminant is strictly positive, the two solutions are:")
		return (positive_d(a, b, c, d))

	elif (d == 0):
		print ("The solution is:")
		return (zero_d(a, b, c))
	else:
		print ("Discriminant is strictly negative, the two solutions are:")
		return (negative_d(a, b, c, d))
		


def solve_linear(pols):
	if (len(pols) == 2):
		result = -1 * pols[0].coef / pols[1].coef
	else:
		result = 0
	print ("The solution is: {1}{0:g}{2}".format(result, colors.OKGREEN, colors.ENDC))
		# print ("{1}x1 = {0:g}{2}".format(x1, colors.OKGREEN, colors.ENDC))

	return ([2, result])


def solution(pols):
	res = []
	if len(pols) == 0 :
		print ("Polynomial degree: 0")
		print ("All real numbers are solution")
	else:
		print ("Polynomial degree: " + str(int(pols[len(pols) - 1].power)))
		if (pols[len(pols) - 1].power > 2):
			print("The polynomial degree is stricly greater than 2, I can't solve.")
			return
		elif (pols[len(pols) - 1].power == 2):
			res = solve_quardatic(pols)
		elif (pols[len(pols) - 1].power == 1):
			res = solve_linear(pols)
		elif (pols[len(pols) - 1].power == 0):
			print("No solution")
		return (res)


