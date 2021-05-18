import os
import thread
from subprocess import Popen, PIPE

pwd=os.getcwd()

os.chdir(r"foxeyerobot/build")
#os.system("ls")
os.system("make")

os.chdir(pwd)
os.chdir(r"foxeyerobot/bin")

print("starting main")
p = Popen('./FoxI_main', stdin=PIPE)

def start_foxIiso():
    print("starting iso")
    #os.system("./FoxI_iso --nodisplay --avicfg /home/AD/atewary/LUUM/DeepEdgeSample/videoOut/autoRV_03-12-2020_15-22-12_858~ValidateIsolation_LOCK_DOWN_Right_LL0_target_x23.3734_y28.9256_z35.2151_~")

try:
    thread.start_new_thread(start_foxIiso,())
except:
    print("Error")

print("feeding iso")
p.communicate(os.linesep.join(["IDbg12","quit"]))
print("exit program")
