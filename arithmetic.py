import argparse

MAX_PREVIEW_PARAMETERS = 3

parser = argparse.ArgumentParser(description="arithmetic")
parser.add_argument("expression", help="")
parser.add_argument("parameters", help="")
parser.add_argument("--preview", help="", action="store_true")
args = parser.parse_args()

def parse_parameters(parameters):
	parameters_fixed_chars = []
	index = 0
	while index < len(parameters):
		if len(parameters)-index+1 >= 4 and parameters[index:index+4] == "'\\''":
			parameters_fixed_chars.append("\\")
			parameters_fixed_chars.append("'")
			index += 4
		elif parameters[index] == "\\":
			parameters_fixed_chars.append("\\")
			parameters_fixed_chars.append("\\")
			index += 1
		else:
			parameters_fixed_chars.append(parameters[index])
			index += 1
	
	parameters_fixed = "".join(parameters_fixed_chars)
	
	class State:
		class LookingForQuote:
			def __init__(self):
				pass
		class ParsingString:
			def __init__(self):
				self.escape = False
	
	parameters_split = []
	parameter_current = []
	state = State.LookingForQuote()
	for char in parameters_fixed:
		if isinstance(state, State.LookingForQuote):
			if char == "'":
				state = State.ParsingString()
		elif isinstance(state, State.ParsingString):
			if not state.escape:
				if char == "\\":
					state.escape = True
				elif char == "'":
					state = State.LookingForQuote()
					parameters_split.append("".join(parameter_current))
					parameter_current.clear()
				else:
					parameter_current.append(char)
			else:
				parameter_current.append(char)
				state.escape = False
	return parameters_split

class Evaluator:
	def __init__(self):
		import math, random
		self.math = math
		self.random = random
	def evaluate(self, expression, i, x):
		return eval(
			expression,
			{"math": self.math, "random": self.random},
			{"i": i, "x": eval(x)},
		)

parameters = parse_parameters(args.parameters)
evaluator = Evaluator()
if args.preview:
	results = []
	for i in range(min(len(parameters), MAX_PREVIEW_PARAMETERS)):
		x = parameters[i]
		result = evaluator.evaluate(args.expression, i, x)
		results.append(result)
	
	dots = (len(parameters) > len(results))
	for i in range(len(results)):
		result = results[i]
		final_in_parameters = (i == len(parameters)-1)
		final_in_results = (i == len(results)-1)
		if final_in_parameters:
			end = ""
		else:
			end = ", "
			if final_in_results:
				end += "…"
		print(f"{result}", end=end)
else:
	results = []
	for i,x in enumerate(parameters):
		result = evaluator.evaluate(args.expression, i, x)
		results.append(result)
	
	for result in results:
		print(f"'{result}'", end=" ")
