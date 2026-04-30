#WAP TO FIND LARGEST AND SMALLEST NUMBER OF THE LIST

numbers = [9, 37, 4, 250, 28, 6]

largest = smallest = numbers[0]

#Method1:- Using for() loop-1.
for i in numbers:
 if i > largest:
  largest = i
 if i < smallest:
  smallest = i
print("Largest number:", largest)
print("Smallest number:", smallest)

#Method2:- Using for() loop-2.
for i in range(1,len(numbers)):
 if numbers[i] > largest:
  largest = numbers[i]
 if numbers[i] < smallest:
  smallest = numbers[i]
print("Largest number:", largest)
print("Smallest number:", smallest)

#Method3:- Using for() and Slicing.
for i in numbers[1:]:
 if i > largest:
  largest = i
 if i < smallest:
  smallest = i
print("Largest number:", largest)
print("Smallest number:", smallest)


#Method4:- Using max() and min() function.
largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
