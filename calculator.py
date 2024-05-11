from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Erro")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.geometry("400x600")

screen = StringVar()

entry = Entry(root, textvar = screen, font="lucida 20 bold")
entry.pack(fill=X, ipadx=8, pady=10, padx=10)

button_frame = Frame(root)
button_frame.pack()

lista_de_botoes = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '.', '0', '=', '+', 'C']

i = 0
for button_text in lista_de_botoes:
    button = Button(button_frame, text=button_text, font='lucida 15 bold')
    button.grid(row=int(i/4), column=i%4, padx=3, pady=3)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()