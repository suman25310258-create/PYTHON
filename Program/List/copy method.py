#WAP TO SHOW THE DIFFERENCE BETWEEN 'New_list=Old_list' AND 'New_list=Old_list.copy()' 

Old_list=[5,8,3,1,2]

#WHEN New_list=Old_list, 'New_list' JUST A REFERENCE COPY OF 'Old_list'. NO NEW LIST CREATED.
#THE BELOW CODING PROVE THIS MATTER. WHEN WE ADD ANYTHING TO 'New_list','Old_list' ALSO CHANGES.
#IDs OF THE TWO LISTS ARE SAME.  
New_list=Old_list
print(New_list)
New_list.append(20)
print(New_list)
print(Old_list)
print("ID of the Old-List : ", id(Old_list))
print("ID of the New-List : ", id(New_list))

print("\n")

#WHEN WE USE 'copy()' METHOD, 'NEW LIST' IS CREATED WHICH IS NOT JUST A REFERENCE COPY OF
#'Old_list'. 'Old_list' NOT CHANGES THIS TIME.
#IDs ARE DIFFERENT THIS TIME.
New_list=Old_list.copy()
print(New_list)
New_list.append(10)
print(New_list)
print(Old_list)
print("ID of the Old-List : ", id(Old_list))
print("ID of the New-List : ", id(New_list))