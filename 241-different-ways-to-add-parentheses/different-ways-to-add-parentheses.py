class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}
        
        def operators(ops,a,b):
            if ops == '+':
                return a+b 
            if ops == '*':
                return a*b
            if ops == '-':
                return a-b
        i = 0
        numbers = []
        while i <= len(expression)-1:
            if not expression[i].isdigit():
                numbers.append(expression[i])
                i += 1
                
            else:
                temp = ''
                while i <= len(expression)-1 and expression[i].isdigit():
                    temp += expression[i]
                    i += 1
                numbers.append(int(temp))
            
        
        def dfs(i,j):
            if i > j:
                return []
            if i == j:
                return [numbers[i]]
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = []
            for k1 in range(i,j+1):
                if type(numbers[k1]) != str:
                    continue 
                left = dfs(i,k1-1)
                right = dfs(k1+1,j)
                for les in left:
                    for res in right:
                        dp[(i,j)].append(operators(numbers[k1],les,res))
            return dp[(i,j)]
        return dfs(0,len(numbers)-1)