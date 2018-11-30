#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import random
from modules.Polynome import *
from modules.minimize import *
from modules.Solution import *
from modules.graph import *


def parsing(line):
	left = re.findall(r'.+(?=.*=)', line)[0]
	right = re.findall(r'(?!.*=).+', line)[0]

	left = re.findall(r'((?:[+-]?\d+(?:\.\d+)?(?:\*[A-Z])?(?:\^\d+)?)|[+-]?[A-Z](?:\^\d+)?)', left)
	right = re.findall(r'((?:[+-]?\d+(?:\.\d+)?(?:\*[A-Z])?(?:\^\d+)?)|[+-]?[A-Z](?:\^\d+)?)', right)

	leftPol = []
	for x in left:
		leftPol.append(Polynome(x))
	rightPol = []
	for x in right:
		rightPol.append(Polynome(x))
	for x in rightPol:
		x.coef *= -1;
	pols = leftPol + rightPol
	return pols

def main():
	line_array = [
		"x ^ 2 + 2 * x + 48 = 0",
		"x ^ 2 - 1 = 0",
		"x ^ 2 - 10 * x + 26 = 0",
		"-4 * x ^ 2 – 7 * x + 12 = 0",
		"6 * x ^ 1 = 23",
		"2 * x ^ 2 = 50",
		"1 * x ^ 1 = 0",
		"5 * x ^ 1 = 23",
		"456.464 * x ^ 1 = 23",
		"2 * X ^ 2 + 4 * X ^ 1 + 7= - 0",
		"x ^ 2 + x - 6 =0 ",
		"9 * x ^ 2 - 12 * x + 4 = 0"
		]
	visualization = 0




	if len(sys.argv) == 2:
		if (sys.argv[1] != "-v"):
			line = sys.argv[1]
		else:
			print ("Please enter an equation after the -v flag.")
			exit()
	elif len(sys.argv) == 3:
		if (sys.argv[1] == "-v"):
			line = sys.argv[2];
			visualization = 1
		else:
			print ("Please use -v flag to see the graph")
			exit()
	else:
		print ("Please enter an equation to be solved. Will use default:")
		ran = random.randint(0, 11)

		line = line_array[ran]
	try:
		line = line.upper()
		to_left = parsing(re.sub(r' ', '', line))

		minimized = minimize(to_left)
		results = solution(minimized)


		if visualization == 1 and minimized[len(minimized) - 1].power == 2:
			graph(minimized, results)
		if visualization == 1 and minimized[len(minimized) - 1].power == 1:
			graph(minimized, results)
	except:
		print("Error. Usage: ./computerv1 -v [your equation]")




if __name__ == "__main__":
    main()

'''

python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

bonus:
- x and X
- default equations from the list
- intermidiate steps
- graph
- color

'''
