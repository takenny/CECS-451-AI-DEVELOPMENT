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
		#self.test =[[0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.04], [0.013333333333333334, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.013333333333333334, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.013333333333333334, 0.02666666666666667], [0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.02], [0.008, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.008, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.008, 0.016], [0.006666666666666667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.006666666666666667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.006666666666666667, 0.013333333333333334], [0.005714285714285714, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005714285714285714, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005714285714285714, 0.011428571428571429], [0.005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005, 0.01], [0.0044444444444444444, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0044444444444444444, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0044444444444444444, 0.008888888888888889], [0.004, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.004, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.004, 0.008], [0.0036363636363636364, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0036363636363636364, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0036363636363636364, 0.007272727272727273], [0.0033333333333333335, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0033333333333333335, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0033333333333333335, 0.006666666666666667], [0.003076923076923077, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003076923076923077, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003076923076923077, 0.006153846153846154], [0.002857142857142857, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002857142857142857, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002857142857142857, 0.005714285714285714], [0.002849002849002849, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002849002849002849, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002849002849002849, 0.005698005698005698], [0.0026595744680851063, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0026595744680851063, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0026595744680851063, 0.005319148936170213], [0.0024937655860349127, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0024937655860349127, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0024937655860349127, 0.004987531172069825], [0.002347417840375587, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002347417840375587, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002347417840375587, 0.004694835680751174], [0.00234192037470726, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00234192037470726, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00234192037470726, 0.00468384074941452], [0.0022123893805309734, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0022123893805309734, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0022123893805309734, 0.004424778761061947], [0.0020964360587002098, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0020964360587002098, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0020964360587002098, 0.0041928721174004195], [0.00199203187250996, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00199203187250996, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00199203187250996, 0.00398406374501992], [0.0018975332068311196, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0018975332068311196, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0018975332068311196, 0.003795066413662239], [0.001893939393939394, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001893939393939394, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001893939393939394, 0.003787878787878788], [0.0018083182640144665, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0018083182640144665, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0018083182640144665, 0.003616636528028933]]
	def read_original(self, inFile):
		with open(inFile) as file:
			for line in file:
				fixed = line.replace('â€™',"'") #changed the incorrect thing outputted
				self.original.append(fixed.rstrip("\n").split())


	def conv_audio(self, inDir):
		r = sr.Recognizer()
		#iterates through
		for file in glob.glob(inDir):  #all the Sent01's but I need all the Sents
			recording = sr.AudioFile(file)
			with recording as source:
				audio = r.record(source)
				audio_speech = r.recognize_google(audio)
				s.recognized.append(audio_speech.split())


	def comp_string(self):

		#flat_list_recognized = [item for sublist in s.recognized for item in sublist]
		#print("flat List REcognized ", flat_list_recognized)
		#flat_list_original = [item for sublist in s.original for item in sublist]
		#print("flat list original ", self.original)
		#LD = distance.levenshtein(flat_list_original, flat_list_recognized)
		for i in range(len(self.original)):
			original_sentence = self.original[i]
			recognized_sentence = self.recognized[i]
			#run check for diff lengths
			if len(original_sentence) > len(recognized_sentence):
				diff = len(original_sentence) - len(recognized_sentence)
				while diff > 0:
					recognized_sentence.append(" ")
					diff = diff - 1
			distances = []
			for j in range(len(original_sentence)):
				original_word = original_sentence[j]
				recognized_word = recognized_sentence[j]
				LD = distance.levenshtein(original_word, recognized_word)
				NLD = float(LD) / max(len(self.original), len(self.recognized))
				distances.append(NLD)
		self.distances.append(distances)



if __name__ == '__main__':
	s = Speech()
	name = []
	s.read_original("How Speech Recognition Works.txt")
	os.chdir("inDir")
	for i in range(1, 26): #changing range for faster compile then ened to change it back to 26
		if i < 10:
			inDir = "0" + str(i) + "*.wav"
			name_for_plot = "Sent0" + str(i)
			name.append(name_for_plot)
		else:
			inDir = str(i) + "*.wav"
			name_for_plot = "Sent" + str(i)
			name.append(name_for_plot)
		s.conv_audio(inDir)
		s.comp_string() #need to check if NLD is right bc i might need to alternate the strings to be individual words
		print("Done with iteration", i)


	#make dataframe
		#have list of lists [[1,2],[2,3]
		#need data from list of lists to be in columns?

	#put boxplot in dataframe
		#y axis is normalized distance
		#x axis is Sentence#s
	alldata = s.distances
	labels = name

	fig, (ax1) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

	# rectangular box plot
	bplot1 = ax1.boxplot(alldata,
						 vert=True,  # vertical box alignment
						 patch_artist=True,  # fill with color
						 labels=labels)  # will be used to label x-ti
	# show plot
	plt.show()