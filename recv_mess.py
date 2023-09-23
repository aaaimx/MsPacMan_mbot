import cyberpi, time, event, mbot2
# initialize variables
import socket
#import websockets, asyncio


cyberpi.network.config_sta('iotpractica', '')
cyberpi.network.create_client()
HEADER = 64
PORT = 5050
FORMAT ='utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.0.101'
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

last_move={
    0:'RIGHT',
    1: "None"
    }

byte_str_move_dict={
    b'\x00': 'UP',
    b'\x01': 'RIGHT', 
    b'\x02': 'DOWN',    
    b'\x03': 'LEFT'
    }
move_dict={
    ('UP','RIGHT') : 90,
    ('UP','LEFT') : -90,
    ('UP','UP') : 0,
    ('UP','DOWN') : 180,
    ('RIGHT','DOWN') : 90,
    ('RIGHT','UP') : -90,
    ('RIGHT','LEFT') : 180,
    ('RIGHT','RIGHT') : 0,
    ('LEFT','UP') : 90,
    ('LEFT','DOWN') : -90,
     ('LEFT','RIGHT') :180,
    ('LEFT','LEFT') : 0,
    ('DOWN','RIGHT') : 90,
    ('DOWN','LEFT') : -90,
    ('DOWN','UP') : 180,
    ('DOWN','DOWN') : 0,


}



def receive_messages():
#    URI = "ws://192.168.0.101:5050"
#    async with websockets.connect(URI) as websocket:
#        while True:
#            message=await websocket.recv()
#            print(message)
    while True:
        message = client.recv(1024)
       
        new_message=byte_str_move_dict[message]
        last_move[1]=new_message
        print("mensaje recibido ",new_message)
        #n = int(message)
        cyberpi.console.print("mensaje recibido ")
        cyberpi.console.println(new_message)
        last_move_made=list(last_move.values())
        move(move_dict[tuple(last_move_made)])


def move(moved):
    mbot2.turn(moved)
    mbot2.straight(10)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght=str(msg_lenght).encode(FORMAT)
    send_lenght += b' '*(HEADER-len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    recv = client.recv(2048).decode(FORMAT)
    cyberpi.console.print(recv+'\n')
    move(str(recv))


@event.start
def on_start():
    cyberpi.network.config_sta('iotpractica', '')
    cyberpi.network.create_client()
    while not cyberpi.network.is_connect():
        pass

    cyberpi.led.show('green green green green green')
    cyberpi.console.print(cyberpi.network.get_ip())
    cyberpi.led.show('cyan cyan cyan cyan cyan')
    
    receive_messages()

   # send('Hi')

@event.is_press('b')
def is_btn_press():
    send('127 holaaa')

@event.is_press('a')
def is_btn_press():
    send('cosasssss')

@event.is_press('middle')
def is_joy_press():
    cyberpi.console.clear()