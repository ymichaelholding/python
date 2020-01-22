def sorted_by_length(input_list):
    temp_dict = {}
    final_list = []
    for i in input_list:
        temp_dict[len(i)] = i
    for i in sorted(temp_dict.keys(),reverse=True):
        final_list.append(temp_dict[i])
    print(final_list)

test=['abv', 'ggggg', 'hhhhhh', 'ttttttt', 'holdinmichael']
sorted_by_length(test)
