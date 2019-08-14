from Parse import parse
import string
from Utils import error, normalize

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

	def _solve_conditions(self, facts, ops):
		n_fact	= len(facts)
		n_ops	= len(ops)
		result	= 0

		if self.data[facts[0]] != 0 and self.data[facts[1]] != 0:
			if ops[0] == "+":
				res = self.data[facts[0]] + self.data[facts[1]]
				res = normalize(res)
				print(res)
				exit()

	def _get_conditions(self, rules):
		for r in rules:
			ops = []
			facts = []
			for i, rr in enumerate(r):
				if rr.isalpha():
					if r[i - 1] == "!":
						facts.append("!" + rr)
					else:
						facts.append(rr)
				else:
					ops.append(rr)
			self._solve_conditions(facts, ops)
					

	def expertise(self):
		for q in self.queries:
			rules = []
			print("Current Query: %c" %(q))
			for r in self.rules:
				if q in r.split("=>")[1]:
					rules.append(r.split("=>")[0])
			self._get_conditions(rules)
			
