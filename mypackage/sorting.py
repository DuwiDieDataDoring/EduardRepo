def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    print(items)
    return(items)

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        #recursion
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

        print(items)
        return items

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    less = []
    equal = []
    greater = []
    if len(items) > 1:
        pivot = items[0]
        for x in items:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return items
