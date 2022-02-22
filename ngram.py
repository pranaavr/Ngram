from sys import argv
import re

ngram = argv[1]     #ngram model
numSentences = argv[2]      #number of sentences to return
filenames = argv[3:]    #files to compose corpus
text = ''

#this loop iterates over the arguments of the program, accesses the named files, and adds all text to the corpus string
for file in filenames:
    with open(file, encoding="utf8") as f:
        text += f.read()

text = text.strip()
text = re.sub(r'[.|!|?]', ' <end> <start> ',text)
corpus = text.split()

#create dictionary that records the frequency of each token in the named texts
freq_dict = {}
for i in corpus:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

#create dictionary holding the probability of each token
prob_dict = {}
for i in freq_dict:
    prob_dict[i] = freq_dict[i]/len(corpus)


#unigram base case

#always end in .
