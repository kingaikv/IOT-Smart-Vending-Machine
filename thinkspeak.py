
import requests
import random
import subprocess
import time 
import threading
import os


def send_to_thinkspeak(data):
    write_api_key = "4UU5NLXQ7H0ILGN6"
    read_api_key = "XXXNHDO9ZC0CRAAX"
    channel_id = 59136
    url = "https://api.thingspeak.com/update"
    res = requests.get(url,params=data)
    print("%s,%s,res:%s" % (data.get("field3"), data.get("field4"),res.text))



def bme280():
    subprocess.check_output('./app')
    msg = subprocess.check_output('./app')
    mm=msg.decode('utf8')
    t=mm.split(',')[0].split(':')[1]
    h=mm.split(',')[1].split(':')[1]
    p=mm.split(',')[2].split(':')[1]
    
    
    write_api_key = "4UU5NLXQ7H0ILGN6"
    read_api_key = "XXXNHDO9ZC0CRAAX"
    channel_id = 59136
    
    url = "https://api.thingspeak.com/update"
    data={
        "api_key": write_api_key, 
        "field1": str(t),
        "field2": str(h),
        #"field3": str(p),
    }
    
    res = requests.get(url,params=data)
    print(res.text)
    print("%s, %s" % (t,h))

cc2500 = subprocess.Popen('../cc2500/test',shell=True)
print("TEST")



def loop_2():
    while(True):
        time.sleep(0.5)
        if(os.access("/home/pi/misc/cc2500/tmp.data",os.R_OK | os.W_OK)):
            with open("/home/pi/misc/cc2500/tmp.data") as f :
                data = f.readline()
            os.remove("/home/pi/misc/cc2500/tmp.data")

 
            write_api_key = "4UU5NLXQ7H0ILGN6"
            read_api_key = "XXXNHDO9ZC0CRAAX"
            channel_id = 59136
            data={
                "api_key": write_api_key, 
                "field3": data.split(',')[0],
                "field4": data.split(',')[1]
            }
            send_to_thinkspeak(data)
        

        
th_loop2 = threading.Thread(target=loop_2,args=())
th_loop2.start()

while True:
    bme280()
    time.sleep(30)

