WORK_TIME = 25 * 60
BREAK_TIME = 5 * 60

def next_pomodoro(state):
    if state == "work":
        return "break", BREAK_TIME
    return "work", WORK_TIME
