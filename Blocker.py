import subprocess
import time

def is_process_running(process_name):
    cmd = 'tasklist /fi "imagename eq {}"'.format(process_name)
    output = subprocess.check_output(cmd, shell=True).decode()
    if process_name.lower() in output.lower():
        return True
    else:
        return False


while 1 :
    if is_process_running("WhatsApp.exe"):
        with open("nul", "w") as null_file:
            subprocess.call("TASKKILL /F /IM WhatsApp.exe", shell=True, stdout=null_file, stderr=null_file)
            time.sleep(5)