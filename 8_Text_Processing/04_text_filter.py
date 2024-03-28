# banned_word = input().split(", ")
# text = input()
#
# for ban_word in banned_word:
#     if ban_word in text:
#         new_symbol = "*" * len(ban_word)
#         text = text.replace(ban_word, new_symbol)
#
# print(text)

banned_words_list = input().split(", ")
text = input()

for banned_words in banned_words_list:
    text = text.replace(banned_words, "*" * len(banned_words))
print(text)