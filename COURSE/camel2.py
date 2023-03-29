#https://www.pythontutorial.net/python-regex/python-regex-sub/
import re

def solution(s):
    #the re.sub function returns a string after replacing the matched pattern
    #re.sub(pattern, repl, string, count=0, flags=0)
    
    # finds an uppercase letter and replaces it with the letter before it, a space and itself:
    #             "word character | caps A-Z"  
    it = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
    # finds an uppercase letter and replaces it with a space and itself:
    #it = re.sub(r"([A-Z])", r" \1", s)
    return it
 
print(solution("wordInTheCamelCases"))

