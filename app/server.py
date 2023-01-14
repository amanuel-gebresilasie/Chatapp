import websockets
import asyncio
import json
import requests
import os

HOST = "0.0.0.0"
PORT = os.getenv("PORT")
connected = set()

async def broadcast(msg, sender):
    print(f"{json.loads(msg)['name']}: {json.loads(msg)['msg']}")
    for client in connected:
        try:
            await client.send(msg)
        except Exception as e:
            print("Error: ",e.__class__.__name___,"\n\tdesc: ",e)

async def handler(ws):
    #print("NewConnection: ",ws.id)
    # add to set
    connected.add(ws)
    '''
    The Loop below uses the __aiter__ method:
        __aiter__:
            -> yeilds message when ever available
            if not:
                loop is not closed until client is disconnected
    '''
    try:
        async for msg in ws:
            # when msg is recved send the msg to all clients
            data = json.loads(msg)
            requests.post("https://chatapp-production-0a81.up.railway.app/save",data={'name': data['name'],'date': data['_date'],'msg': data['msg']})
            await asyncio.create_task(broadcast(msg,ws))
    except websockets.exceptions.ConnectionClosedError:
        pass
    # this line is hitted when the client disconnectes
    connected.remove(ws)
    #print(f"Client: {ws.id} Disconnected")

async def main():
    async with websockets.serve(handler, HOST, PORT) as s:
        print(f"listening on <{HOST}, {PORT}>...")
        await asyncio.Future()
try:
    asyncio.run(main())
except KeyboardInterrupt as e:
    print("\rServer Disconnected By User")

