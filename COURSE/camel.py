s_1 = "CamelCase"
s_2 = "testThat"

gap = ''

def solution(s, idx=0):
    if s[idx].islower():
        low = s[idx]
        print (low)
    if s[idx].isupper():
        cap =  s[idx]
        #gap.join(cap)
        print (" " + cap)
    if idx == len(s) - 1:
        return "none found"
    return solution(s, idx+1)

print(solution(s_1))
print(solution(s_2))


'''
import re

s = "CamelCase"


def solution(s):
    #s = "CamelCase" 
    words = re.findall('[A-Z][a-z]*', s)
    words.split()
    return words[0,1]

print(solution(s))


s = "camelCase"
gap = '#'

def solution(s):
    for ch in range(len(s)):
        if s[ch].isupper():
            upper = s[ch].isupper()
            print(upper)
            s = gap.join(upper)
            #return s[ch]
            return s
            
print(solution(s))
'''
