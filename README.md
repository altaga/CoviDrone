# CoviDrone

Indoor UV light surface cleaning drone.

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Diagram](#diagram)
* [Stripe Led Assembly](#stripe-led-assembly)
* [Gateway Configuration](#gateway-configuration)
* [Demo](#demo)

## Introduction:

The Covid19 pandemic has been an event that has affected not only the life of each person, but the coexistence of people in all aspects of life and one of these aspects has clearly been the way in which employees coexist in offices .

One of the main measures to combat the pandemic is cleaning work areas [1](#1), however the use of chemicals to perform this cleaning can be harmful to health in the long term, so the use of UV lights is a vital part for the future of office work.

I want to make a drone that is capable of disinfecting office areas that conventional robots cannot access for example [2](#2).

- TMiRob 
- XDBOT
- Tru-D SmartUVC
- UVCLight
- Siemens / Aucma

None of these robots is capable of disinfecting surfaces such as tables or desks.

<img src="https://i.ibb.co/5ndwL6K/drone.png" width="800">

# Materials:

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

# Diagram:

<img src="https://i.ibb.co/VjNvMp3/Esquema.png" width="1000">

# Stripe Led Assembly:

Diagram: 

<img src="https://i.ibb.co/JdjKRsr/Untitled-Sketch-2-bb.png" width="1000">

Assemble the LED's one by one, taking care to always connect Anodes with Anodes and Cathodes with Cathodes.

<img src="https://i.ibb.co/BVWSn0r/20200827-182459.jpg" width="1000">

Create a ring around the base of the drone.

<img src="https://i.ibb.co/BZ4dbkx/20200828-232339.jpg" width="1000">

Place the power circuit of the Led strip.

<img src="https://i.ibb.co/M6bh7d0/20200828-233147.jpg" width="1000">

And works.

<img src="https://i.ibb.co/SNBGynq/20200828-233752.jpg" width="1000">

# WARNING

<img src="https://i.ibb.co/sF4QLyG/image.png" width="1000">

According to a scientific article from PurpleSun [3] (# 3) we know the following data:

This measurement here is the minimum dose to lower virus activity by 90%.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=D_{90}\ Dose=47\ \frac{J}{m^2}" width="400">
<p>
<p >
Watts equals Joules between Seconds.
<p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W=\frac{J}{s}" width="200">
</p>
Watts per time equals Joules.
<p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W\ *\ s=\ J" width="200">
</p>
<p >
Therefore Watts per time between area equals Joules between area equals dose.
<p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{W\ *\ s}{m^2}=\frac{J}{m^2}\ =\ Dose" width="500">
</p>
<p >
Within an electrical circuit Watts is equal to Voltage times current.
<p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W=V\ *\ I" width="200">
</p>
Developing the formula to our problem, we know that the voltage of each Led is 3 volts and the number of LED's is 30, therefore.
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W=3\ volts\ *\ I\ *\ 30\ Leds" width="500">
</p>

We obtain the current of the circuit with the resistance that we have before the LED's, since we have a LiPo battery, this will stabilize its voltage at 3.7 Volts, however the LED's require 3 volts to work, therefore our resistance will be determining the current that passes through the LED's, in this case the voltage that the resistance will have will be 0.7 volts.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I\ =\ \frac{V}{R}" width="130">
</p>

Then.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=I\ =\ \frac{0.7\ volts}{22\ ohms}\ =\ 31mA" width="400">
</p>

Therefore the power of all LEDs would be.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=W=3\ *\ 0.0318\ *\ 30\ =\ 2.86\ Watts" width="600">
</p>

Combining all the formulas we obtain the following general formula.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\ \frac{(V_{source}\ -\ V_{Led})}{R}\ *\ V_{Led}\ *\ NLeds\ *\ t}{Area}\ =\ \ Dose" width="1000">
</p>

- Vsource = Voltage of the source [volts]
- Vled = LED operating voltage [volts]
- R = Resistor before the led [ohms]
- NLeds = Number of LED's in parallel in the circuit [dimensionless]
- Area = Exposure area [square meter]
- Time = Exposure time [seconds]

Substituting in the formula the values ​​we want.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2.863*\ t\ =\ \ 47" width="300">
</p>

Now we calculate the exposure time necessary for the drone to achieve the D90 dose.

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=t\ =\ \ \frac{47}{2.863}\ =\ 16.41\ s" width="400">
</p>

# Tello Important Considerations:

- Check the propeller order, if the order of the propellers is not correct, the drone will not fly.
<img src="https://i.ibb.co/QJxjrsX/Correct-Drone-Propeller.png" width="600">

- This drone is very unstable outdoors because wind affects it, I recommend for it only to be used for indoor applications.

- I recommend using a protective cage so that the drone is 100% safe.

<img src="https://gloimg.gbtcdn.com/soa/gb/pdm-product-pic/Electronic/2019/01/14/goods_img_big-v1/20190114092657_21926.jpg" width="600">

- If you use the protective cage the drone can not perform flips, if you try them, the drone will fall and hit itself hard.

- Always check the battery level of the drone, if the battery is less than 10% the drone will not take off, also if it is flying and reaches 10% the drone will land.

# Gateway Configuration:

Download the operating system of the Raspberry Pi.

- To download the operating system of the Raspberry enter the following link:
- Link: https://www.raspberrypi.org/downloads/raspbian/
- Download the lastest version.

Flash the operating system in the SD.

Software: https://www.balena.io/etcher/

Because the drone use the WiFi connection to control it, we must first connect to our WiFi to set up the libraries.

<p align="center">
<img src="https://i.ibb.co/gMGXbYJ/image.png" width="500">
</p>

- Run the following commands to setup the libraries

        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python3-opencv
        pip3 install tellopy
        git clone https://github.com/altaga/CoviDrone
    
- Connect to the Tello Drone WiFi network.

<img src="https://i.ibb.co/JxS59X3/RPI-WiFI.png" width="1000">

# Tello Software:

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

# Demo:

Video: Click on the image:

[![CoviDrone](https://i.ibb.co/5ndwL6K/drone.png)](Pending)

Sorry github does not allow embed videos.

* [Table of Contents](#table-of-contents)

Articles:

### 1
https://covid19.cdc.gov.sa/community-public/preventive-measures-in-workplaces/
### 2
https://tectales.com/bionics-robotics/9-disinfection-robots-fighting-the-coronavirus.html
### 3
https://www.researchgate.net/publication/339887436_2020_COVID-19_Coronavirus_Ultraviolet_Susceptibility