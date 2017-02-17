# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:01:52 2017

Code Created following the instructions  from the Harvard online class:
    PH526x Using Python for Research Harvard class
    
@link https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/info
@author: Sylhare

"""

from collections import Counter
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import random


#Random text for the tests
text = (
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
    'sed do eiusmod tempor incididunt ut labore et dolore magna '
    'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
    'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
    'Duis aute irure dolor in reprehenderit in voluptate velit '
    'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
    'occaecat cupidatat non proident, sunt in culpa qui officia '
    'deserunt mollit anim id est laborum.'
    ) 
    
text2 = (
    'Sed ut perspiciatis unde omnis iste natus error sit voluptatem'
    'accusantium doloremque laudantium, totam rem aperiam, eaque ipsa'
    'quae ab illo inventore veritatis et quasi architecto beatae vitae dicta'
    'sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur'
    'aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione'
    'voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum'
    'quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam'
    'eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat'
    'voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam'
    'corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?'
    'Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam'
    'nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo'
    'voluptas nulla pariatur?'
    )



def count_words(text):
    """
    Count the number of times each word occurs in text (str). Skip punctuation. 
    Return dictionary where keys are unique words and values are word count.
    
    """
    text = text.lower()
    skips = [".",";",",",":","!","?",'"']
    for ch in skips:
        text.replace(ch, "")
    
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts


def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Skip punctuation. 
    Return dictionary where keys are unique words and values are word count.
    
    """
    text = text.lower()
    skips = [".",";",",",":","!","?",'"']
    for ch in skips:
        text.replace(ch, "")
    
    word_counts = Counter(text.split(" "))
            
    return word_counts
    
def read_book(title_path):
    """
    Read a book and return it as a string.
    
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
        
    return text
    
def word_stats(word_counts):
    """
    Return number of unique words and word frequencies
    
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
    
def word_count_distribution(text):
    """
    Outputs a dictionary with items corresponding to the 
    count of times a collection of words appears in the translation,
    and values corresponding to the number 'word_count' 
    that appear with that frequency.
    key : the number of times a group of words appears in the text
    value : frequency of that number of time appearing (key)
    
    """
       
    frequency = count_words_fast(text)    #{('word':20)}
    distribution = Counter(frequency.values())
    
    return distribution
    
def random_distribution():
    text = []
    for i in range(0, 100):
        text.append(random.randrange(0, 100, 1))
    frequency = Counter(text)
    distribution = Counter(frequency.values())
    
    return distribution
    



def more_frequent(distribution):
    """
    Takes a word distribution {n: d} and outputs a dictionary 
    with the same keys (number of time a words appears in the text),
    and values corresponding of the fraction of words that occur
    with more frequency than that key.
    
    n = number of time a word appear in a text
    d = number of equal n
    f = ratio of each d compared to the total count of n
    
    Returns a dictionary of frequency {n: f}
    
    """
    counts = sorted(distribution.keys())
    sorted_frequencies = sorted(distribution.values(), reverse = True)
    
    #Each [1, 2, 3] -> [1, 3, 6]
    cumulative_frequencies = numpy.cumsum(sorted_frequencies) 
    #Frequency of cumulated element based on the total
    more_frequent = 1 - cumulative_frequencies / cumulative_frequencies[-1] 
    
    return dict(zip(counts, more_frequent))
    
    
#=============================  USAGE EXAMPLE  ================================

#How much words is there for a book depending on the language
book_titles = { "English": {"Shakespear": ("Hamlet", "MacBeth", "Othello"),
                            "Orwells": ("1984",)},
                "French": {"Shakespear": ("Hamlet", "MacBeth"),
                            "Orwells": ("1984",),
                            "Voltaire": ("Candide",)},
                "Portuguese": {"Shakespear": ("Hamlet",)},
                "Spanish": {"Cervantes": ("Don Quixote",)} }

hamlets = pd.DataFrame(columns = ("language", "distribution"))
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                #Because I don't have the books and their word length
                distribution = random_distribution()      
                hamlets.loc[title_num] = language, distribution
                title_num += 1
                
#Plotting the results
hamlet_languages = []
plt.title("Word Frequencies in Hamlet Translations")
colors = ["crimson", "forestgreen", "blueviolet"]
xlim = [0, 2e1]
xlabel = "Frequency of Word $W$"
ylabel = "Fraction of Words\nWith Greater Frequency than $W$"

for index in range(hamlets.shape[0]):
    language = hamlets.language[index+1]
    distribution = hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    hamlet_languages.append(language)
    plot = plt.loglog(sorted(list(dist.keys())), 
                      sorted(list(dist.values()), reverse = True),
                      color = colors[index], linewidth = 2)
                      
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(hamlet_languages, loc="upper right", numpoints = 1)
plt.show()

    