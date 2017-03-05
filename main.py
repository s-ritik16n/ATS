import os, sys, time, signal, getpass, crypt, pam, atexit, threading

# support for posix users to run subprocess in python2
if os.name=='posix' and sys.version_info[0]<3:
    import subprocess32 as subprocess
else:
    import subprocess

def checkStat():
    """chekcing the status - charging/discharging"""
    output = subprocess.check_output("upower -i /org/freedesktop/UPower/devices/battery_BAT0",shell=True).split("\n")[11].split()[1]
    return output

def recieve_signal(signum,stack):
    """aynchronously recieving CTRL+C, and hence prompt for password,
    so that noone can turn off this script
    """
    promptpass();

#async function which catches the signal
signal.signal(signal.SIGINT,recieve_signal)

def loopChargeStat():
    """if system is in charging status,
    keep checking for power interrupt"""
    while checkStat() == "charging":
        time.sleep(2)
    if checkStat() != "charging":
        alarm()

def alarm():
    """if someone disconnects from charging,
    raise the alarm"""
    print "alarm"
    sys.exit()  #for the mean time

def promptpass():
    """the person who wishes to exit this programm should authenticate first"""
    passw = getpass.getpass(prompt = "Enter password: ")
    if not checkpass(passw):
        print "Unsuccessful attempt - the owner wants you to stay away"
    else:
        sys.exit()

def checkpass(passw):
    return pam.authenticate(os.environ["LOGNAME"],passw)

def new_bash():
    os.system("gnome-terminal -e 'bash -c \"python main.py 0; exec bash\"'")
    #os.Popen("python main.py")
    print threading.current_thread()

def create_another_thread():
    t1 = threading.Thread(target=new_bash,name="supporting_thread1")
    t1.start()
    t2 = threading.Thread(target=new_bash,name="supportingthread2")
    t2.start()

if len(sys.argv) == 1:
    create_another_thread()
loopChargeStat()
