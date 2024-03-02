current_text = [x for x in input().split() if len(x) % 2 == 0]
print(*current_text, sep="\n")