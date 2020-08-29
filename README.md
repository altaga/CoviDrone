# CoviDrone

When you start driving drones with a remote control, it's like giving a small child the detonator of a bomb, at any time it is possible for the drone to get out of control and take an eye out of someone.

Some examples of problems caused by the bad handling of drones.

"During a Christian Democratic Party campaign in September 2014, a Parrot AR drone crashed in front of German Chancellor Angela Merkel."

"What started out as a goofy holiday promotion ended terribly when a drone crashed into the face of Brooklyn Daily photographer Georgine Benvenuto"

https://www.techrepublic.com/article/12-drone-disasters-that-show-why-the-faa-hates-drones/

Personally, the first time I flew a drone, I almost cut a finger off of my friend, so I say it from my own experience.

I want to make a drone that is capable of disinfecting office areas that conventional robots cannot access for example [1].

- TMiRob 
- XDBOT
- Tru-D SmartUVC
- UVCLight
- Siemens / Aucma

None of these robots is capable of disinfecting surfaces such as tables or desks.

<img src="https://i.ibb.co/p1JxcnM/20200827-225132.jpg" width="1000">

[1] https://tectales.com/bionics-robotics/9-disinfection-robots-fighting-the-coronavirus.html

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Diagram](#diagram)
* [Stripe Led Assembly](#stripe-led-assembly)
* [Gateway Configuration](#gateway-configuration)
* [Demo](#demo)

## Introduction:



<img src="https://i.ibb.co/5ndwL6K/drone.png" width="800">

## Materials:

List the hardware and software you will use to build this.

Hardware: 
- DJI Tello Drone.
- RaspberryPi 3/4.
- Serial Module CH340.
- 30 UV Leds (3V, 40mA).
- 1 Resistor (22 Ohm).
- 3.7 V, 400mA, LiPo Battery, C1.

Software: 
- Python 3.8. 

Libraries:

- Paho-Mqtt. (https://pypi.org/project/paho-mqtt/)
- TelloPy. (https://pypi.org/project/tellopy/) 

## Diagram:

<img src="https://i.ibb.co/VjNvMp3/Esquema.png" width="1000">

## Stripe Led Assembly:

Diagram: 

<img src="https://i.ibb.co/JdjKRsr/Untitled-Sketch-2-bb.png" width="1000">

Assemble the LEDs one by one, taking care to always connect Anodes with Anodes and Cathodes with Cathodes.

<img src="https://i.ibb.co/BVWSn0r/20200827-182459.jpg" width="1000">

Create a ring around the base of the drone.

<img src="https://i.ibb.co/BZ4dbkx/20200828-232339.jpg" width="1000">

Place the power circuit of the Led strip.

<img src="https://i.ibb.co/M6bh7d0/20200828-233147.jpg" width="1000">

And works.

<img src="https://i.ibb.co/SNBGynq/20200828-233752.jpg" width="1000">

## Tello Important Considerations:

- Check the propeller order, if the order of the propellers is not correct, the drone will not fly.
<img src="https://i.ibb.co/QJxjrsX/Correct-Drone-Propeller.png" width="600">

- This drone is very unstable outdoors because wind affects it, I recommend for it only to be used for indoor applications.

- I recommend using a protective cage so that the drone is 100% safe.

<img src="https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/01/14/goods_img_big-v1/20190114092657_21926.jpg" width="600">

- If you use the protective cage the drone can not perform flips, if you try them, the drone will fall and hit itself hard.

- Always check the battery level of the drone, if the battery is less than 10% the drone will not take off, also if it is flying and reaches 10% the drone will land.

## Gateway Configuration:

If you are noob consider setting up your raspberry with the following tutorial.
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

You need to have the following configuration to be able to perform Serial communication.

<img src="https://i.ibb.co/6gKKmy3/raspberry-pi-configuration.png" width="500">

- Run the following commands to setup the libraries

    sudo apt-get update
    sudo apt-get upgrade
    pip3 install tellopy paho-mqtt
    
- Connect to the Tello Drone WiFi network.

<img src="https://i.ibb.co/ZzbxQZC/Capturewifi.png" width="800">
        
- Connect the USBSerial, download and run the code "TelloSerial.py"

<img src="https://i.ibb.co/mHsGSMw/Captures.png" width="800">

## Tello Software:

Libraries that you have to install before continuing.

- https://pypi.org/project/tellopy/
- https://pypi.org/project/pyserial/
- https://pypi.org/project/av/
- https://pypi.org/project/opencv-python/
- https://pypi.org/project/numpy/

The flight algorithm of the Drone is based on pure programming along with the libraries that were previously mentioned. The algorithm reviews at all times that there is a human face in front of it and looks for the way to focus and approach.

Face recognition is done using Face Detection using Haar Cascades, the Haar Cascade file used will be in the "haarcascade" folder, inside "Python Code", more information in the link below.

Link: https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html

It is important to mention that this code provides the method to check all the sensors of the drone, for example the height, the level of the battery, position, etc ... However we added that the battery level has to be displayed in the OpenCV screen at all times:

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
            
            
<img src="https://i.ibb.co/n0SPQpc/rep.png" width="1000">

The system works like a state machine, the case requires the command that makes the drone approach the client, with this type of system we avoid sending commands that are useless to the drone.

Lateral Fly Control Diagram (This is the diagram of how the drone moves if you are looking at it from the side):
<img src="https://i.ibb.co/qmyyPNW/Control.png" width="1000">

Frontal Fly Control Diagram (This is the diagram of how the drone moves if you are looking at it from the front):
<img src="https://i.ibb.co/nCCYmbw/Frontal-control-diagram.png" width="1000">

## System Connection Diagram:

This is our general connection diagram.

<img src="https://i.ibb.co/4Zz9tCM/Spresense-Diagram-bb.png" width="1000">

## Demo:

In this video we will present our EPIC Demo.

Video: Click on the image:

[![SGD](https://i.ibb.co/R4JrJg3/Tello-01.png)](https://youtu.be/IduAEYOa_H8)

Sorry github does not allow embed videos.

* [Table of Contents](#table-of-contents)