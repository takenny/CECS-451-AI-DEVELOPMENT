import glob
import distance
import speech_recognition as sr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os.path
from os import path


class Speech:
    def __init__(self):
        self.original = []
        self.recognized = []
        self.distances = []

    # self.test = [[0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.08, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.08, 0.0, 0.0, 0.04, 0.08], [0.32, 0.24, 0.28, 0.36, 0.36, 0.24, 0.28, 0.36, 0.24, 0.24, 0.24, 0.24, 0.12, 0.32, 0.12, 0.12, 0.2, 0.2, 0.28, 0.2, 0.24, 0.2], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.32, 0.24, 0.4, 0.24, 0.4, 0.36, 0.12, 0.32, 0.24, 0.24, 0.2, 0.28, 0.08, 0.16, 0.2, 0.32, 0.12, 0.2, 0.32, 0.2, 0.24, 0.2], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.16], [0.12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.08], [0.24, 0.24, 0.24, 0.44, 0.36, 0.24, 0.28, 0.36, 0.12, 0.2, 0.28, 0.28, 0.12, 0.16, 0.08, 0.16, 0.2, 0.28, 0.28, 0.24, 0.24, 0.2]]
    def read_original(self, inFile):
        with open(inFile) as file:
            for line in file:
                fixed = line.replace('â€™', "'")  # changed the incorrect thing outputted
                self.original.append(fixed.rstrip("\n").split())

    def conv_audio(self, inDir):
        r = sr.Recognizer()
        # iterates through
        for file in glob.glob(inDir):
            recording = sr.AudioFile(file)
            with recording as source:
                audio = r.record(source)
                audio_speech = r.recognize_google(audio)
                s.recognized.append(audio_speech.split())

    def comp_string(self):
        for i in range(len(self.original)):
            original_sentence = self.original[i]
            recognized_sentence = self.recognized[i]
            # run check for diff lengths
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
    for i in range(1, 26):  # changing range for faster compile then ened to change it back to 26
        if i < 10:
            inDir = "0" + str(i) + "*.wav"
            name_for_plot = "Sent0" + str(i)
            name_for_exist = "0" + str(i) + "-Sent0" + str(i) + ".wav"
            name.append(name_for_plot)
        else:
            inDir = str(i) + "*.wav"
            name_for_plot = "Sent" + str(i)
            name_for_exist = str(i) + "-Sent" + str(i) + ".wav"
            name.append(name_for_plot)
        if path.exists(name_for_exist):  # checks for nonexistent files group 19, 24
            s.conv_audio(inDir)
            s.comp_string()
            s.recognized.clear()  # clear list after each finished thing iteration
        else:
            name.remove(name_for_plot)
        print("Done with group", i)

    test = np.array(s.distances).transpose()
    df = pd.DataFrame(test)
    df.columns = name
    plt.figure(figsize=(20, 10))
    sns.boxplot(data=df)
    plt.ylabel("NLD", fontsize=20)
    plt.yticks(fontsize=15)
    plt.xticks(fontsize=10)
    plt.show()
