from Utils import read_file, get_qf
from sys import argv
import re

def parse():
	content	= read_file(argv[1])
	rules = []
	for line in content:
		if line[0] == "?":
			queries = get_qf(line, "?")
		elif line[0] == "=":
			facts = get_qf(line, "=")
		elif line != "\n":
			line = re.sub('[\s]', '', line)
			if "#" in line:
				line = line.split("#")[0]
			rules.append(line)
	ctx	= {
		"queries": queries,
		"facts": facts,
		"rules": rules
	}
	return ctx