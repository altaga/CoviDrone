# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:46:30 2018

@author: VAI
"""

import tellopy
import av
import cv2.cv2 as cv2  
import numpy
import time
from time import sleep

prev_flight_data = None
font = cv2.FONT_HERSHEY_SIMPLEX
battery=100

def handler(event, sender, data, **args):
    global prev_flight_data
    global battery
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        if prev_flight_data != str(data):
            #print(data)
            datas=str(data)
            num = datas.find("BAT")
            battery=int(datas[num+4:-31])
            print("Battery:" + str(battery))
            prev_flight_data = str(data)
    else:
        print('event="%s" data=%s' % (event.getname(), str(data)))

cascPath="haar_model/cascade.xml"
signalCascade = cv2.CascadeClassifier(cascPath)
star=1

def main():
    global star
    global cascPath
    posx=0
    counter=0
    drone = tellopy.Tello()
    counter1=0
    step=200 #Seed Value, Dont Care :3
    step1=200
    stop=0
    flag1=True

    try:
        #Start Protocol
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        container = av.open(drone.get_video_stream())
        frame_skip = 300
        xdis=200
        ydis=150
        drone.takeoff()
        sleep(5)
        drone.up(18)
        sleep(5)
        drone.up(0)
        sleep(1)
        countface=0
        # End Start Protocol
        
        
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()
                image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                #imagep= cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_BGR2GRAY)
                
                
                signals = signalCascade.detectMultiScale(
                image,
                scaleFactor=1.7,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )
                
                
                if (len(signals) == 0):
                    countface=0
                    if(step!=0):    
                        if(step==1):
                            drone.backward(0)
                        elif(step==3):
                            drone.up(0)
                        elif(step==4):
                            drone.down(0)
                        elif(step==5):
                            drone.left(0)
                        elif(step==6):
                            drone.right(0)
                        elif(step==7):
                            drone.up(0)
                            drone.right(0)
                        elif(step==8):
                            drone.up(0)
                            drone.left(0)
                        elif(step==9):
                            drone.down(0)
                            drone.right(0)
                        elif(step==10):
                            drone.down(0)
                            drone.left(0)
                        elif(step==11):
                            drone.forward(0)
                        else:
                            ... #Nothing
                    step=0
                    counter1+=1
                    if counter1>=10 and flag1==True:
                        flag1=False
                        if posx < 430:
                            drone.counter_clockwise(0)
                        else:
                            drone.clockwise(0)
                else:
                    flag1=True
                    counter1=0
                    for (x, y, w, h) in signals:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        place = image[y:y+h, x:x+w]
                        
                        #Save last X position in Memory
                        if(countface > 3):
                            posx=(x+(w/2))
                        else:
                            countface+=1
                        
                        signal = signalCascade.detectMultiScale(    
                        image[y:y+h, x:x+w],
                        scaleFactor= 3.5,
                        minNeighbors=20,
                        minSize=(20, 20),
                        flags=cv2.CASCADE_SCALE_IMAGE)
                        
                        for (x, y, w, h) in signal:
                            cv2.rectangle(place, (x, y), (x+w, y+h), (255, 255, 0), 2)
                           
                            if (counter==10):
                                ...
                                #raise ValueError('Close Connection')
                                #break
                            elif (len(signal) != 0):
                                counter+=1
                            else:
                                counter=0
            
                        if(w*h > 60000 and step!=1):
                            if(step==0):
                                drone.clockwise(0)
                            elif(step==1):
                                ...
                                #drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                                drone.counter_clockwise(10)
                                cascPath=cascPathStop
                                stop=1
                            step=1
                            
                        elif(w*h > 40000 and step!=2):
                            
                            if(step!=2):
                                if(step==0):
                                    drone.counter_clockwise(0)
                                    drone.clockwise(0)
                                elif(step==1):
                                    drone.backward(0)
                                elif(step==3):
                                    drone.up(0)
                                elif(step==4):
                                    drone.down(0)
                                elif(step==5):
                                    drone.left(0)
                                elif(step==6):
                                    drone.right(0)
                                elif(step==7):
                                    drone.down(0)
                                    drone.right(0)
                                elif(step==8):
                                    drone.down(0)
                                    drone.left(0)
                                elif(step==9):
                                    drone.up(0)
                                    drone.right(0)
                                elif(step==10):
                                    drone.up(0)
                                    drone.left(0)
                                elif(step==11):
                                    drone.forward(0)
                                else:
                                    if(stop==1):
                                        raise ValueError('Close Connection')
                                        break
        
                            if(y<ydis and step1!=1 and x>xdis and (960-x-w)>xdis):
                                step1=1
                                drone.up(12)
                                print("Up Stable")
                            elif((720-y-h)<ydis and step1!=2 and x>xdis and (960-x-w)>xdis):
                                step1=2
                                drone.down(12)
                                print("Down Stable")
                            elif(x<xdis and step1!=3 and (720-y-h)>ydis and y>ydis):
                                step1=3
                                drone.left(12)
                                print("Left Stable")
                            elif((960-x-w)<xdis and step1!=4 and (720-y-h)>ydis and y>ydis):
                                step1=4
                                drone.right(12)
                                print("Right Stable")
                            elif(y<ydis and step1!=5 and x>xdis and (960-x-w)<xdis):
                                step1=5
                                drone.right(12)
                                drone.up(12)
                                print("Right Up Stable")
                            elif((720-y-h)<ydis and step1!=6 and x>xdis and (960-x-w)<xdis):
                                step1=6
                                drone.right(12)
                                drone.down(12)
                                print("Right Down Stable")
                            elif(y<ydis and step1!=7 and x<xdis and (960-x-w)>xdis):
                                step1=7
                                drone.left(12)
                                drone.up(12)
                                print("Left Up Stable")
                            elif((720-y-h)<ydis and step1!=8 and x<xdis and (960-x-w)>xdis):
                                step1=8
                                drone.left(12)
                                drone.down(12)
                                print("Left Down Stable")
                            elif(step1!=9 and (720-y-h)>ydis and y>ydis and x>xdis and (960-x-w)>xdis):
                                if(step1==1):
                                    drone.up(0)
                                elif(step1==2):
                                    drone.down(0)
                                elif(step1==3):
                                    drone.left(0)
                                elif(step1==4):
                                    drone.right(0)
                                elif(step1==5):
                                    drone.up(0)
                                    drone.right(0)
                                elif(step1==6):
                                    drone.right(0)
                                    drone.down(0)
                                elif(step1==7):
                                    drone.left(0)
                                    drone.up(0)
                                elif(step1==8):
                                    drone.left(0)
                                    drone.down(0)
                                else:
                                    ... #Nothing
                                step1=9
                                print("Stable")
                            else:
                                ... #Nothing
                            step=2
                        elif(y<ydis and step!=3 and x>xdis and (960-x-w)>xdis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=3
                            drone.up(12)
                            print("Up")
                            
                        elif((720-y-h)<ydis and step!=4 and x>xdis and (960-x-w)>xdis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                ...
                                #drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=4
                            drone.down(12)
                            print("Down")
                            
                        elif(x<xdis and step!=5 and (720-y-h)>ydis and y>ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                ...
                                #drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            print(step)
                            step=5
                            drone.left(12)
                            print("Left")
                        elif((960-x-w)<xdis and step!=6 and (720-y-h)>ydis and y>ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                ...
                                #drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=6
                            drone.right(12)
                            print("Right")
                        elif((960-x-w)<xdis and step!=7 and (720-y-h)<ydis and y>ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                ...
                                #drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                ...
                                #drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=7
                            drone.down(12)
                            drone.right(12)
                            print("Right Down")
                        elif(x<xdis and step!=8 and (720-y-h)<ydis and y>ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                ...
                                #drone.down(0)
                            elif(step==5):
                                ...
                                #drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=8
                            drone.down(12)
                            drone.left(12)
                            print("Left Down")
                        elif((960-x-w)<xdis and step!=9 and (720-y-h)>ydis and y<ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                ...
                                #drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                ...
                                #drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                ...
                                #drone.up(0)
                                #drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=9
                            drone.up(12)
                            drone.right(12)
                            print("Right Up")
                        elif(x<xdis and step!=10 and (720-y-h)>ydis and y<ydis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                ...
                                #drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                ...
                                #drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                ...
                                #drone.up(0)
                                #drone.left(0)
                            elif(step==11):
                                drone.forward(0)
                            else:
                                ... #Nothing
                            step=10
                            drone.up(12)
                            drone.left(12)
                            print("Left Up")
                        elif (step!=11 and (720-y-h)>ydis and y>ydis and x>xdis and (960-x-w)>xdis):
                            if(step==0):
                                drone.counter_clockwise(0)
                                drone.clockwise(0)
                            elif(step==1):
                                drone.backward(0)
                            elif(step==3):
                                drone.up(0)
                            elif(step==4):
                                drone.down(0)
                            elif(step==5):
                                drone.left(0)
                            elif(step==6):
                                drone.right(0)
                            elif(step==7):
                                drone.down(0)
                                drone.right(0)
                            elif(step==8):
                                drone.down(0)
                                drone.left(0)
                            elif(step==9):
                                drone.up(0)
                                drone.right(0)
                            elif(step==10):
                                drone.up(0)
                                drone.left(0)
                            elif(step==11):
                                ...
                                #drone.forward(0)
                            else:
                                ... #Nothing
                            step=11
                            drone.forward(12)
                            print("forward")
                        else:
                                ... #Nothing

                        
    # Display the resulting frame
                cv2.putText(image,"Battery %:"+str(battery),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
                cv2.imshow('Original', image)
                               
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    raise ValueError('Close Connection')
                    break
                elif frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
                
    except:
        drone.forward(0)
        drone.backward(0)
        drone.right(0)
        drone.left(0)
        drone.down(0)
        drone.up(0)
        drone.counter_clockwise(100)
        drone.land()
        sleep(5)
        drone.quit()
        cv2.destroyAllWindows()
        exit()
    

if __name__ == '__main__':
    main()