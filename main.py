import cyberpi, time, event, mbot2
from main1 import *



@event.start
def on_start():
    cyberpi.led.show('blue blue blue blue blue')
    cyberpi.network.config_sta('itmerida', '')
    cyberpi.led.show('green green green green green')
    client = Client("10.64.132.204",8000)
    cyberpi.led.show('yellow yellow yellow yellow yellow')
    #cyberpi.console.println(client.get_address_client())
    while True:
        client.send_msg("holaa")
        msg=client.recv_msg()
        cyberpi.console.println(msg)
        if (msg == "close"):
            client.close_client()
            cyberpi.console.println("client close")
            cyberpi.console.println(msg)
            break

         