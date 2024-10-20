class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop() 
                operator = stack.pop()
                
                if operator == '!':
                    result = not self.to_bool(sub_expr[0])
                elif operator == '&':
                    result = all(self.to_bool(val) for val in sub_expr)
                elif operator == '|':
                    result = any(self.to_bool(val) for val in sub_expr)
                
                stack.append('t' if result else 'f')
            elif char not in (',', ' '): 
                stack.append(char)
    
        return self.to_bool(stack.pop())
    
    def to_bool(self, char: str) -> bool:
        return char == 't'
