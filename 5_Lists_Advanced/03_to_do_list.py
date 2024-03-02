notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    text = command.split("-")
    priority = int(text[0]) - 1
    note = text[1]
    notes.pop(priority)
    notes.insert(priority, note)
result = [element for element in notes if element != 0]
print(result)