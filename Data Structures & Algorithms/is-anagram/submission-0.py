class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for letter in s:
            if letter not in count_s:
                count_s[letter] = 1
            else:
                count_s[letter] += 1
            
        for letter in t:
            if letter not in count_t:
                count_t[letter] = 1
            else:
                count_t[letter] +=1
    
        return(count_s==count_t)
            

