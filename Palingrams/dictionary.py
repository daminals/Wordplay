# dictionary.py
# Daniel Kogan, 6/21/2020

import sys


def main():
    def load(file):
        dicttxt = open(file)
        loaded_txt = dicttxt.read().strip().split('\n')
        loaded_txt = [x.lower() for x in loaded_txt]
        dicttxt.close()
        return loaded_txt

    All_Words = load('dictionary.txt')

    def palindromeInList(list_object):
        pal_list = []
        for i in list_object:
            if palindrome(i):
                pal_list.append(i)
        return pal_list

    def semordnilapInList(list_object):
        sem_list = []
        for i in list_object:
            if semordnilap(i):
                sem_list.append([i,i[::-1]])
                list_object.remove(i[::-1])
        return sem_list

    def palindrome(word):
        if word == word[::-1]:
            return True
        else:
            return False

    def semordnilap(word):
        if palindrome(word):
            return False
        if word[::-1] in All_Words:
            return True
        else:
            return False

    #print(palindromeInList(All_Words))
    print(semordnilapInList(All_Words))


if __name__ == '__main__':
    main()
