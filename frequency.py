""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import collections




def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    path = open(file_name, 'r')
    content = path.readlines()
    curr_line = 0
    while content[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    content = content[curr_line+1:]
    exclude = set(string.punctuation)
    content = ''.join(ch for ch in content if ch not in exclude)
    words = content.split()
    listwords = []
    for word in words:
        listwords.append(word)
    listwords = [word.lower() for word in listwords]
    listwords = [word.strip(string.punctuation) for word in listwords]
    return listwords

text = '/home/anikapayano/ToolBox-WordFrequency/Pride_and_Prejudice.txt'


get_word_list(text)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    hist = dict()
    words = word_list
    hist = collections.Counter(words)
    mostfrequent = []
    mostfrequent = sorted(hist, key=hist.get, reverse= True)
    return mostfrequent[:n]



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
word_list = get_word_list(text)
top_n_words = get_top_n_words(word_list, 100)
#print('Number of Words:', len(top_n_words))
print('Top', len(top_n_words), 'Words:' , top_n_words)
