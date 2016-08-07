def quicksort(lists):   # initiates the sorting
    quickSortHelper(lists, 0, len(lists)-1)


def quickSortHelper(lists, first, last):
    if first < last:
        
        splitpoint = partition(lists, first, last)
        
        quickSortHelper(lists, first, splitpoint-1)
        quickSortHelper(lists, splitpoint + 1, last)
        

def partition(lists, first, last): #takes list, left mark and right mark as args
    
    pivot = lists[first] # defines the pivot point
    
    left = first + 1 # defines the left mark
    right = last # defines the right mark
    
    finished = False
    while not finished:
        
        while left <= right and lists[left] <= pivot: # moves the left mark toward the right
            left = left + 1
            
        while right >= left and lists[right] >= pivot: # moves right marker towards the left
            right = right - 1
            
        if right < left:
            finished = True
        else:                   # switches right mark and left mark
            temp = lists[left]
            lists[left] = lists[right]
            lists[right] = temp
            
    temp = lists[first]   # switches pivot point and right mark
    lists[first] = lists[right]
    lists[right] = temp
    
    return right


example = [25,30,31, 7, -75, 1]            
quicksort(example)
print example  
