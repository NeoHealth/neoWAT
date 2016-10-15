import matplotlib.pyplot as plt
import numpy as np
from scipy import signal 
import time as t

running_val = []
running_time = []
running_d = []
prevFinger = 0

def totalPeaks(val,time):
    d1 = np.gradient(val)
    thresh = max(val)/2
    peaks = [time[x] for x in range(1,len(time)) if val[x] > thresh and d1[x] * d1[x-1] <0]
    
    return peaks

def checkFingerProbe(fingerVal):    
    global prevFinger
    if (fingerVal and not prevFinger):
        prevFinger = fingerVal
        return True
    prevFinger = fingerVal
    return False
    
def runningPeaks(val, time, sz):
    global running_time
    global running_val
    global running_d
    if (len(running_val) > 0):
        running_d.append((val-running_val[-1])/(time-running_time[-1]))
    else:
        running_d.append(0)
    running_time.append(time)
    running_val.append(val)
    
    if(len(running_time) > sz):
        
        thresh = 0.5*max(running_val)
        if (len(running_time) > sz):
            running_time.pop(0)
            running_val.pop(0)
            if (val > thresh and running_d[-1]*running_d[-2] < 0):
                print('yes')
                return True
            
    return False
    #for x in range(N, len(val)):
       # temp_val = val(x-window:x)
        #temp_time = time(x-window:x)
        

f = open('ecgsyn.dat')
f = list(f)
time = [float(x.split(' ')[0]) for x in f]
val = [float(x.split(' ')[1]) for x in f]
period = time[1] - time[0]
finger_time = [x-0.6 for x in time]
temp_time = [x*(2*np.pi) for x in finger_time]
finger = signal.square(temp_time, 0.5)
finger = [0.5 + x/2 for x in finger]
peak_times = []
a = False
b = False
for x in range(len(time)):
    if(not a and runningPeaks(val[x], time[x], 500)):
        print('Check a checka')
        a = True
        startTime = time[x]
    if(a and checkFingerProbe(finger[x])):
        peak_times.append(time[x] - startTime)
        print(peak_times[-1])
        a = False
    
plt.figure(1)
plt.plot(time[0:1000],finger[0:1000], 'b')
plt.plot(time[0:1000],val[0:1000], 'r')
plt.figure(2)
plt.plot(peak_times)
print(len(peak_times))
plt.show()
      
