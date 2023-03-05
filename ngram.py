'''
Programming Assignment 2 - Ngram
Class: CMSC416 Natural Language Processing
Author: Pranaav Rao
Date: 5/18/2022

This program will learn an N-gram language model from an arbitrary number
of plain text files. It will generate an user-specified number of sentences
based on the specified N-gram model.

Directions:
Run program on command line with the first CL argument being the N-gram model
(3 for trigram, 4 for quadgram, etc.), the second CL argument being the number of 
sentences to be returned, and all following arguments are the texts for the model
to be processed on.

Example input:
python3 ngram.py 4 10 .\anna-karenina.txt '.\crime&punishment.txt' '.\war&peace.txt

Example output:
This program generates random sentences based on an Ngram model
Command line settings: ngram.py 4 9
1
“then who can have latched the door , “why i’m especially fond of that music .
2
The rooms , and hay , and beat down one another’s prices to below what they had already told her many times: that so-and-so was dead and so-and-so was married , which she would again be unable to live for a single moment .
3
“adieu , mary , today elias mitrofánych” ( this was his overseer ) “came back from the tambóv estate and told me they are already offering eighty thousand rubles for the forest .
4
Order after order and plan after plan were issued by him from the time the first person said and proved that the number of public domain and licensed works that can be freely distributed in machine-readable form accessible by the widest array of equipment including outdated equipment .  
5
He pricked up his horse ; another was saying that pleased her—that did not even interest her , for it is irrevocably linked to the project gutenberg literary archive foundation , how to help produce our new ebooks , and how to subscribe to our email newsletter to hear about new ebooks . 
6
Zakhár , while still wearing deep mourning , such matchmaking would be an insult to the world and the clearness of our perception of the place where you are located before using this ebook .  
7
Mechanically he drew from a chair beside him .
8
The russian army in paris when the news of his father’s death reached him .
9
Veslovsky’s only lately married .

Algorithm:
The algorithm parses over the provided text, noting frequency of words appearing
in each n-gram of the text as well as a record of the how often an ngram appears. 
It then generates sentences based on the previous n-grams through random selection 
from the history dictionary and extending the sentences using the ngram model
based on the previous n words of the generating sentence.
'''

from sys import argv
import re
import random

n = int(argv[1])     #ngram model
numSentences = int(argv[2])      #number of sentences to return
filenames = argv[3:]    #files to compose corpus
text = ''

#informative message
print("This program generates random sentences based on an Ngram model")
print("Command line settings: ngram.py "+str(n)+' '+str(numSentences))

#this loop iterates over the arguments of the program, accesses the named files, and adds all text to the corpus string
for file in filenames:
    with open(file, 'r', encoding="utf-8-sig") as f:
        text += f.read()

text = text.replace('\n', ' ')
text = text.lower()
# separate punctuation for future tokenization
text = re.sub(r'([,";\(\)])',r' \1 ', text)
# identify sentence boundaries
end_tag = ' <end> <start> '
text = text.replace('.', end_tag)
text = text.replace('!', end_tag)
text = text.replace('?', end_tag)
text = text.replace('_', " ")
corpus = text.split()
#move end <start> tag to front
corpus = ['<start>']+corpus[:-1]


#create n-gram
ndict = {}
hdict = {}
ptr = 0
while ptr < len(corpus)-n:
    array = corpus[ptr:ptr+n]
    word = array[-1]
    history = ' '.join(array[:-1])
    if history in ndict and word in ndict[history]:
        ndict[history][word] += 1
    else:
        ndict[history] = {word:1}
    if history in hdict:
        hdict[history] += 1
    else:
        hdict[history] = 1
    ptr += 1


for i in range(1, numSentences+1):
    # randomly pick starting phrase for sentence
    sentence = random.choice(list(hdict.keys()))
    # ensure starting phrase starts with start tag and final word isn't an end tag
    if n == 2:
        sentence = random.choice(list(hdict.keys()))
    elif n > 2:
        while sentence.split()[0] != '<start>' or sentence.split()[-1] == '<end>' or sentence.split()[1] == '"':
            sentence = random.choice(list(hdict.keys()))
    

    while sentence.split()[-1] != '<end>':
        arr_sent = sentence.split()
        #get last n-1 words
        if n== 2 and len(arr_sent) > 70:
            sentence += '.'
            break
        check_hist = arr_sent[-n+1:]
        check_hist = ' '.join(check_hist)
        #get dictionary containing that history
        current_hist = ndict[check_hist]
        #pick random word from that dictionary
        word = random.choice(list(current_hist.keys()))
        arr_sent = arr_sent+[word]
        sentence = ' '.join(arr_sent)
    
    sentence = sentence.replace('<start>', '')
    sentence = sentence.replace('<end>', '.')
    print(i)
    print(sentence.strip().capitalize())
    
