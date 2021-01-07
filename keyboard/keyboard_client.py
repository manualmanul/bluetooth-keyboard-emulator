import dbus
import dbus.service
import datetime
from time import sleep

bus = dbus.SystemBus()
btkservice = bus.get_object("de.syss.btkbdservice", "/de/syss/btkbdservice")
iface = dbus.Interface(btkservice, "de.syss.btkbdservice")


def send(modif, keycode, sint=0.5, longsint=1.2):
    iface.send_keys(modif, keycode)
    iface.send_keys(0, [0, 0, 0, 0, 0, 0])
    if keycode[0] == SPACE:
        sleep(longsint)
    else:
        sleep(sint)


TAB = 43
SPACE = 44

nums = [
    39,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
]

lastdate = datetime.datetime(100, 1, 1, 00, 00, 00)


def gibdate():
    global lastdate
    newdate = lastdate + datetime.timedelta(minutes=user_min)
    for n in newdate.strftime("%H%M"):
        send(0, [nums[int(n)], 0, 0, 0, 0, 0], 0.2)
    lastdate = newdate


def gibnum():
    for n in str(user_min):
        send(0, [nums[int(n)], 0, 0, 0, 0, 0], 0.2)
    sleep(1.5)


# First run
print(
    """
Welcome to Croncuts!

Please follow these instructions:

0. Connect your phone to a bluetooth device "Croncuts_Keyboard"
1. Set device language to English
2. Set time to 24 hours
3. Enable airplane mode w/ bluetooth
4. Swipe to close the Shortcuts app and open it again
4. Go to the automation screen
5. Set up at least one automation
6. Set up a shortcut with a name like "Every X minutes"

"""
)

device = input("Which device are you using? (iPhone/iPad): ")

print("We'll start by aligning Croncuts with the current state of the device\n")
while True:
    user_state = input(
        "Enter YES if you see a blue border around the Automation screen\nOtherwise press ENTER\n"
    )
    if "YES" in user_state:
        break
    else:
        send(0, [TAB, 0, 0, 0, 0, 0])

while True:
    user_min = int(
        input("Enter interval in minutes for which to set up automations: ")
    )
    if 60 % user_min == 0:
        break
    else:
        print("Please enter a number that can be divided by 60 without a remainder")

print("Starting Croncuts deployment")

while True:
    if device.lower() == "iphone":
        send(0, [TAB, 0, 0, 0, 0, 0])
        send(0, [TAB, 0, 0, 0, 0, 0])
        send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [81, 0, 0, 0, 0, 0])
    send(0, [81, 0, 0, 0, 0, 0])
    send(0, [81, 0, 0, 0, 0, 0])
    send(0, [81, 0, 0, 0, 0, 0])
    send(0, [19, 0, 0, 0, 0, 0])
    gibdate()
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [21, 0, 0, 0, 0, 0])
    send(0, [24, 0, 0, 0, 0, 0])
    send(0, [17, 0, 0, 0, 0, 0])
    send(0, [0, 44, 0, 0, 0, 0])
    send(0, [22, 0, 0, 0, 0, 0])
    send(0, [11, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [81, 0, 0, 0, 0, 0])
    send(0, [0, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [8, 0, 0, 0, 0, 0])
    send(0, [25, 0, 0, 0, 0, 0])
    send(0, [8, 0, 0, 0, 0, 0])
    send(0, [21, 0, 0, 0, 0, 0])
    send(0, [28, 0, 0, 0, 0, 0])
    send(0, [0, 44, 0, 0, 0, 0])
    gibnum()
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(1, [TAB, 0, 0, 0, 0, 0])
    send(1, [0, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [TAB, 0, 0, 0, 0, 0])
    send(0, [SPACE, 0, 0, 0, 0, 0])
    if lastdate.strftime("%H%M") == "0000":
        break

print("Done!")
