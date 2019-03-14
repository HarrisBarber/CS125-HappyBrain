import tkinter as tk
master = tk.Tk()
import webbrowser


urls = ['https://www.alltrails.com/','https://www.traillink.com/activity/hiking-trails/',
        'https://www.meetup.com/cities/us/ca/irvine/book-clubs/' ,'https://www.theoutbound.com/']




## reading text file from system.
f = open('state_questionnaire_aref.txt', "r")
line = f.readline()
info_list =[]

while line:
    line = f.readline().replace("\n", "")
    info_list.append(line)
f.close()


print(info_list)




def avg_list(l:list):
    result = []
    info = l[15:-2]
    for e in info:
        result.append(float(e))
    #print(result)
    return result


result = avg_list(info_list)

def avg_number(l:list):
    n = sum(l)/len(l)
    return n





main_info = avg_number(result)

print(main_info)
##########################################################


############################################################
def emergency_doctor(l:list):
    number2 = float(l[16])
    number1 = float(l[15])
    if (number1 > 7) or (number2 > 8):
        return ("Please go to your doctor and talk to him you are in emergency situation\n\n")
    else:
        return ("you are not in emregency  \n\n")

def activity_sol(l:list,w:list):
    number1 = float(l[-2])
    number2 = float(l[-3])
    if (number1 > 2) or (number2 > 2):
        for element in w:
            webbrowser.open_new_tab(element)
        return ("Spending time outside is good for your mental health "
                "and can help with seasonal depression. When paired with a physical activity, like hiking or running, the health "
                "benefits of going outside increase, and may include "
                "lower blood pressure and stress.You can use websites that open on your web "
                "browser to find hiking places,meet new people and outside activities  \n\n\n ")

    else:
        return ("It seems your social life is normal  \n\n")






































whatever_you_do = emergency_doctor(info_list)
whatever_you_do2 = activity_sol(info_list,urls)


#master.geometry('1200x1200')
msg = tk.Message(master, text = whatever_you_do + whatever_you_do2 )
msg.config(bg='lightblue', font=('times', 18, 'italic'))
msg.pack()
tk.mainloop()





#print(emergency_doctor(info_list))
