# example list:
a_list = [1, 2, 5, 6, 5, 2, 12]

# copy list to avoid mutation:
b_list = a_list.copy()

# set up list to store results:
result = []

# loop through list:
for num in b_list:

    # check that num doesn't exist in result list:
    if num not in result:
    
        # if it doesn't exist add it
        result.append(num)

print(result)
