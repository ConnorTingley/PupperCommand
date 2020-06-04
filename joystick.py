from UDPComms import Publisher, Subscriber, timeout
import xbox

import time

## you need to git clone the PS4Joystick repo and run `sudo bash install.sh`

## Configurable ##
MESSAGE_RATE = 30

joystick_pub = Publisher(8830)
joystick_subcriber = Subscriber(8840, timeout=0.01)
joystick = xbox.Joystick()

while True:
    print("running")

    if (not joystick.connected()):
        joystick = xbox.Joystick()
    else:

        left_y = joystick.leftY()
        right_y = joystick.rightY()
        right_x = joystick.rightX()
        left_x = joystick.leftX()

        L2 = joystick.leftTrigger()
        R2 = joystick.rightTrigger()

        R1 = joystick.rightBumper()
        L1 = joystick.leftBumper()

        square = joystick.X()
        x = joystick.A()
        circle = joystick.B()
        triangle = joystick.Y()

        dpadx = joystick.dpadRight() - joystick.dpadLeft()
        dpady = joystick.dpadUp() - joystick.dpadDown()

        msg = {
            "ly": left_y,
            "lx": left_x,
            "rx": right_x,
            "ry": right_y,
            "L2": L2,
            "R2": R2,
            "R1": R1,
            "L1": L1,
            "dpady": dpady,
            "dpadx": dpadx,
            "x": x,
            "square": square,
            "circle": circle,
            "triangle": triangle,
            "message_rate": MESSAGE_RATE,
        }
        joystick_pub.send(msg)

    try:
        msg = joystick_subcriber.get()
    except timeout:
        pass

    time.sleep(1 / MESSAGE_RATE)
