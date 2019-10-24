'''
# coding: utf-8

# Given 2 list of strings a and b, check whether strings in b are have strings from a as prefix or not.
# 
# For example:-
# 
# a=['one','two','three']
# 
# b=['onetwo','one']
# 
# The function should return True if and only if all the strings in b have some strings from a as prefix.
'''


def prefixString(a,b):
    p=[]
    for i in b:
        x=False
        for j in a:
            if i.startswith(j):
                x=True
        p.append(x)
    for i in p:
        if i==False:
            return False
        else:
            return True

