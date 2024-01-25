tail = input()
body = input()
head = input()

new_list = [tail, body, head]
new_list[0], new_list[2], = new_list[2], new_list[0]
print(new_list)
