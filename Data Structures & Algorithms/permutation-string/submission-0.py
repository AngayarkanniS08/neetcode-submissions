class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        window = {}

        s1_count = {}

        if len(s1) > len(s2):
            return False

        for letter in s1:
            if letter in s1_count:
                s1_count[letter] += 1
            else:
                s1_count[letter] = 1

        for right in range(len(s2)):
            if s2[right] in window:
                window[s2[right]] +=1

            else:
                window[s2[right]] = 1

            if right - left + 1 == len(s1):
                
                if (window == s1_count):
                    return True

                window[s2[left]] -= 1 
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left+=1
        
        return False
