from Focus_app_functions import *
import subprocess
import time
    
process = subprocess.Popen(["python", "Blocker.py"])

print("Hello, please enter the tasks you want to complete today :")

s = input()
to_do = []

while s != "stop":
	s+= " 0%"
	to_do.append(s)
	s = input()

clear()

# That was the end of the setup phase, now we move on to the iterative phase 

while  True:
	display_tasks(to_do)
	display_options()
	t = int(input())
	clear()
	if t==1:
		display_tasks(to_do)
		to_do = add_task(to_do)
	elif t==2:
		display_tasks(to_do)
		print("Which task do you want to complete")
		temp = int(input())
		to_do = update_task(to_do, temp)
	
	elif t==3:
		break	

	elif t==4:
		process.terminate()
		formatted_time = time.strftime('%H:%M:%S', time.localtime())
		print("The 5 minute break has started at ", formatted_time)
		time.sleep(240)
		print("1 minute remains")
		time.sleep(60)
		process = subprocess.Popen(["python", "Blocker.py"])
		clear()
	else:
		print("Wrong choice")
		continue

	clear()	
	display_tasks(to_do)
	display_options()
	


print("Thank you for giving your best and not getting distracted!")

process.terminate()
time.sleep(3)
os.system('exit()')

