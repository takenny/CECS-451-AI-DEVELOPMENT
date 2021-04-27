import glob
import os
import distance
import speech_recognition as sr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.distances = []

	def read_original(self, inFile):
		with open(inFile) as file:
			for line in file:
				fixed = line.replace('â€™',"'") #changed the incorrect thing outputted
				self.original.append(fixed.rstrip("\n").split())


	def conv_audio(self, inDir):
		r = sr.Recognizer()
		#file_name = index_val.append("-Sent01.wav")
		#os.chdir("inDir/Folder")
		#iterates through
		for file in glob.glob(inDir):  #all the Sent01's but I need all the Sents
			recording = sr.AudioFile(file)
			with recording as source:
				audio = r.record(source)
				audio_speech = r.recognize_google(audio)
				s.recognized.append(audio_speech.split())

	#	file_name = "Group 03.zip"
	#	with ZipFile(file_name, 'r') as zip:
	#		zip.extractall()
	#	for file in glob.glob("*.wav"): #this means for all files with wav extension
	#		harvard = sr.AudioFile(file)
	#			audio = r.record(source)
	#			audio_speech = r.recognize_google(audio)
	#			s.recognized.append(audio_speech)

		#for file in inDir:


	def comp_string(self):
		flat_list_recognized = [item for sublist in s.recognized for item in sublist]
		#print("lol", flat_list_recognized)
		flat_list_original = [item for sublist in s.original for item in sublist]
		#print("22323222 ", self.original)
		LD = distance.levenshtein(flat_list_original, flat_list_recognized)
		#print("LD DISTANCE IS ", LD)
		#print("MAX IS ", max(len(flat_list_original), len(flat_list_recognized)))
		NLD = LD / max(len(flat_list_original), len(flat_list_recognized))
		self.distances.append(NLD) #stored by index?  lol


if __name__ == '__main__':
	s = Speech()
	name = []
	s.read_original("How Speech Recognition Works.txt")
	os.chdir("inDir")
	for i in range(1, 26): #changing range for faster compile then ened to change it back to 26
		if i < 10:
			inDir = "*Sent0" + str(i) + ".wav"
			name_for_plot = "Sent0" + str(i)
			name.append(name_for_plot)
		else:
			inDir = "*Sent" + str(i) + ".wav"
			name_for_plot = "Sent" + str(i)
			name.append(name_for_plot)
		s.conv_audio(inDir)
		#print(s.original)
		#print("THIS ", s.recognized)
		s.comp_string() #need to check if NLD is right bc i might need to alternate the strings to be individual words
		#print("THIS IS NLD ", s.distances)
		#then now i need to plot graph probalby or add values to the graph somehow
		#print(s.distances[i-1])
	print("DISTANCE ", s.distances)
	print("NAMES for PLOT ", name)
	ax = sns.boxplot(name, s.distances)
	plt.show()
	ax.show()