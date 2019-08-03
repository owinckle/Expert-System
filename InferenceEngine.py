from Parse import parse
import string

class InferenceEngine():
	def __init__(self, config):
		self.config		= config
		content 		= parse()
		self.rules		= content["rules"]
		self.data		= dict.fromkeys(string.ascii_uppercase, 0)
		self.queries	= dict.fromkeys(list(content["queries"]), 0)
		self.facts		= dict.fromkeys(list(content["facts"]), 1)
		for i in self.facts:
			self.data[i] = 1

	def expertise(self):
		for q in self.queries:
			print("Current Query: %c" %(q))
			for r in self.rules:
				if q in r:
					print(r)
