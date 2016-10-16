import time as t
import numpy as np
import bluetooth
import json
#ReadFromComPort
# input : ACD data
#Maybe filter
#Do math
#Format to Json
#Send Json over bt
lst1 = []
lst2 = []
d1 = []
d2 = []

def runningPeaks(val, sz, n):
    global lst1
    global lst2
    global d1
    global d2
    if (n == 1):
        if (len(lst1) > 0):
            d1.append((val-lst1[-1]))
        else:
            d1.append(0)
        lst1.append(val)
    
        if(len(lst1) > sz):
        
            thresh = 0.5*max(lst1)
            lst1.pop(0)
            d1.pop(0)
            if (val > thresh and d1[-1]*d1[-2] < 0):
                return True
    else:
        if (len(lst2) > 0):
            d2.append((val-lst2[-1]))
        else:
            d2.append(0)
        lst2.append(val)
    
        if(len(lst2) > sz):
        
            thresh = 0.5*max(lst2)
            lst2.pop(0)
            d2.pop(0)
            if (val > thresh and d2[-1]*d2[-2] < 0):
                return True
        
    return False


f = open('ecgsyn.dat')
f = list(f)
time = [float(x.split(' ')[0]) for x in f]
val = [float(x.split(' ')[1]) for x in f]
prevTime = t.time
check = 0
sz = 500
h = 2
P1 = 700
P2 = 766000
P3 = -1
P4 = 9
dist = 1
BP_ptt_cal = 0
BP_cal = 0
while(True):
    GPIO = something
    if (GPIO == 'FF'):
        check = 0
    elif ( check == 0):
        check = 1
        first = runningPeaks(GPIO, sz, 1)
        
    else:
        second = runningPeaks(GPIO,sz,2)
    if (check == 0):
        if (first):
            time1 = t.time
        if (second):
            timeDiff = t.time - time1
            PWV = dist/timeDiff
            BP = P1*PWV*np.exp(P3*PWV) + P2*PWV**P4 - (BP_ptt_cal - BP_cal)            
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            server_sock = BluetoothSocket(bluetooth.RFCOMM)
            port = 1
            server_sock.bind(("",port))
            server_sock.listen(1)
            
            client_sock, address = server_sock.accept()
            print('Accepted connection from', address)
            
            client_sock.send('test')
            client_sock.close()
            server_sock.close()
            
    