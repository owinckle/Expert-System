from Utils import read_file, content_between

class Config():
	def __init__(self, config_file):
		content	= read_file(config_file)
		self.op	= self._get_op(content)

	def _get_op(self, content):
		for line in content:
			if "set implies" in line:
				op_implies = content_between(line, '"')
			elif "set and" in line:
				op_and = content_between(line, '"')
			elif "set neg" in line:
				op_neg = content_between(line, '"')
			elif "set or" in line:
				op_or = content_between(line, '"')
			elif "set xor" in line:
				op_xor = content_between(line, '"')
		op = {
			"implies": op_implies,
			"and": op_and,
			"neg": op_neg,
			"or": op_or,
			"xor": op_xor
		}
		return op