from sys import argv
import re

ngram = argv[1]
numSentences = argv[2]
filenames = argv[3:]
text = ''

#this loop iterates over the arguments of the program, accesses the named files, and adds all text to the corpus string
for file in filenames:
    with open(file, encoding="utf8") as f:
        text += f.read()

text = re.sub(r'[.|!|?]', '<end> <start>',text)


