import re

class Polynome():
	def __init__(self, line):
		self.coef = 0
		self.power = 0
		self.parsing(line)

	def parsing(self, line):

		if line.find('X') is -1:
			self.coef = float(line)
		else:
			if line.find('*') is not -1:
				self.coef = float(re.findall(r'(.+(?=\*X))', line)[0])
			else:
				if line[0] is '-':
					self.coef = -1
				else:
					self.coef = 1
			if line.find('^') is not -1:
				self.power = float(re.findall(r'((?!.*\^).+)', line)[0])
			else:
				self.power = 1

	def __str__(self):
		res = ""
		if self.coef < 0:
			res += "- {0:g}".format(self.coef * -1)
		else: 
			res += "{0:g}".format(self.coef)
		return res + " * X^{0:g}".format(self.power)
