import keyboard
import time

# import os
import sys
import numpy
import itertools
import threading
from pywinauto import mouse
from pywinauto.keyboard import send_keys

from skimage.io import imread #type: ignore
from sklearn.svm import SVC #type: ignore
from sklearn.metrics import accuracy_score #type: ignore
from skimage.transform import resize #type: ignore
from sklearn.model_selection import train_test_split #type: ignore
from time import sleep as stop
# from pywinauto import keyboard



import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Define image directory and parameters
# image_dir = 'C:\\Users\\Wes\\Downloads\\DEXP-IMG\\VEX TYPE'
# image_dir = 'C:\\Users\\Wes\\Desktop\\D2Exp'

# image_size = (64, 64)


# done = False



# ########################################################################
# #here is the animation                                              ####
# def animate():                                                      ####
#     for c in itertools.cycle(['|  ', '/  ', '-  ', '\\  ']):        ####
#         if done:                                                    ####
#             break                                                   ####
#         sys.stdout.write('\rloading ' + c)                          ####
#         sys.stdout.flush()                                          ####
#         stop(0.13)                                                  ####
# t = threading.Thread(target=animate)                                ####
# t.start()                                                           ####
# ########################################################################


# AI/ML RECOGNIZE [VEX CONSTRUCTS + SPARROW + SKIMMER + MOB DROP POD TYPE + MISC.CONSTRUCTS] 
# ################################################################################################################################################

# image_dir = r"C:\Users\Wes\Desktop\Vehicle Type"
# image_size = (128, 128)

# images, labels = [], []

# for class_name in os.listdir(image_dir):
#     class_path = os.path.join(image_dir, class_name)
#     if os.path.isdir(class_path):
#         for image_filename in os.listdir(class_path):
#             image_path = os.path.join(class_path, image_filename)
#             try:
#                 img = imread(image_path)
#                 if img is not None:
#                     img_resized = resize(img, image_size, anti_aliasing=True)
#                     images.append(img_resized.flatten())
#                     labels.append(class_name)
#             except Exception as e:
#                 print(f"Skipping {image_path}: {e}")

# X = np.array(images)
# y = np.array(labels)

# print(f"Loaded {len(X)} samples.")

# if len(X) > 0:
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     clf = SVC(kernel='linear', random_state=42)
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     print("Accuracy:", accuracy_score(y_test, y_pred))
# else:
#     print("No images found. Check directory structure and file types.")

# ################################################################################################################################################


# ########################################################################
# VENDOR - TAP                                                        #### 
# for i in range(101):                                                ####
#     stop(18)                                                        ####
#     mouse.click(button='left', coords=(251, 832))                   ####
# sys.stdout.write('\rXUR\'s Exchange 1-item / 1-coin')               ####
# done = True                                                         ####
# ########################################################################
# #POSTMASTER - HOLD                                                 #####
# for i in range(21):                                                #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1000, 350))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rPostmaster Clear')                             #####
# done = True                                                        #####
# ########################################################################
# ########################################################################
# #INVENTORY - HOLD - PRIMARY                                        #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(510, 380))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(410, 380))                                  #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rPrimary Clear')                                #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - ENERGY                                         #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(510, 485))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(410, 485))                                  #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rEnergy Clear')                                 #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - HEAVY                                          ##### 
# for i in range(8):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(510, 639))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(450, 640))                                  #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rPower Clear')                                  #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - MASK                                           #####
# for i in range(8):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 239))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 239))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rMask Clear')                                   #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - MASK MASTERWORK                                #####
# for i in range(8):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 239))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 239))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     mouse.right_click(coords=(1500, 239))                          #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     mouse.move(coords=(270, 430))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(270, 550))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(212, 550))                                  #####
#     # MOUSE CLICK AND HOLD 5 SECONDS                               #####
#     for i in range(5):                                             #####
#         stop(3)                                                    #####
#         mouse.press(button='left',coords=(212, 550))               #####
#         stop(4)                                                    #####
#         mouse.release(button='left',coords=(212, 550))             #####
#     stop(4)                                                        #####
#     keyboard.press('esc')                                          #####
#     keyboard.release('esc')                                        #####
#     stop(4)                                                        #####
#     mouse.move(coords=(1410, 239))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 239))                                 #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#     stop(3)                                                        #####
#     mouse.click(coords=(1500, 239))                                #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
# sys.stdout.write('\rMask Masterworked')                            #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - GAUNTLET                                       #####
# for i in range(7):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 400))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 400))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rGauntlet Clear')                               #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - GAUNTLET MASTERWORK                            #####
# for i in range(7):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 400))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 400))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     mouse.right_click(coords=(1500, 400))                          #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     mouse.move(coords=(270, 430))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(270, 550))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(212, 550))                                  #####
#     # MOUSE CLICK AND HOLD 5 SECONDS                               #####
#     for i in range(5):                                             #####
#         stop(3)                                                    #####
#         mouse.press(button='left',coords=(212, 550))               #####
#         stop(4)                                                    #####
#         mouse.release(button='left',coords=(212, 550))             #####
#     stop(4)                                                        #####
#     keyboard.press('esc')                                          #####
#     keyboard.release('esc')                                        #####
#     stop(4)                                                        #####
#     mouse.move(coords=(1410, 400))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 400))                                 #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#     stop(3)                                                        #####
#     mouse.click(coords=(1500, 400))                                #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
# sys.stdout.write('\rGauntlet Masterworked')                        #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - VESTEMENT                                      #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 540))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 540))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rVestement Cleaned')                            #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - VESTEMENT MASTERWORK                           #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 540))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 540))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     mouse.right_click(coords=(1500, 540))                          #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     mouse.move(coords=(270, 430))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(270, 550))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(212, 550))                                  #####
#     # MOUSE CLICK AND HOLD 5 SECONDS                               #####
#     for i in range(5):                                             #####
#         stop(3)                                                    #####
#         mouse.press(button='left',coords=(212, 550))               #####
#         stop(4)                                                    #####
#         mouse.release(button='left',coords=(212, 550))             #####
#     stop(4)                                                        #####
#     keyboard.press('esc')                                          #####
#     keyboard.release('esc')                                        #####
#     stop(4)                                                        #####
#     mouse.move(coords=(1410, 540))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 540))                                 #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#     stop(3)                                                        #####
#     mouse.click(coords=(1500, 540))                                #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
# sys.stdout.write('\rVestement Masterworked')                       #####
# done = True                                                        #####
# ########################################################################
# #INVENTORY - HOLD - DENIMS                                         #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 609))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 609))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rDenims Cleaned')                               #####
# done = True                                                        #####
# ########################################################################
# ########################################################################
# #INVENTORY - HOLD - DENIMS MASTERWORK                              #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 609))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 609))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     mouse.right_click(coords=(1500, 609))                          #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     mouse.move(coords=(270, 430))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(270, 550))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(212, 550))                                  #####
#     # MOUSE CLICK AND HOLD 5 SECONDS                               #####
#     for i in range(5):                                             #####
#         stop(3)                                                    #####
#         mouse.press(button='left',coords=(212, 550))               #####
#         stop(4)                                                    #####
#         mouse.release(button='left',coords=(212, 550))             #####
#     stop(4)                                                        #####
#     keyboard.press('esc')                                          #####
#     keyboard.release('esc')                                        #####
#     stop(4)                                                        #####
#     mouse.move(coords=(1410, 609))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 609))                                 #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#     stop(3)                                                        #####
#     mouse.click(coords=(1500, 609))                                #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#                                                                    #####
# sys.stdout.write('\rDenims Masterworked')                          #####
# done = True                                                        #####
# ########################################################################
# ########################################################################
# #INVENTORY - HOLD - ACCESSORY                                      #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 750))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 750))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     keyboard.press('f')                                            #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     keyboard.release('f')                                          #####
# sys.stdout.write('\rAccessory Cleaned')                            #####
# done = True                                                        #####
# ########################################################################
# ########################################################################
# #INVENTORY - HOLD - ACCESSORY MASTERWORK                           #####
# for i in range(9):                                                 #####
#     stop(8)                                                        #####
#     mouse.move(coords=(1410, 750))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 750))                                 #####
#     stop(3)                                                        #####
#     # Press and hold 'F'                                           #####
#     mouse.right_click(coords=(1500, 750))                          #####
#     # Hold for 10 seconds (adjust as needed)                       #####
#     stop(4)                                                        #####
#     # Release the key                                              #####
#     mouse.move(coords=(270, 430))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(270, 550))                                  #####
#     stop(3)                                                        #####
#     mouse.move(coords=(212, 550))                                  #####
#     # MOUSE CLICK AND HOLD 5 SECONDS                               #####
#     for i in range(5):                                             #####
#         stop(3)                                                    #####
#         mouse.press(button='left',coords=(212, 550))               #####
#         stop(4)                                                    #####
#         mouse.release(button='left',coords=(212, 550))             #####
#     stop(4)                                                        #####
#     keyboard.press('esc')                                          #####
#     keyboard.release('esc')                                        #####
#     stop(4)                                                        #####
#     mouse.move(coords=(1410, 750))                                 #####
#     stop(3)                                                        #####
#     mouse.move(coords=(1500, 750))                                 #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#     stop(3)                                                        #####
#     mouse.click(coords=(1500, 750))                                #####
#     stop(3)                                                        #####
#     send_keys('^')                                                 #####
#                                                                    #####
# sys.stdout.write('\rAccessory Masterworked')                       #####
# done = True                                                        #####
# ########################################################################
##########################################################################
# #XUR'S INVENTORY - TAP                                             #####
# for i in range(15):                                                #####
#     stop(8)                                                        #####
#     mouse.click(button='left', coords=(1732, 170))                 #####
# sys.stdout.write('\r')                                             #####
# done = True                                                        #####
##########################################################################