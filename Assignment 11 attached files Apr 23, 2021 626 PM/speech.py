import glob
import os
from zipfile import ZipFile
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
		r = sr.Recognizer()
		#os.chdir("inDir/Folder")
		os.chdir("inDir")
	#	file_name = "Group 03.zip"
	#	with ZipFile(file_name, 'r') as zip:
	#		zip.extractall()
		for file in glob.glob("*.wav"):
			harvard = sr.AudioFile(file)
			with harvard as source:
				audio = r.record(source)
				audio_speech = r.recognize_google(audio)
				s.recognized.append(audio_speech)

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
	print(s.original)
	inDir = "C:/Users/kta67/Desktop/451 AI/CECS-451-AI-DEVELOPMENT/Assignment 11 attached files Apr 23, 2021 626 PM/"
	s.conv_audio(inDir)
	NLD = s.comp_string() #need to check if NLD is right bc i might need to alternate the strings to be individual words
