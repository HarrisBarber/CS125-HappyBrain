
def get_name():
    s = "state_"
    name = input("What is your name?")
    nameList = name.split()
    for word in nameList:
        if (word != nameList[-1]):
            s += word.lower() + "_"
        else:
            s += word.lower()
    s += ".txt"
    return s

def read_state(f):
    pass

def write_state2(f):
    pass

def write_state():
    s = get_name()
    try:
        f = open(s, "r")
        read_state(f)
        write_state2(f)
    except:
        f = open(s, 'w+')
        write_state2(f)

if __name__ == '__main__':
    pass