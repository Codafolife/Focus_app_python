import os

def add_task(to_do):
    print("What you wanna add bro")
    s = input()
    s+= " 0%"
    to_do.append(s)
    return to_do


def display_tasks(to_do):
    temp = 1
    print()
    for task in to_do:
        print(temp, ". ", task)
        temp+=1

def display_options():
    print("Press 1 to add new task, press 2 to update a task, press 3 to end for the day, press 4 to take a 5 minute break")

def update_task(to_do,task_id):

    clear()
    display_tasks(to_do)
    print("kitna hua")
    temp = int(input())
    if temp==50:
        st = to_do[task_id-1]
        st = st[:-4] + " 50%"
        to_do[task_id-1] = st
    elif temp == 100:
        st = to_do[task_id-1]
        st = st[:-4] + " 100%"
        to_do[task_id-1] = st
    else:
        print("Either do half or full idiot")

    return to_do

def clear():
    os.system('cls')