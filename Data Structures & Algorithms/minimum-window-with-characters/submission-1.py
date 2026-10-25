class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        required = len(need)
        # print(required)

        formed = 0
        window = {}
        min_length = float('inf')
        min_window = ""

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] +=1
            else:
                window[s[right]] = 1

            char = s[right]
            if char in need and window[char] ==  need[char]:
                formed+=1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]
                window[s[left]] -=1

                if char in need and  window[s[left]] < need[s[left]]:
                    formed -= 1
                left+=1

        return min_window


                
            
 
        


        