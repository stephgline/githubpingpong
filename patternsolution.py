class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(" ")
        letters = list(pattern)
        patterndict = {}
        wordict = {}
        for i in range(len(letters)):
            if letters[i] in patterndict:
                patterndict[letters[i]].append(i)
            else:
                patterndict[letters[i]] = [i]
                
        for j in range(len(words)):
            if words[j] in wordict:
                wordict[words[j]].append(j) # this method will give you a list of matching locations
            else:
                wordict[words[j]] = [j]
       
        count = 0
    	for key in patterndict:
    		if patterndict[key] in wordict.values():
    			count = count + 0
    		else:
    			count = count + 1
    	if len(wordict) != len(patterndict):
    		count = count +1
    	if count == 0:
    	    return True
    	else:
    	    return False
        