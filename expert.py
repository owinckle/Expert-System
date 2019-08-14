from sys import argv
from Config import Config
from InferenceEngine import InferenceEngine
from Utils import error

CONFIG_FILE	= "config"

def main():
	config	= Config(CONFIG_FILE)
	Expert	= InferenceEngine(config)

	Expert.expertise()
	Expert.results()

	# print(Expert.data)
	# print(Expert.queries)
	# print(Expert.facts)

if __name__ == "__main__":
	if len(argv) != 2:
		error("arguments")
	main()