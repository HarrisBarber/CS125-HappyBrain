from tkinter import *
import health_state

class Questionnaire:
   
    def __init__(self, oldValues):
        self.TITLE_FONT = ('Arial', 16)
        self.FONT = ('Arial', 12)
        self.root = Tk()
        OPTIONS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        title = Label(self.root, text = "Mental Health Questionnaire", font = self.TITLE_FONT)
        title.grid(row = 0, column = 1, columnspan = 1, padx = 10, pady = 8, sticky = N)

        rating = Label(self.root, text = "Rate from 0 (extremely disagree) to 9 (extremely agree)", 
            font = self.FONT)

        rating.grid(row = 1, column = 1, columnspan = 1, padx = 10, pady = 7, sticky = N)

        q1 = Label(self.root, text = "Do you blame yourself for everything bad that happens?", 
            font = self.FONT)

        q1.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v1 = StringVar(self.root)
        self.v1.set(oldValues[1])

        q1Options = OptionMenu(self.root, self.v1, *OPTIONS)
        q1Options.grid(row = 2, column = 2, columnspan = 2, sticky = E)


        q2 = Label(self.root, text = "Do you feel you would kill yourself if you had the chance?", 
            font = self.FONT)

        q2.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v2 = StringVar(self.root)
        self.v2.set(oldValues[2])

        q2Options = OptionMenu(self.root, self.v2, *OPTIONS)
        q2Options.grid(row = 3, column = 2, columnspan = 2, sticky = E)


        q3 = Label(self.root, text = "Do you feel you are being punished?", font = self.FONT)
        q3.grid(row = 4, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v3 = StringVar(self.root)
        self.v3.set(oldValues[3])

        q3Options = OptionMenu(self.root, self.v3, *OPTIONS)
        q3Options.grid(row = 4, column = 2, columnspan = 2, sticky = E)


        q4 = Label(self.root, text = "Do you feel the future is hopeless and that things cannot improve?", 
            font = self.FONT)

        q4.grid(row = 5, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v4 = StringVar(self.root)
        self.v4.set(oldValues[4])

        q4Options = OptionMenu(self.root, self.v4, *OPTIONS)
        q4Options.grid(row = 5, column = 2, columnspan = 2, sticky = E)


        q5 = Label(self.root, text = 
            "Are you failing to fulfill your responsibilities such as your career or relationships?", font = self.FONT)

        q5.grid(row = 6, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v5 = StringVar(self.root)
        self.v5.set(oldValues[5])

        q5Options = OptionMenu(self.root, self.v5, *OPTIONS)
        q5Options.grid(row = 6, column = 2, columnspan = 2, sticky = E)


        q6 = Label(self.root, text = " Do you feel that you can’t make decisions at all anymore?", 
            font = self.FONT)

        q6.grid(row = 7, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v6 = StringVar(self.root)
        self.v6.set(oldValues[6])

        q6Options = OptionMenu(self.root, self.v6, *OPTIONS)
        q6Options.grid(row = 7, column = 2, columnspan = 2, sticky = E)


        q7 = Label(self.root, text = "Are you too tired to do anything?", font = self.FONT)
        q7.grid(row = 8, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v7 = StringVar(self.root)
        self.v7.set(oldValues[7])

        q7Options = OptionMenu(self.root, self.v7, *OPTIONS)
        q7Options.grid(row = 8, column = 2, columnspan = 2, sticky = E)


        q8 = Label(self.root, text = "Are you so sad and unhappy that you can’t stand it?", font = self.FONT)
        q8.grid(row = 9, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v8 = StringVar(self.root)
        self.v8.set(oldValues[8])

        q8Options = OptionMenu(self.root, self.v8, *OPTIONS)
        q8Options.grid(row = 9, column = 2, columnspan = 2, sticky = E)


        q9 = Label(self.root, text = "Do you feel irritated all the time?", font = self.FONT)
        q9.grid(row = 10, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v9 = StringVar(self.root)
        self.v9.set(oldValues[9])

        q9Options = OptionMenu(self.root, self.v9, (*OPTIONS))
        q9Options.grid(row = 10, column = 2, columnspan = 2, sticky = E)


        q10 = Label(self.root, text = "Are you dissatisfied or bored with everything?", font = self.FONT)
        q10.grid(row = 11, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v10 = StringVar(self.root)
        self.v10.set(oldValues[10])

        q10Options = OptionMenu(self.root, self.v10, *OPTIONS)
        q10Options.grid(row = 11, column = 2, columnspan = 2, sticky = E)


        q11 = Label(self.root, text = "Have you lost all of your interest in other people?", font = self.FONT)
        q11.grid(row = 12, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v11 = StringVar(self.root)
        self.v11.set(oldValues[11])

        q11Options = OptionMenu(self.root, self.v11, *OPTIONS)
        q11Options.grid(row = 12, column = 2, columnspan = 2, sticky = E)

        
        q12 = Label(self.root, text = "Have you exclusively stayed indoors recently?", 
            font = self.FONT)

        q12.grid(row = 13, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v12 = StringVar(self.root)
        self.v12.set(oldValues[12])

        q12Options = OptionMenu(self.root, self.v12, *OPTIONS)
        q12Options.grid(row = 13, column = 2, columnspan = 2, sticky = E)


        q13 = Label(self.root, text = "Do you have very little or no appetite at all anymore?", 
            font = self.FONT)

        q13.grid(row = 14, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = W)

        self.v13 = StringVar(self.root)
        self.v13.set(oldValues[13])

        q13Options = OptionMenu(self.root, self.v13, *OPTIONS)
        q13Options.grid(row = 14, column = 2, columnspan = 2, sticky = E)


        buttonFrame = Frame(master = self.root)
        buttonFrame.grid(row = 99, column = 3, columnspan = 2, padx = 10, pady = 10, sticky = E + S)

        confirmButton = Button(
            master = buttonFrame, text = 'Confirm', font = self.FONT, command = self._on_confirm)

        confirmButton.grid(row = 0, column = 0, pady = 10)

        cancelButton = Button(
            master = buttonFrame, text = 'Cancel', font = self.FONT, command = self._on_cancel)

        cancelButton.grid(row = 0, column = 1,  pady = 10)

        self.confirm = False
        self.iterations = int(oldValues[0]) + 1


    def _on_confirm(self):
        self.confirm = True
        self.root.destroy()

    def _on_cancel(self):
        self.root.destroy()

    def start(self):
        self.root.mainloop()



if __name__ == '__main__':
    oldValues = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    Questionnaire(oldValues).start()