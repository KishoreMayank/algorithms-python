'''
# coding: utf-8

#  Dropbox has tasked you with gathering some qualitative metrics regarding a simple text search auto-complete feature. You'll be given a set of documents, each having a title and a body of text.
# 
# Every word in the documents can be assigned a numeric score. The score is defined as follows:
# 
# Each occurrence in the title: 10
# 
# Each occurrence in the body: 1
# 
# Note that the scores should be computed across all documents.
# 
# For example, given two documents
# 
# Title	Body
# 
# Document A	ANIMALS	ANT ANTELOPE CAMEL CAT DOG
# 
# Document B	DOG FACTS	FURRY FURRY LOYAL
# 
# ANIMALS has a score of 10, because it appears once in a document's title
# 
# CAT has a score of 1, because it appears once in a document's body
# 
# DOG has a score of 11, because it appears once in a docurnent's body, and once in a document's title
# 
# FURRY has a score of 2, because it appears twice in a document's body
# 
# You'll then be given a set of user queries, each a string with no whitespace. For each query, compute the highest score among all the words that could be auto-completed from it. For instance, among the set of words above, the query 'AN' could be auto-completed into ANIMALS, ANT, and ANTELOPE. If no such words exist, the score is 0.
# 
# For example, given these following queries:
# 
# AN would output 10, because it can auto-complete into ANIMAL (which has a higher score than ANT and ANTELOPE)
# 
# DO would output 11, because it can auto-complete into DOG
# 
# FUR would output 2, because it can auto-complete into FURRY
# 
# ELEPH would output 0, because it cannot auto-complete into any of the words
# 
# You can assume text and queries are comprised of A-Z characters. In documents, words are separated by a space; there is no other whitespace.
# 
# Constraints
# 
# N: the number of documents 1 <= N < 1,000
# 
# Q: the number of queries 1 <= Q < 300,000
'''

def autoCompleteScores(title,body,queries):
    docTitles = [word for line in title for word in line.split()]
    docBodies = [word for line in body for word in line.split()]
    docBodyScore={i:docBodies.count(i) for i in docBodies}
    docTitleScore={i:docTitles.count(i)*10 for i in docTitles}
    docscore={k:docBodyScore.get(k,0)+docTitleScore.get(k,0) for k in set(docBodyScore)|set(docTitleScore)}
    querysearch={}
    scorecalc={}
    for query in queries:
        querysearch[query]=[]
        scorecalc[query]=[]
    for query in querysearch:
        for docs in docscore:
            if docs.startswith(query):
                querysearch[query].append(docs)
    for query in querysearch:
        y=[]
        scorecalc[query]=[]
        for docs in querysearch[query]:
            y.append(int(docscore[docs]))
        if len(y)==0:
            scorecalc[query].append(0)
        else:
            b=max(y)
            scorecalc[query].append(b)
    return scorecalc
