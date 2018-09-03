import time

# INSERTION SORT
'''
def insertion_sort(A):
    for index in range(1,len(A)):
        currentvalue = A[index]
        position = index
        print "CurrentValue:::",currentvalue
        print "Postion:::",position
        while position > 0 and A[position-1] > currentvalue:
            A[position] = A[position-1]
            position -= 1
        A[position] = currentvalue

A = ['a','c','b','e','d','f']
B = [10,43,54,67,1,99,12]
c = insertion_sort(B)
print B

'''


# BUBBLE SORT

'''
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        print "passnum::",passnum
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                #temp = alist[i]
                #alist[i] = alist[i+1]
                #alist[i+1] = temp
                alist[i],alist[i+1]=alist[i+1],alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
'''


# MERGE SORT:
'''
def mergesort(A):
    start_time = time.time()
    print "Splitting :",A
    if len(A) > 1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0 # left half iterator
        j = 0 # right half iterator
        k = 0 # Position of new SORTED ARRAY

        while i < len(lefthalf) and j <len(righthalf):
            print "**** INSIDE FIRST WHILE LOOP ****"
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i = i+1
                print "I now has new value::",i
                #print "K now has new value::",k
                print "A[k] now contains::",A[k]
                print "A[k] got this value from lefthalf"
                print "K's VALUE::",k
            else:
                A[k] = righthalf[j]
                j = j+1
                print "J now has new value::",j
                print "A[k] now contains::",A[k]
                print "A[k] got this value from righthalf"
                print "K's VALUE::",k
            k = k+1
            print "K now has new value::",k

        while i < len(lefthalf):
            print " ***** INSIDE SECOND WHILE LOOP ****"
            A[k] = lefthalf[i]
            print "A[K] now contains::",A[k]
            print "A[k] got this value from lefthalf"
            print "A[k] index is::",k
            i = i+1
            k = k+1
            print "I now has new value::",i
            print "K now has new value::",k

        print "Value of J::",j
        while j < len(righthalf):
            print " ***** INSIDE THIRD WHILE LOOP ****"
            A[k] = righthalf[j]
            print "A[k] now contains::",A[k]
            j = j+1
            k = k+1
            print "J now has new value::",j
            print "K now has new value::",k


    print "Merging::",A
    end_time = time.time() - start_time
    print end_time



A = [54,26,93,17,77,31,44,55,20,34,566]
mergesort(A)

'''

# SELECTION SORT
# TIme complexity of SELECTION SORT is (O(n2))
'''
def selection_sort(a):
    i=0
    while i<len(a):
        print "Iteration ##",i
        smallest = min(a[i:])
        #print smallest,type(smallest)
        index_of_smallest = a.index(smallest)
        print "INDEX_OF_SMALLEST::",index_of_smallest
        a[i],a[index_of_smallest] = a[index_of_smallest],a[i]
        i=i+1

    print a

A = [54,26,93,17,77,31,44,55,20,34]
selection_sort(A)
'''
'''
def selection_sort(a):
    for i in range(0,len(a)):
        least = i
        for j in range(i+1,len(a)):
            if a[j] < a[least]:
                least = j
                #print least
        print "After %s PASS, the LEAST item is %s"%(i,a[least])
        a[least],a[i]=a[i],a[least]
        #print a

    print a
A = [54,26,93,17,77,31,44,55,20,34]
B = ['P','Y','T','H','O','N']
selection_sort(A)

'''
'''
def sort_new(a):
    list_len = len(a)
    for i in range(0,list_len):
        for j in range(0,list_len-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print a
A = [54,26,93,17,77,31,44,55,20,34]
sort_new(A)
'''