#WAP TO FIND THE 2nd MOST FREQUENT CHARACTER IN A STRING
#------------------------------------------------------#.

string = "aabbbccdeee"

# Step 1: Count frequency of each character
freq = {}
for ch in string:
  if ch in freq:
    freq[ch] += 1
  else:
    freq[ch] = 1

# Step 2: Find the two highest counts
values = list(freq.values())
values.sort(reverse=True)

if len(values) >= 2:
 second_highest = values[1]
 # Step 3: Find the character with that frequency
 for ch in freq:
   if freq[ch] == second_highest:
     print("Second most frequent character:", ch)
     break
else:
    print("Not enough unique characters.")
