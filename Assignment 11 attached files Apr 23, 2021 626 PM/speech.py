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
		#self.test = [0.9027777777777778, 0.9073660714285714, 0.911690496215307, 0.9269256089532587, 0.9383450513791238, 0.9473447344734474, 0.9509569377990431, 0.954239091876552, 0.9465435208508256, 0.949740932642487, 0.9529832935560859, 0.954013875123885, 0.9562383612662942, 0.9569874752801583, 0.9602909972719006, 0.9604577056778679, 0.9595108695652174, 0.9610062893081761, 0.9614834247555449, 0.96256374594344, 0.9616634178037686, 0.962657313802352, 0.9628591450595655, 0.9632431383958879, 0.9633920296570899]
		#self.test2 = [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08, 0.08, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.28, 0.28, 0.24, 0.2], [0.04, 0.04, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.12, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.04, 0.04, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.04, 0.04, 0.0, 0.0, 0.44, 0.36], [0.24, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.08], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.24, 0.2, 0.12, 0.36, 0.4, 0.44, 0.04, 0.36, 0.52, 0.24, 0.12, 0.24, 0.08, 0.24, 0.4, 0.36, 0.44, 0.32, 0.24, 0.16, 0.24], [0.04, 0.0, 0.0, 0.04, 0.0, 0.08, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.48, 0.4], [0.04, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28, 0.44], [0.12, 0.36, 0.24, 0.16, 0.24, 0.24, 0.24, 0.56, 0.16, 0.32, 0.0, 0.12, 0.28, 0.16, 0.28, 0.24, 0.28, 0.24, 0.32, 0.16, 0.32, 0.2], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.28, 0.4, 0.32, 0.16, 0.28], [0.04, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08, 0.0, 0.0, 0.04], [0.08, 0.16, 0.2, 0.2, 0.44, 0.44, 0.28, 0.2, 0.28, 0.12, 0.16, 0.32, 0.32, 0.2, 0.2, 0.16, 0.36, 0.4, 0.2, 0.44, 0.48, 0.52, 0.44, 0.32, 0.24, 0.24, 0.2, 0.44], [0.04, 0.0, 0.0, 0.0, 0.16, 0.16, 0.16, 0.24, 0.24, 0.16, 0.24, 0.24, 0.16, 0.16, 0.28, 0.28, 0.16, 0.2, 0.24, 0.24, 0.28], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.08, 0.0, 0.0, 0.04, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06, 0.14, 0.14, 0.12, 0.1], [0.02, 0.02, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.06, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.02, 0.02, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.02, 0.02, 0.0, 0.0, 0.22, 0.18], [0.12, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.04], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.1, 0.06, 0.18, 0.2, 0.22, 0.02, 0.18, 0.26, 0.12, 0.06, 0.12, 0.04, 0.12, 0.2, 0.18, 0.22, 0.16, 0.12, 0.08, 0.12], [0.02, 0.0, 0.0, 0.02, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.24, 0.2], [0.02, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14, 0.22], [0.06, 0.18, 0.12, 0.08, 0.12, 0.12, 0.12, 0.28, 0.08, 0.16, 0.0, 0.06, 0.14, 0.08, 0.14, 0.12, 0.14, 0.12, 0.16, 0.08, 0.16, 0.1], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.14, 0.2, 0.16, 0.08, 0.14], [0.02, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.02], [0.04, 0.08, 0.1, 0.1, 0.22, 0.22, 0.14, 0.1, 0.14, 0.06, 0.08, 0.16, 0.16, 0.1, 0.1, 0.08, 0.18, 0.2, 0.1, 0.22, 0.24, 0.26, 0.22, 0.16, 0.12, 0.12, 0.1, 0.22], [0.02, 0.0, 0.0, 0.0, 0.08, 0.08, 0.08, 0.12, 0.12, 0.08, 0.12, 0.12, 0.08, 0.08, 0.14, 0.14, 0.08, 0.1, 0.12, 0.12, 0.14], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.04, 0.0, 0.0, 0.02, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.04]
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

		#flat_list_recognized = [item for sublist in s.recognized for item in sublist]
		#print("flat List REcognized ", flat_list_recognized)
		#flat_list_original = [item for sublist in s.original for item in sublist]
		#print("flat list original ", self.original)
		#LD = distance.levenshtein(flat_list_original, flat_list_recognized)
		for i in range(len(self.original)):
			original_sentence = self.original[i]
			#print("LENGTH1 ", len(original_sentence))
			#print('original setnence is ', original_sentence)
			recognized_sentence = self.recognized[i]
			#run check
			if len(original_sentence) > len(recognized_sentence):
				diff = len(original_sentence) - len(recognized_sentence)
				while diff > 0:
					recognized_sentence.append(" ")
					diff = diff - 1
			#print("LENGTH2 ", len(recognized_sentence))
		#	print('recgonzied sentence is ', recognized_sentence)
			distances = []
			#for line in original_sentence:
			for j in range(len(original_sentence)):
				original_word = original_sentence[j]
				recognized_word = recognized_sentence[j]
				LD = distance.levenshtein(original_word, recognized_word)
				NLD = LD / max(len(self.original), len(self.recognized))
				distances.append(NLD)
		self.distances.append(distances)

		#print("LD DISTANCE IS ", LD)
		#print("MAX IS ", max(len(flat_list_original), len(flat_list_recognized)))
		#NLD = LD / max(len(flat_list_original), len(flat_list_recognized))
		#self.distances.append(NLD) #stored by index?  lol


if __name__ == '__main__':
	s = Speech()
	name = []
	s.read_original("How Speech Recognition Works.txt")
	os.chdir("inDir")
	for i in range(1, 26): #changing range for faster compile then ened to change it back to 26
		if i < 10:
			inDir = "0" + str(i) + "*.wav"
			#print(inDir)
			#inDir = "*Sent0" + str(i) + ".wav" #gives wrong input? for original
			name_for_plot = "Sent0" + str(i)
			name.append(name_for_plot)
		else:
			inDir = str(i) + "*.wav"
			#print(inDir)
			#inDir = "*Sent" + str(i) + ".wav"
			name_for_plot = "Sent" + str(i)
			name.append(name_for_plot)
		s.conv_audio(inDir)
		s.comp_string() #need to check if NLD is right bc i might need to alternate the strings to be individual words
		#df.loc[i] = name_for_plot + str(s.distances)
		print("Done with iteration", i)

#	df[name_for_plot] = s.distances
#	ax = sns.boxplot(x=name, y=df[name_for_plot])
#TESTIONG PURPOSES
	#print("S Original ", s.original)
	#print("Recognized " , s.recognized)
	#ax = sns.boxplot(name, s.distances)
	#ax = sns.boxplot(x= name, y=s.test)
	#df = pd.DataFrame(s.distances)
	#df = df.transpose()
	#print(df)
	print("Distances " , s.distances)
	print("distances length ", len(s.distances))
	#ax = sns.boxplot(y=df, data=df)

	plt.show()