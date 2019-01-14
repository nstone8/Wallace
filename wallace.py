def rawWordCount(document):
    ''' Calculate the raw word count for document, which should be an iterable which returns strings on each iteration (such as a file)'''
    counts=dict()
    for section in document: #for each line in a file
        words=section.split() #get individual words
        for word in words:
            #strip trailing punctuation from words
            while word and (not word[-1].isalnum()):
                word=word[:-1]
            if word: #ignore empty strings
                if word.lower() in counts: #do all comparisons using lowercase versions of the word
                    counts[word.lower()]+=1
                else:
                    counts[word.lower()]=1
    return counts
