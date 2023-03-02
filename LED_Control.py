from PyP100 import PyL530
l530 = PyL530.L530("local IP of the Lightbulb", "Email", "password")
#Connect the P100 device using the tapo app, find the IP address from your router panel
l530.handshake()
l530.login()
alreadyRan=False
def gestureTrue():
    global alreadyRan
    if not alreadyRan:
         l530.setColor(0, 100)
         l530.setBrightness(100)
         l530.turnOn()
         alreadyRan=True
def gestureFalse():
    global alreadyRan
    if alreadyRan:
        l530.setColorTemp(2700)
        l530.setBrightness(50)
        alreadyRan=False

