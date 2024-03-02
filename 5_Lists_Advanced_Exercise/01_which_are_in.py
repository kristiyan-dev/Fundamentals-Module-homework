def filter_substrings(sequence1, sequence2):
    result = [substring1 for substring1 in sequence1 if any(substring1 in string2 for string2 in sequence2)]
    return result

input_sequence1 = input().split(", ")
input_sequence2 = input().split(", ")

filtered_substrings = filter_substrings(input_sequence1, input_sequence2)
print(filtered_substrings)
