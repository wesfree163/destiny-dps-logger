import sys
import threading
import itertools
from pywinauto import mouse
from time import sleep as stag
from pywinauto import keyboard

done = False

########################################################################
#here is the animation                                              ####
def animate():                                                      ####
    for c in itertools.cycle(['|  ', '/  ', '-  ', '\\  ']):        ####
        if done:                                                    ####
            break                                                   ####
        sys.stdout.write('\rloading ' + c)                          ####
        sys.stdout.flush()                                          ####
        stag(0.13)                                                  ####
t = threading.Thread(target=animate)                                ####
t.start()                                                           ####
########################################################################
# #VENDOR - TAP                                                       ####
# for i in range(15):                                                 ####
#     stag(8)                                                         ####
#     mouse.click(button='left', coords=(1732, 170))                  ####
# sys.stdout.write('\rCollection at the postmaster')                  ####
# done = True                                                         ####
########################################################################
# #POSTMASTER - HOLD                                                 #####
# for i in range(N):                                                 #####
#     stag(8)                                                        #####
#     mouse.click(button='left', coords=(1732, 170))                 #####
# sys.stdout.write('\rCollection at the postmaster')                 #####
# done = True                                                        #####
########################################################################
# #INVENTORY - HOLD - PRIMARY/ENERGY/HEAVY/ARMOR(5)                  #####
# for i in range(N):                                                 #####
#     stag(8)                                                        #####
#     mouse.click(button='left', coords=(1732, 170))                 #####
# sys.stdout.write('\rCollection at the postmaster')                 #####
# done = True                                                        #####
########################################################################
#XUR'S INVENTORY - TAP                                             #####
for i in range(27):                                                #####
    stag(8)                                                        #####
    mouse.click(button='left', coords=(280, 780))                 #####
sys.stdout.write('\rCollection at the postmaster')                 #####
done = True                                                        #####
########################################################################