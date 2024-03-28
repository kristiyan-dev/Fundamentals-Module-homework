sequence = input().split()
new_sequence = ""

for word in sequence:
    repeat_count = len(word)
    new_sequence += word * repeat_count

print(new_sequence)

# data = input().split()
# repeat_text = [text * len(text) for text in data]
# print(repeat_text)