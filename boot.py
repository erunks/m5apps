# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
#import webrepl
#webrepl.start()

from apps.AppSelector import AppSelector
app = AppSelector()
app.run()
