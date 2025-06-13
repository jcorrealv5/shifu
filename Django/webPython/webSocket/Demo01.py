import asyncio
from websockets.asyncio.client import connect

async def iniciarWS():
    # async with connect("ws://190.43.83.241:9002") as websocket:
    async with connect("ws://192.168.1.7:9002") as websocket:
        #mensajeEnviar = input("Ingresa un Mensaje: ")
        await websocket.send("jhon correal")
        async for mensaje in websocket:
            print("Mensaje Recibido: " + mensaje)
if __name__ == "__main__":
    asyncio.run(iniciarWS())