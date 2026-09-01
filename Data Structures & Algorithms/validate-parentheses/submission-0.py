class Solution:
    def isValid(self, s: str) -> bool:
        brackets_seen = []
        mapping = {")": "(", "}": "{", "]": "["}

        for brackets in s:
            if brackets in mapping:
                if brackets_seen and brackets_seen[-1] == mapping[brackets]:
                    brackets_seen.pop()
                else:
                    return False
            else:
                brackets_seen.append(brackets)
        
        if len(brackets_seen)==0:
            return True
        else:
            return False
       



