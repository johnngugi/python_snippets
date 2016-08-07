def mergesort(lists):

    if len(lists) > 1:    # if list is only 1 element it is already sorted
        mid = len(lists)/2
        left = lists[:mid]  # divides list into two
        right = lists[mid:]
        
        mergesort(left)  # continues to divide list recursively
        mergesort(right)
        
        
        a = 0  # placeholder values
        b = 0
        c = 0
        
        while a < len(left) and b < len(right):  # compares both sides of separated list
        
            if left[a] < right[b]:
                lists[c] = left[a]
                a += 1
            else:
                lists[c] = right[b]
                b += 1
            c += 1
            
        while a < len(left): # sorts left side
            lists[c] = left[a]
            a += 1
            c += 1
            
        while b < len(right): # sorts right side
            lists[c] = right[b]
            b += 1
            c += 1
                
example = [25,30,31, 7, -75, 1]            
mergesort(example)
print example


