class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for temp in range(len(temperatures)):
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                pop_index = stack.pop()
                distance = temp - pop_index
                result[pop_index] = distance
            stack.append(temp)
        
        return result

        

