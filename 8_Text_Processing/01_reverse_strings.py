# while True:
#     word = input()
#
#     if word == "end":
#         break
#
#     print(f"{word} = {word[::-1]}")

command = input()

while command != "end":
    current_word = command
    word_reversed = ""
    for text in reversed(current_word):
        word_reversed += text
    print(f"{current_word} = {word_reversed}")
    command = input()