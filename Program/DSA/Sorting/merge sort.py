# WAP TO DEMONSTRATE MERGE SORT USING 'append()' FUNCTION
#-------------------------------------------------------#
def mergesort(a):
  if len(a) <= 1:
    return a

  mid = len(a)//2
  left = mergesort(a[:mid])
  right = mergesort(a[mid:])

  return merge(left, right)

def merge(l, r):
   result = []
   i = j = 0

   while i < len(l) and j < len(r):
     if l[i] < r[j]:
        result.append(l[i]); i += 1
     else:
        result.append(r[j]); j += 1

   result += l[i:]
   result += r[j:]
   return result

a = [8,3,5,1,9]
print("The Unsorted List :",a)
print("The Sorted List :",mergesort(a))


# WAP TO DEMONSTRATE MERGE SORT USING 'sorted()' FUNCTION
#-------------------------------------------------------#
def mergesort(a):
  if len(a) <= 1:
    return a
  mid = len(a)//2
  left = mergesort(a[:mid])
  right = mergesort(a[mid:])
  return sorted(left + right)

a = [8,3,5,1,9]
print("\nThe Unsorted List :",a)
print("The Sorted List :",mergesort(a))
