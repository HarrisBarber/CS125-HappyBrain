<<<<<<< HEAD
import questionnaire as quest
import prompt

def get_name(name):
    s = "state_questionnaire_"
    nameList = name.split()
    for word in nameList:
        if (word != nameList[-1]):
            s += word.lower() + "_"
        else:
            s += word.lower()
    s += ".txt"
    return s

def get_values(q):
    newValues = [str(q.iterations), q.v1.get(), q.v2.get(), q.v3.get(), q.v4.get(), q.v5.get(), q.v6.get(), 
        q.v7.get(), q.v8.get(), q.v9.get(), q.v10.get(), q.v11.get(), q.v12.get(), q.v13.get()]
    return newValues

def read_state(f):
    oldValues = []
    avgValues = []
    section = "ITERATION"
    for value in f.readlines():
        if (value.strip() == "RECENT"):
            section = "RECENT"
        elif (value.strip() == "AVERAGE"):
            section = "AVERAGE"
        elif (section == "RECENT"):
            oldValues.append(value.strip())
        elif (section == "AVERAGE"):
            avgValues.append(value.strip())
        else:
            oldValues.append(value.strip())
            avgValues.append(value.strip())
    return oldValues, avgValues

def write_state_questionnaire(f, oldValues, avgValues, userCheck):
    q = quest.Questionnaire(oldValues)
    q.start()
    if ((q.confirm) == False):
        return 0

    f.seek(0)
    f.truncate()
    newValues = get_values(q)
    f.write(newValues[0] + "\n")

    f.write("RECENT\n")
    for i in range(1, 14):
        f.write(newValues[i] + "\n")

    f.write("AVERAGE\n")
    if (userCheck == "new"):
        for i in range(1, 14):
            f.write(newValues[i] + "\n")
    else:
        for i in range(1, 14):
            f.write(str((int(newValues[i]) + (float(avgValues[i]) * int(avgValues[0])))/
                int(newValues[0]))  + "\n")
    return 0

def write_state():
    p = prompt.prompt()
    p.start()
    s = get_name(p.nameVar.get())
    answer = p.ansVar.get()
    if (p.confirm == False):
        return 0
    if (answer != "Yes"):
        return 0
    try:
        f = open(s, "r+")
        oldValues, avgValues = read_state(f)
        write_state_questionnaire(f, oldValues, avgValues, "existing")
        f.close()
    except FileNotFoundError:
        f1 = open(s, 'w+')
        oldValues = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        write_state_questionnaire(f1, oldValues, [], "new")
        f1.close()

if __name__ == '__main__':
    write_state()
