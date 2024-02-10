import tkinter as tk

window = tk.Tk()
window.geometry('600x600')
window.title('test')


# window.resizable(False, False)
# window.configure(background='white')

def first_print():
    text = 'Обичам те толкоша много! А ти обичашли ме?'
    text_output = tk.Label(window, text=text)
    text_output.grid(row=0, column=2)
def second_print():
    text = 'Happy'
    text_output = tk.Label(window, text=text)
    text_output.grid(row=1, column=2)
def third_print():
    text = 'Sad'
    text_output = tk.Label(window, text=text)
    text_output.grid(row=2, column=2)


first_button = tk.Button(text='click me', command=first_print)
first_button.grid(row=0, column=0)
second_button = tk.Button(text='Да', command=second_print)
second_button.grid(row=1, column=0)
third_button = tk.Button(text='Не', command=third_print)
third_button.grid(row=2, column=0)

if __name__ == '__main__':
    window.mainloop()

