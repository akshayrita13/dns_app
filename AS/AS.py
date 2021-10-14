import requests
import socket
import json

localPort   = 53533

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('', localPort))

while True:

    message, clientaddress = soc.recvfrom(2048)
    message = message.decode()
    message = json.loads(message)

    if len(message) == 2:
        with open("out.json", "r") as outfile:
            dictionary = json.load(outfile)
        DNS_response = dictionary[message["NAME"]]
        dns_object = json.dumps(DNS_response)
        soc.sendto(dns_object.encode(),clientaddress)

    else:
        database = {message["NAME"]: message}
        as_object = json.dumps(database)
        with open("out.json", "w") as outfile:
            outfile.write(as_object)
        soc.sendto(str(201).encode(), clientaddress)