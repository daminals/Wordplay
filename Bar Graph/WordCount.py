# WordCount.py

import matplotlib.pyplot as plt


def main():
    read = open('read.txt')
    text = read.read()
    read.close()

    letterL = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
        'h': [],
        'i': [],
        'j': [],
        'k': [],
        'l': [],
        'm': [],
        'n': [],
        'o': [],
        'p': [],
        'q': [],
        'r': [],
        's': [],
        't': [],
        'u': [],
        'v': [],
        'w': [],
        'x': [],
        'y': [],
        'z': [],
    }
    num_list = []
    letter_list = []

    def letters(let):
        if let in letterL:
            templist = letterL[let]
            templist.append(let)
            letterL[let] = templist

    for i in text:
        letters(i)

    for x,y in letterL.items():
        letter_list.append(x)
        num_list.append(len(y))

    print(num_list,letter_list)



    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(letter_list, num_list)
    plt.savefig('letters.png')
    plt.show()
    




if __name__ == '__main__':
    main()