import os
import ipaddress
import wifi
import socketpool
import adafruit_requests
import ssl
import time
import json
from digitalio import *
import board


remote = "https://flask.julimiro.eu.org/data.json"


def send(path_parsed, data):
    response = requests.post(f"https://ntfy.sh/{path_parsed}", data=str(data).encode('utf-8'))
    return response.status_code



print("Connecting to WiFi")
#  connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
requests = adafruit_requests.Session(pool, ssl.create_default_context())

#send("julipi1",wifi.radio.ipv4_address)


led_red = DigitalInOut(board.GP0)
led_red.direction = Direction.OUTPUT


led_ylw = DigitalInOut(board.GP16)
led_ylw.direction = Direction.OUTPUT


led_grn = DigitalInOut(board.GP3)
led_grn.direction = Direction.OUTPUT
def cool_sleep_routine(time_var):
    i=0
    time_var=int(time_var)
    while i<time_var:
        print(time_var-i)
        i+=1
        time.sleep(1)
        


cool_sleep_routine(5)

# Listen for connections
while True:
    try:
        print("request")
        request = requests.get(remote)
        print(request.text)
        json_data = json.loads(request.text)
        print(json_data)
        
        led_grn.value=json_data["green"]
        led_ylw.value=json_data["yellow"]
        led_red.value=json_data["red"]
        
        print("sleep")
        cool_sleep_routine(10)
    except OSError as e:
        cl.close()
        print('connection closed')
