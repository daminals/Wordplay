# WordCount.py
import matplotlib.pyplot as plt
from collections import OrderedDict

# read text
file = open('read.txt')
text = file.read()
file.close()

# analyze letters
charDict = {} # dictionaries are defined by curly braces
def count_letter(character):
  character = character.lower()
  if character.isspace():
    return
  if character in charDict:
      charDict[character] = charDict[character] + 1
  else:
    charDict[character] = 1

# loop through text
for i in text:
    count_letter(i)

charDict = OrderedDict(sorted(charDict.items()))

char_list = [] # character
num_list = [] # frequency
# create x and y axes
for x,y in charDict.items():
    char_list.append(x)
    num_list.append(y)

fig = plt.figure() # create a new figure
ax = fig.add_subplot(111) # create a new bar graph within the figure
fig.canvas.manager.set_window_title('The Great Gatsby') # title of window
ax.bar(char_list, num_list) # add the data to the graph
plt.savefig('chars.png') # download an image of the bar graph
plt.show() # show the image