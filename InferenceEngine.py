from Parse import parse
import string
from Utils import error

class InferenceEngine():
	def __init__(self, config):
		self.config		= config
		self.content 	= parse()
		self.rules		= self.content["rules"]
		self.data		= dict.fromkeys(string.ascii_uppercase, 0)
		self.queries	= dict.fromkeys(list(self.content["queries"]), 0)
		self.facts		= dict.fromkeys(list(self.content["facts"]), 1)
		for i in self.facts:
			self.data[i] = 1

		self._is_valid()

	def _is_valid(self):
		for f in self.facts:
			for q in self.queries:
				if f == q:
					error("queries: [%c] is already known in facts [%s]" % (q, self.content["facts"]))		
			for r in self.rules:
				if f in r.split("=")[1]:
					error("facts: [%c] cannot be defined in a rule [%s]" % (f, r))

	def _solve_rules(self, rules):
		for r in rules:
			for i, rr in enumerate(r):
				if rr.isalpha():
					if r[i - 1] == "!":
						print("!" + rr)
					else:
						print(rr)
					

	def expertise(self):
		for q in self.queries:
			rules = []
			print("Current Query: %c" %(q))
			for r in self.rules:
				if q in r.split("=")[1]:
					rules.append(r)
			self._solve_rules(rules)
			
