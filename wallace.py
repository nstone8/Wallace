import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import EnglishStemmer

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
    countFrame=countFrame.sort_values('count',ascending=False).reset_index(drop=True)
    return countFrame

def getLemma(*words):
    '''Return a list of the lemmas corresponding to the words provided as arguments'''
    wnl=WordNetLemmatizer()
    out=list()
    for word in words:
        out.append(wnl.lemmatize(word))
    return out

def getStem(*words):
    '''Return a list of the stems corresponding to the words provided as arguments'''
    stemmer=EnglishStemmer()
    out=list()
    for word in words:
        out.append(stemmer.stem(word))
    return out

def stemCount(document):
    ''' Calculate the word count for document, which should be an iterable which returns strings on each iteration (such as a file), and aggregate the results by word stem. Returns a tuple where the first member is a dataframe containing the count per stem and the second member is a dictionary with the keys corresponding to stems and the values are lists of words corresponding to that stem'''
    counts=rawWordCount(document)
    counts.loc[:,'stem']=getStem(*counts.word)
    grouped=counts.groupby('stem')
    stemDict=dict()
    for stem in set(counts.stem):
        #make list of words corresponding to each stem
        stemDict[stem]=list(counts.loc[counts.loc[:,'stem']==stem,'word'])
    #Sum up total count for each stem
    agg=counts.loc[:,('stem','count')].groupby('stem').aggregate(sum).sort_values('count',ascending=False)
    return agg,stemDict
