from tkinter import *

class prompt:

    def __init__(self):
        self.TITLE_FONT = ('Times New Roman', 20)
        self.FONT = ('Arial', 12)
        self.root = Tk()

        title = Label(self.root, text = "Welcome to Happy Brain!", font = self.TITLE_FONT, foreground='red')
        title.grid(row = 0, column = 1, columnspan = 1, pady = 8, sticky = N)


        name = Label(self.root, text = "Name:", font = self.FONT)
        name.grid(row = 1, column = 0, columnspan = 1, padx = 10, pady = 8, sticky = W)


        self.nameVar = StringVar(self.root)
        entry = Entry(self.root, textvariable = self.nameVar)
        entry.grid(row = 1, column = 1, columnspan = 1, pady = 8, sticky = W)


        self.ansVar = StringVar()
        self.ansVar.set("Yes")

        question = Label(self.root, text = "Do you want to do the questionnaire? (default: Yes)", 
            font = self.FONT)

        question.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 8, sticky = W)

        ans1 = Radiobutton(self.root, text="Yes", variable=self.ansVar, value="Yes")
        ans1.grid(row = 2, column = 1, columnspan = 1, sticky = W)

        ans2 = Radiobutton(self.root, text="No", variable=self.ansVar, value="No")
        ans2.grid(row = 3, column = 1, columnspan = 1, sticky = W)


        buttonFrame = Frame(master = self.root)
        buttonFrame.grid(row = 99, column = 3, columnspan = 2, padx = 10, pady = 10, sticky = E + S)

        confirmButton = Button(
            master = buttonFrame, text = 'Confirm', font = self.FONT, command = self._on_confirm)

        confirmButton.grid(row = 0, column = 0, pady = 10)

        cancelButton = Button(
            master = buttonFrame, text = 'Cancel', font = self.FONT, command = self._on_cancel)

        cancelButton.grid(row = 0, column = 1,  pady = 10)

        self.confirm = False

    def _on_confirm(self):
        self.confirm = True
        self.root.destroy()

    def _on_cancel(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    prompt().start()