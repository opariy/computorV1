import matplotlib.pyplot as plt
import numpy as np
from modules.Polynome import *


minus = -1
nul = 00
plus = 1
linear = 2
RANGE = 20


def graph(equation, results):

	pow_0 = Polynome("0")
	pow_1 = Polynome("0")
	pow_2 = Polynome("0")


	for x in equation:
		if (x.power == 2):
			pow_2 = x
		if (x.power == 1):
			pow_1 = x
		if (x.power == 0):
			pow_0 = x

	if not results:
		return
	if results[0] == minus:
		x = np.arange(-100, 100, 0.01)
	elif results[0] == nul or results[0] == linear:
		x = np.arange(float(results[1]) - RANGE, float(results[1]) + RANGE, 0.01)
	elif results[0] == plus:
		x = np.arange(float(min(results[1:])) - RANGE, float(max(results[1:])) + RANGE, 0.01)
	else:
		raise ValueError("Wrong discriminant")

	fig = plt.figure()
	ax = fig.add_subplot(111)
	fig.subplots_adjust(top=0.85)
	ax.set_xlabel('x')
	ax.set_ylabel('y')


	plt.axhline(0, color='grey')
	plt.axvline(0, color='grey')

	plt.plot(x, x ** 2 * float(pow_2.coef ) + x * float(pow_1.coef ) + float(pow_0.coef))


	fig = plt.gcf()
	fig.canvas.set_window_title('Computor V-1')
	plt.show()
