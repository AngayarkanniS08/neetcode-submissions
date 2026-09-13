class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        for value in tokens:
            try:
                number = int(value)
                stack.append(number)
            except ValueError:
                first = stack.pop()
                second = stack.pop()
                
                if value == "+":
                    result = second + first
                elif value == "-":
                    result = second - first
                elif value == "*":
                    result = second * first
                elif value == "/":
                    result = int(second / first)

                stack.append(result)

        return stack[0]



            
        
    