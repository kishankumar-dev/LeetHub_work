class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ar=[]
        for i in matrix:
            ar=ar+i
        count=0
        for i in ar:
            if i==target:
                count+=1
        if count>0:
            return True
        else:
            return False