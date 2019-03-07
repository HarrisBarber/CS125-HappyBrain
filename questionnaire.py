from tkinter import *

import health_state

class Questionnaire:
   
    def __init__(self):
        self.TITLE_FONT = ('Arial', 16)
        self.FONT = ('Arial', 12)
        self.root = Tk()

        title = Label(self.root, text="Mental Health Questionnaire", 
            font = self.TITLE_FONT)
        
        title.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10, sticky = N)

        q1 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q1.grid(row = 1, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q1v = StringVar(self.root)
        self.q1v.set("Average")

        q1Options = OptionMenu(self.root, self.q1v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q1Options.grid(row = 1, column = 2, columnspan = 2, sticky = E)


        q2 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q2.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q2v = StringVar(self.root)
        self.q2v.set("Average")

        q2Options = OptionMenu(self.root, self.q2v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q2Options.grid(row = 2, column = 2, columnspan = 2, sticky = E)


        q3 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q3.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q3v = StringVar(self.root)
        self.q3v.set("Average")

        q3Options = OptionMenu(self.root, self.q3v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q3Options.grid(row = 3, column = 2, columnspan = 2, sticky = E)


        q4 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q4.grid(row = 4, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q4v = StringVar(self.root)
        self.q4v.set("Average")

        q4Options = OptionMenu(self.root, self.q4v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q4Options.grid(row = 4, column = 2, columnspan = 2, sticky = E)


        q5 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q5.grid(row = 5, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q5v = StringVar(self.root)
        self.q5v.set("Average")

        q5Options = OptionMenu(self.root, self.q5v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q5Options.grid(row = 5, column = 2, columnspan = 2, sticky = E)


        q6 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q6.grid(row = 6, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q6v = StringVar(self.root)
        self.q6v.set("Average")

        q6Options = OptionMenu(self.root, self.q6v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q6Options.grid(row = 6, column = 2, columnspan = 2, sticky = E)


        q7 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q7.grid(row = 7, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q7v = StringVar(self.root)
        self.q7v.set("Average")

        q7Options = OptionMenu(self.root, self.q7v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q7Options.grid(row = 7, column = 2, columnspan = 2, sticky = E)


        q8 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q8.grid(row = 8, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q8v = StringVar(self.root)
        self.q8v.set("Average")

        q8Options = OptionMenu(self.root, self.q8v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q8Options.grid(row = 8, column = 2, columnspan = 2, sticky = E)


        q9 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q9.grid(row = 9, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q9v = StringVar(self.root)
        self.q9v.set("Average")

        q9Options = OptionMenu(self.root, self.q9v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q9Options.grid(row = 9, column = 2, columnspan = 2, sticky = E)


        q10 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q10.grid(row = 10, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q10v = StringVar(self.root)
        self.q10v.set("Average")

        q10Options = OptionMenu(self.root, self.q10v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q10Options.grid(row = 10, column = 2, columnspan = 2, sticky = E)


        q11 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q11.grid(row = 11, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q11v = StringVar(self.root)
        self.q11v.set("Average")

        q11Options = OptionMenu(self.root, self.q11v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q11Options.grid(row = 11, column = 2, columnspan = 2, sticky = E)


        q12 = Label(self.root, text = "How do you feel?", font = self.FONT)

        q12.grid(row = 12, column = 0, columnspan = 1, padx = 10, pady = 6, sticky = W)

        self.q12v = StringVar(self.root)
        self.q12v.set("Average")

        q12Options = OptionMenu(self.root, self.q12v, "Terrible", "Bad", "Average", "Good", "Great")
    
        q12Options.grid(row = 12, column = 2, columnspan = 2, sticky = E)


        buttonFrame = Frame(master = self.root)

        buttonFrame.grid(row = 99, column = 3, columnspan = 2, padx = 10, pady = 10, sticky = E + S)

        confirmButton = Button(
            master = buttonFrame, text = 'Confirm', font = self.FONT, command = self._on_confirm)

        confirmButton.grid(row = 0, column = 0, pady = 10)

        cancelButton = Button(
            master = buttonFrame, text = 'Cancel', font = self.FONT, command = self._on_cancel)

        cancelButton.grid(row = 0, column = 1,  pady = 10)

        self.okay = False


    def _on_confirm(self):
        self.okay = True
        print(self.q1v.get())
        print(self.q2v.get())
        print(self.q3v.get())
        print(self.q4v.get())
        print(self.q5v.get())
        print(self.q6v.get())
        print(self.q7v.get())
        print(self.q8v.get())
        print(self.q9v.get())
        print(self.q10v.get())
        print(self.q11v.get())
        print(self.q12v.get())

        self.root.destroy()

    def _on_cancel(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()




if __name__ == '__main__':
    Questionnaire().start()