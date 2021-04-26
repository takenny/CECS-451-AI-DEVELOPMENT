class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.distances = []

	def read_original(self, inFile):
		with open(inFile) as file:
			for line in file:
				fixed = line.replace('â€™',"'")
				self.original.append(fixed.rstrip("\n"))


	def conv_audio(self, inDir):
		print("uh")

	def comp_string(self):
		print("uh")



if __name__ == '__main__':
	s = Speech()
	s.read_original("How Speech Recognition Works.txt")
	print(s.original)