import pandas as pd
from nltk.stem import WordNetLemmatizer

def rawWordCount(document):
    ''' Calculate the raw word count for document, which should be an iterable which returns strings on each iteration (such as a file)'''
    counts=dict()
    for section in document: #for each line in a file
        words=section.split() #get individual words
        for word in words:
            #strip trailing punctuation from words
            while word and (not word[-1].isalnum()):
                word=word[:-1]
            #strip leading punctuation from words
            while word and (not word[0].isalnum()):
                word=word[1:]
            if word: #ignore empty strings
                if word.lower() in counts: #do all comparisons using lowercase versions of the word
                    counts[word.lower()]+=1
                else:
                    counts[word.lower()]=1
    #convert output to a dataframe
    countItems=list(counts.items())
    keys=[k for k,v in countItems]
    values=[v for k,v in countItems]
    countFrame=pd.DataFrame(dict(word=keys,count=values))
    return countFrame

def getLemma(*words):
    '''Return a list of the lemmas corresponding to the words provided as arguments'''
    wnl=WordNetLemmatizer()
    out=list()
    for word in words:
        out.append(wnl.lemmatize(word))
    return out
