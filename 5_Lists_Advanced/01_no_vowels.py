word = input()
sorted_text = [text for text in word if text.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(sorted_text))