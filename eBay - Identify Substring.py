'''
# coding: utf-8

# Given a string S and an array of patterns P, develop a function to find all possible substrings in the string that matches the pattern.
# 
# For example:-
# 
# 
# S = AMAZING
# 
# Pattern = [0,1,0] where 0 represents vowels and 1 represents consonants.
# 
# Resulting list of substrings will be [AMA,AZI]
'''


def findSubstring(word,pattern):
    lpattern = len(pattern)
    lword = len(word)
    subs =[]
    match=[]
    if lpattern<=lword:
        for i in range(lword-lpattern+1):
            subs.append(word[i:lpattern+i])
    for i in subs:
        i=i.upper()
        b=list(i)
        subpattern=[]
        for j in b:
            if j in ('A','E','I','O','U'):
                subpattern.append(0)
            else:
                subpattern.append(1)
        if subpattern==pattern:
            match.append(i)
    return match
