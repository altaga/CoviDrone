import serial, time
from time import sleep
import tellopy

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = tellopy.Tello()
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
    
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
        drone.connect()
        drone.wait_for_connection(60.0)
        sleep(5)
        while 1:
            rawString = arduino.readline()
            if(rawString.decode() == "Land\r\n"):
                drone.land()
                print("Land\r\n")
            elif(rawString.decode() == "Take\r\n"):
                drone.takeoff()
                print("Take\r\n")
            elif(rawString.decode() == "Back\r\n"):
                drone.backward(30)
                sleep(2)
                drone.backward(0)
                print("Backward\r\n")
            elif(rawString.decode() == "Forw\r\n"):
                drone.forward(30)
                sleep(2)
                drone.forward(0)
                print("Forward\r\n")
            elif(rawString.decode() == "R\r\n"):
                drone.right(30)
                sleep(2)
                drone.right(0)
                print("Rigth\r\n")
            elif(rawString.decode() == "L\r\n"):
                drone.left(30)
                sleep(2)
                drone.left(0)
                print("Left\r\n")
            elif(rawString.decode() == "Up\r\n"):
                drone.up(30)
                sleep(2)
                drone.up(0)
                print("Up\r\n")
            elif(rawString.decode() == "Down\r\n"):
                drone.down(30)
                sleep(2)
                drone.down(0)
                print("Down\r\n")
            elif(rawString.decode() == "Circle L\r\n"):
                drone.counter_clockwise(60)
                sleep(2)
                drone.counter_clockwise(0)
                print("Circle L\r\n")
            elif(rawString.decode() == "Circle R\r\n"):
                drone.clockwise(60)
                sleep(2)
                drone.clockwise(0)
                print("Circle R\r\n")
            else:
                print(rawString.decode())
                sleep(5)
    except (KeyboardInterrupt, SystemExit):
        arduino.close()
        drone.quit()        

if __name__ == '__main__':
    test()

