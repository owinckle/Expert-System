from Parse import parse
import string
from Utils import error, normalize, rule_parser
from Solver import *

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

	def _get_related_rules(self, query):
		try:
			related = []
			for rule in self.rules:
				if query == rule.split("=>")[1]:
					related.append(rule)
					content = rule_parser(rule.split("=>")[0])
					break;
			for rule in self.rules:
				if rule.split("=>")[1] in content:
					related.append(rule)
			return [x for x in reversed(related)]
		except UnboundLocalError:
			pass

	def _prepare_rules(self, rules):
		rule = rules[-1]
		rule = rule.split("=>")
		syntax	= rule[0]
		result	= rule[1]
		facts	= []

		for x in syntax:
			if x.isalpha():
				facts.append(x)

		rules = [syntax + "=>" + result]
		for f in facts:
			if f not in self.facts:
				try:
					rules += self._get_related_rules(f)
				except TypeError:
					pass

		rules = rules[1:] + [rules[0]]
		return rules

	def _solve(self, rule, query):
		ops		= []
		facts	= []
		for f in rule:
			if f.isalpha():
				facts.append(f)
			else:
				ops.append(f)

		if ops[0] == self.config.op["and"]:
			res = op_and(self.data[facts[0]], self.data[facts[0]])
			res = normalize(res)

		for i, op in enumerate(ops[1:]):
			if ops[0] == self.config.op["and"]:
				res = op_and(res, self.data[facts[i + 2]])
				res = normalize(res)

		self.data[query] = res

	def results(self):
		for query in self.queries:
			if self.data[query] == 1:
				print("\033[1;32;40m%c" % (query))
			else:
				print("\033[1;31;40m%c" % (query))

	def expertise(self):
		for query in self.queries:
			related = self._get_related_rules(query)
			prepared_rules = self._prepare_rules(related)
			for rule in prepared_rules:
				self._solve(rule.split("=>")[0], rule.split("=>")[1])
