sentence= "I LOVE MY COUNTRY VERY MUCH"

#ACCESSING AND COUNT EACH WORD OF A STRING USING 'for' LOOP
count=0
for word in sentence.split():
 count+=1
 print(word)
print(f"There are {count} words in the sentence: {sentence}")

#ACCESSING AND COUNT EACH WORD OF A STRING USING 'count()' METHOD
count=sentence.count(" ")+1
print("The number of words in string are :" + str(count))
print("The number of words in string are :",count)