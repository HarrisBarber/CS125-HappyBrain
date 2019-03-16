import webbrowser
from tkinter import *
from fitbit_data import *


therapy_url = 'https://www.betterhelp.com/start/'
hiking_urls = ['https://www.alltrails.com/','https://www.traillink.com/activity/hiking-trails/']
yoga_url = 'https://www.glo.com/'
social_url = 'https://www.meetup.com/cities/us/ca/irvine/book-clubs/'
diet_url = 'https://www.weightwatchers.com/us/'


class Guidance:

    def __init__(self, name):
        self.root = Tk()

        f = open(name, "r")
        self.answers =[]
        answer = "start"

        while answer:
            answer = f.readline().strip()
            self.answers.append(answer)
        f.close()


    def check_emergency(self):
        msg = ""
        recent_suicide = int(self.answers[3])
        avg_suicide = float(self.answers[17])
        need_newline = False

        if (recent_suicide > 6):
            msg = "1. Please call the suicide hotline: 1-800-273-8255\n"
            need_newline = True

        if (recent_suicide - avg_suicide < -2):
            if (need_newline == False):
                msg += "1. "
            msg += "Keep being positive!\n"
            need_newline = True
        elif (recent_suicide - avg_suicide > 2):
            if (need_newline == False):
                msg += "1. "
            msg += "Please seek professional help quickly.\n"
            need_newline = True
        
        if (need_newline):
            msg += "\n"
        return msg


    def check_therapy(self):
        msg = ""
        link_therapy = False
        need_newline = False
        recent_blame = int(self.answers[2])
        recent_suicide = int(self.answers[3])
        recent_punished = int(self.answers[4])

        if (recent_blame + recent_suicide + recent_punished > 20):
            msg += "2. We strongly suggest you seek professional therapy.\n"
            need_newline = True
        elif (recent_blame + recent_suicide + recent_punished > 12):
            msg += "2. Your have some issues you might want to work out with a therapist.\n"
            need_newline = True

        if (recent_blame + recent_suicide + recent_punished > 12):
            msg += "Try out this therapy service.\n"
            link_therapy = True
            need_newline = True

        if (need_newline):
            msg += "\n"
        return msg, link_therapy


    def check_goals(self):
        msg = ""
        need_newline = False
        recent_future = int(self.answers[5])
        recent_responsibilities = int(self.answers[6])
        recent_decisions = int (self.answers[7])
        avg_future = float(self.answers[19])
        avg_responsibilities = float(self.answers[20])
        avg_decisions = float(self.answers[21])

        if (recent_future + recent_responsibilities + recent_decisions > 20):
            msg += "3. Set small, reachable goals for yourself and write them down.\n"
            need_newline = True

        if ((recent_future + recent_responsibilities + recent_decisions) - (avg_future + avg_responsibilities + avg_decisions) < -6):
            if (need_newline == False):
                msg += "3. "
            msg += "You've been very productive lately. Good job!\n"
            need_newline = True

        if (need_newline):
            msg += "\n"
        return msg


    def check_fun(self):
        msg = ""
        link_fun = False
        recent_tired = int(self.answers[8])
        recent_sad = int(self.answers[9])
        recent_irritated = int (self.answers[10])
        recent_bored = int(self.answers[11])

        if (recent_tired + recent_sad + recent_irritated + recent_bored > 16):
            msg += "4. Here's a fun activity you can do!\n\n"
            link_fun = True
        return msg, link_fun


    def check_irritated(self):
        msg = ""
        link_yoga = False
        recent_irritated = int (self.answers[10])
        if (recent_irritated > 5):
            msg += "5. Try out yoga to relax!\nHere's a service you can use.\n\n"
            link_yoga = True
        return msg, link_yoga


    def check_social(self):
        msg = ""
        link_social = False
        recent_bored = int(self.answers[11])
        avg_bored = float(self.answers[25])
        recent_interest = int(self.answers[12])
        avg_interest = float(self.answers[26])
        recent_social = int(self.answers[13])
        avg_social = float(self.answers[27])

        if (recent_bored + recent_interest + recent_social > 12):            
            msg += "6. Socializing with people is good for your mental health and helps with seasonal depression.\n" 
            msg += "Here's a service you can use to meet new people.\n"
            link_social = True
        else:
            msg += "6. Your social life is in good condition.\n"

        if ((recent_bored + recent_interest + recent_social) - (avg_bored + avg_interest + avg_social) > 6):
            msg += "You need to get outside, fast!\n"
        elif ((recent_bored + recent_interest + recent_social) - (avg_bored + avg_interest + avg_social) < -6):
            msg +=  "You've been extra social lately. Keep up the great work!\n"

        msg += "\n"
        return msg, link_social


    def check_diet(self):
        msg = ""
        link_diet = False
        recent_appetite = int(self.answers[14])
        avg_appetite = float(self.answers[28])

        if (recent_appetite > 5):
            msg += "7. Here's a service you can use to keep you on a diet!\n"
            link_diet = True

        if (recent_appetite - avg_appetite > 2):
            if (link_diet == False):
                msg += "7. "
            msg += "Try harder to keep up with your diet!\n"
        elif (recent_appetite - avg_appetite < -2):
            if (link_diet == False):
                msg += "7. "
            msg += "Good job keeping up with your diet!\n"

        msg += '\n'
        return msg, link_diet

    def give_guidance(self):
        emergency_msg = self.check_emergency()
        therapy_msg, link_therapy = self.check_therapy()
        goals_msg = self.check_goals()
        fun_msg, link_fun = self.check_fun()
        irritated_msg, link_yoga = self.check_irritated()
        social_msg, link_social = self.check_social()
        diet_msg, link_diet = self.check_diet()

        msg = Message(self.root, text = emergency_msg + therapy_msg + goals_msg + fun_msg + 
            irritated_msg + social_msg + diet_msg)

        total_avg = avg_number(get_recents(self.answers))
        color = 'lightgreen' if total_avg < 4 else 'lightblue' if total_avg < 6 else 'red'
        msg.config(bg = color, font= ('Times New Roman', 18, 'bold'))
        msg.pack()

        self.root.mainloop()
        
        test = False
        if (test == False):
            self.open_links(link_therapy, link_fun, link_yoga, link_social, link_diet)


    def open_links(self, link_therapy, link_fun, link_yoga, link_social, link_diet):
        if (link_therapy):
            webbrowser.open_new_tab(therapy_url)
        if (link_fun):
            webbrowser.open_new_tab(hiking_urls[0])
        if (link_yoga):
            webbrowser.open_new_tab(yoga_url)
        if (link_social):
            webbrowser.open_new_tab(social_url)
        if (link_diet):
            webbrowser.open_new_tab(diet_url)


def get_recents(l:list):
    result = []
    recents = l[2:14]
    for recent in recents:
        result.append(float(recent))
    return result

def get_avgs(l:list):
    result = []
    averages = l[15:-2]
    for average in averages:
        result.append(float(average))
    return result

def avg_number(l:list):
    n = sum(l)/len(l)
    return n

def get_name2(name):
    s = "state_questionnaire_"
    nameList = name.split()
    for word in nameList:
        if (word != nameList[-1]):
            s += word.lower() + "_"
        else:
            s += word.lower()
    s += ".txt"
    return s

if __name__ == '__main__':
    testing = True
    if (testing):
        s = 'state_questionnaire_bad.txt'
    else:
        s = get_name2(input())
    
    g = Guidance(s)
    g.give_guidance()