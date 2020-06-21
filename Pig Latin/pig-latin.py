# pig_latin.py
# Pig Latin generator
# Daniel Kogan 6/19/2020

# Pig Latin Rules:
# When word starts with consonant: move consonant to end and add 'ay'
# When word starts with double-consonant: move both consonants to end and add 'ay'
# When word starts with vowel, add 'way' to the end
# Words shorter than 4 characters and start with vowels can stay

# TODO: Fix the translate back to english function

from colorama import Fore, Back, Style


def main():
    vowels = ['a','o','u','i','e']
    Phrase = input('Phrase to translate: ')

    def toPigLatin(Phrase):

        def Words(word):
            word = word.lower()
            if len(word) < 4:
                return word
            if word[0] in vowels:
                Translated_Word = word + 'way'
                return Translated_Word
            else:
                if word[1] in vowels:
                    Translated_Word = word[1:] + word[0] + 'ay'
                    return Translated_Word
                else:
                    Translated_Word = word[2:] + word[:2] + 'ay'
                    return Translated_Word
    
        
        Phrase = Phrase.split(' ')
        FinalPhrase = ''
        for i in Phrase:
            FinalPhrase = FinalPhrase + ' ' + Words(i)
    
        FinalPhrase = FinalPhrase[1:]
        FinalPhrase = FinalPhrase[0].upper() + FinalPhrase[1:]
        print(Fore.BLUE + FinalPhrase)

    def fromPigLatin(Phrase):

        def PigWords(word):
            word = word.lower()
            word = word[:-2]

            if len(word) < 4:
                print(word)
                return word
            if word[0] in vowels:
                if word[-1] == 'w':
                    if len(word[:-1]) < 4:
                        return word
                    return word[:-1]
                else:
                    return word[-1] + word[:-1]
            else:
                return word

        Phrase = Phrase.split(' ')
        FinalPhrase = ''
        for i in Phrase:
            FinalPhrase = FinalPhrase + ' ' + PigWords(i)

        FinalPhrase = FinalPhrase[1:]
        FinalPhrase = FinalPhrase[0].upper() + FinalPhrase[1:]
        print(Fore.BLUE + FinalPhrase)
            


    toPigLatin(Phrase)
    
    #fromPigLatin(Phrase)

if __name__ == '__main__':
    main()

