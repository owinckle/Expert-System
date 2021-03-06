import re

def error(f):
	print("Error in %s" % (f))
	exit(2)

def read_file(file):
	lines = []
	try:
		with open(file, "r") as content:
			for line in content:
				lines.append(line)
	except IOError:
		error("read_file()")
	return lines

def content_between(s, c):
	return re.findall('"([^' + c + ']*)"', s)[0]

def get_qf(s, c):
	s = re.sub('[\s]', '', s)
	return s.split(c)[1]

def normalize(n):
	if n > 1:
		n = 1
	else:
		n = -1
	return n

def rule_parser(rule):
	parsed = []
	for c in rule:
		if c.isalpha():
			parsed.append(c)
	return parsed