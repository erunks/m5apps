# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
#import webrepl
#webrepl.start()

from apps.RandomColour import RandomColour

rc = RandomColour()
rc.run()
