def mergesort(lists):

    if len(lists) > 1:    
        mid = len(lists)/2
        left = lists[:mid]
        right = lists[mid:]
        
        mergesort(left)
        mergesort(right)
        
        #print left
        #print right
        
        a = 0
        b = 0
        c = 0
        
        while a < len(left) and b < len(right):
        
            if left[a] < right[b]:
                lists[c] = left[a]
                a += 1
            else:
                lists[c] = right[b]
                b += 1
            c += 1
            
        while a < len(left):
            lists[c] = left[a]
            a += 1
            c += 1
            
        while b < len(right):
            lists[c] = right[b]
            b += 1
            c += 1
                
example = [25,30,31, 7, -75, 1]            
mergesort(example)
print example


