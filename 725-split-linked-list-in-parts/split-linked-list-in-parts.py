class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        curr = head
        while curr:
            n += 1  
            curr = curr.next
        
        base = n // k 
        extra = n % k 
    
        res = []
        curr = head
        for i in range(k):
            part_head = curr 
            part_size = base + (1 if extra > 0 else 0) 
            extra -= 1  
            
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next 
                curr.next = None  
                curr = next_part  
            
            res.append(part_head) 
        
        return res