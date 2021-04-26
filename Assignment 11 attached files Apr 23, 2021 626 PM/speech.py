import pathlib

import distance
import speech_recognition as sr

class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.distances = []

	def read_original(self, inFile):
		with open(inFile) as file:
			for line in file:
				fixed = line.replace('â€™',"'") #changed the incorrect thing outputted
				self.original.append(fixed.rstrip("\n"))


	def conv_audio(self, inDir):
		print('in')
		r = sr.Recognizer()
		harvard = sr.AudioFile('08-Sent01.wav')
		with harvard as source:
			audio = r.record(source)
		print(r.recognize_google(audio))
		#for file in inDir:
		#	print('yep')
		#	audio = sr.AudioFile(file)
		#	with audio as source:
		#		print("uh")
		#		test = r.record(source)
		#		r.recognize_google(test)



	def comp_string(self):
		LD = distance.levenshtein(self.original, self.recognized)
		NLD = LD / max(len(self.original), len(self.recognized))
		return NLD


if __name__ == '__main__':
	s = Speech()
	s.read_original("How Speech Recognition Works.txt")
	audio = s.conv_audio("inDir")