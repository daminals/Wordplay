# First, you're going to need to import wordnet:
import nltk,sys,random
from textblob import TextBlob,Word
from nltk.corpus import wordnet

nltk.download('wordnet')
# Then, we're going to use the term "program" to find synsets like so:


f = open("copypaste.txt", 'r')


para = f.read()

para_list = TextBlob(para)

f.close()
output = list()
for word,tag in para_list.tags:
    if tag == 'NN' or tag == "JJ" or tag == 'VB' or random.randint(0,10)>6:
        if len(word) > 3 and len(wordnet.synsets(word)) > 0:
            synonyms = []
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())

            word = random.choice(synonyms)
            if "_" in word:
                word = word.replace('_', ' ')

    output.append(word)

write_to = open('bullshit.txt', 'w+')
write_to.write(" ".join(output))
write_to.close()

print(" ".join(output))




