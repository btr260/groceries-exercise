#list comprehension - it's like a 1 line for loop

my_numbers = [1, 2, 3, 4, 5, 6, 7]

print("ORIGINAL LIST", my_numbers)

# MAPPED LIST: [100, 200, 300, ..., 700]

#could do traditional approach...

#mapped_list=[]
#for i in my_numbers:
#    mapped_list.append(i * 100)

# or you could use list comprehension!

mapped_list=[i*100 for i in my_numbers]

print("MAPPED LIST", mapped_list)


# FILTERED LIST: [4, 5, 6, 7]

# could do traditional approach
#filtered_list = []
#for i in my_numbers:
#    if i > 3:
#        filtered_list.append(i)

# OR could use list comprehension!

filtered_list=[i for i in my_numbers if i>3]

print(filtered_list)
