# import re
# # phone_numbers = input()
# # number_pattern = r"\+359(?P<separator>[ |-])[2](?P=separator)\d{3}(?P=separator)\d{4}\b"
# # valid_numbers = [obj.group() for obj in re.finditer(number_pattern,phone_numbers)]
# # print(*valid_numbers,sep=", ")

import re
numbers = input()
valid_phone_number = []
regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex, numbers)

for i in range(len(matches)):
    if i <len(matches) - 1:
        print(matches[i], end=", ")
    else:
        print(matches[i])
