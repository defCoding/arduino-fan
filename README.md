# arduino-fan

A simple toy project I tried out to learn more about connecting a webserver and an Arduino. As the Arduino I used did not support an internet connection, the Arduino is connected to my laptop, which is hosting the webserver. Upon receiving POST requests on the webserver, my laptop uses the serial USB connection to trigger the Arduino's fan.

## Setup
Set up your Arduino with the following circuit and connect it to your PC:

![image](https://user-images.githubusercontent.com/39608887/163492787-d5d2970f-d867-41f8-ac64-48a2a1bbe742.png)


You will need to determine what port the Arduino is connected to. If you have the Arduino IDE open, you can do so through the "Tools" menu and view the "Ports" submenu. On an Unix system, this will start with `/dev/`. In `server/arduino.py`, set the `DEVICE` variable to that path.

Download the required Python libraries with

```
$ pip install -r requirements.txt
```

Upload the `.ino` file from the `arduino/` folder onto your Arduino. Then in `server/`, run

```
$ python3 server.py
```

The server is now running on `localhost` listening on port 80. If you are on the same PC that is connected to the Arduino, you can visit the site at `http://localhost`. If you want to connect to it on a different device on the same network, you must determine the local IP address of the PC and connect to that IP in your browser.
