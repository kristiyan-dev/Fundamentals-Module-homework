import tkinter as tk

window = tk.Tk()
window.geometry('600x600')
window.title('test')


# window.resizable(False, False)
# window.configure(background='white')

def first_print():
    text = 'Hello Word'
    text_output = tk.Label(window, text=text)
    text_output.grid(row=0, column=1)


first_button = tk.Button(text='Hello', command=first_print)
first_button.grid(row=0, column=0)

if __name__ == '__main__':
    window.mainloop()
