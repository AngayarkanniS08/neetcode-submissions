class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for string in strs:
                sorted_key = "".join(sorted(string))
                if sorted_key not in anagram:
                    anagram[sorted_key] = []
                    
                anagram[sorted_key].append(string)
        return list(anagram.values())
        

        
