def loading_bar(percentage):
    loading = percentage // 10
    bar = "[" + "%" * loading + "." * (10 - loading) + "]"
    if percentage == 100:
        return f"{percentage}% Complete!\n{bar}"
    return f"{percentage}% {bar}\nStill loading..."


input_number = int(input())
loading_bar = loading_bar(input_number)
print(loading_bar)
