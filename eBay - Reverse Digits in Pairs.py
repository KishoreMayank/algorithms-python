'''
# coding: utf-8

# Given a number, generate a number formed by reversing the digits of the number in pairs.
# 
# For example, 
# 
# If you have a number 12345678, then the resulting number after reversing in pairs should be 21436587.
# 
# If the numbers of digits in the number are odd, then the last digit should not be replaced while doing pairwise reverse.
# 
# So, for the number 72158, the number after applying this algorithm should be 27518.
'''

def reverseDigits(n):
    m=list(str(n))
    for i in range(1,len(m),2):
        temp=m[i]
        m[i]=m[i-1]
        m[i-1]=temp
    p=''.join(m)
    w = int(p)
    return w
