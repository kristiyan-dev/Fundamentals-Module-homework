number = int(input())

# for i in range(number):
#     sicret = int(input())
#     if sicret == 88:
#         print("Hello")
#         continue
#     if sicret == 86:
#         print('How are you?')
#         continue
#     if sicret < 88:
#         print('GREAT!')
#         continue
#     if sicret > 88:
#         print('Bye.')

for i in range(number):
    sicret = int(input())
    if sicret == 88:
        print("Hello")
    elif sicret == 86:
        print('How are you?')
    elif sicret < 88:
        print('GREAT!')
    elif sicret > 88:
        print('Bye.')
