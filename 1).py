list = [1, 2, 3, 4, 3, 2, 1, 5]
def unique_elements(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


result = unique_elements(list)
print(result)