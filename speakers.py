'''import asyncio
from bleak import BleakScanner,BleakClient

class Speakers():
    def __init__(self):
        asyncio.run(find())
        self.connectedClients = []
        
    async def find():
        devices = await BleakScanner.discover()
        for d in devices:
            print(str(d.address) + " " + str(d))
            
    def connect(address):
        client = BleakClient(address)
        client.connect()
        self.connectedClients.append(client)
    
    def play():
        cleint = self.connectedClients[0]
        client.play()'''
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        if (d.name=="TY"):
            print(d.address)

asyncio.run(main())
        