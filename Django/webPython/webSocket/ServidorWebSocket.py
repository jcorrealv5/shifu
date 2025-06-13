import asyncio
from websockets.asyncio.server import serve
from websockets.asyncio.server import broadcast

clientes = []
async def handler(websocket):
    clientes.append(websocket)    
    (host, puerto) = websocket.remote_address
    print("Cliente conectado: {0} por el Puerto: {1}".format(host, puerto))
    try:
        async for mensaje in websocket:
            if(mensaje is not None):
                if(type(mensaje) is str):
                    print("Mensaje de Texto Recibido: ", mensaje)
                elif(type(mensaje) is bytes):
                    print("Bytes Recibidos: ", len(mensaje))
                    print("Primer byte: ", str(mensaje[0]))
                broadcast(clientes, mensaje)
        await websocket.wait_closed()
    except Exception as error:
        print("Error: " + str(error))
        clientes.remove(websocket)

async def main():
    print("Iniciando servidor Web Socket")
    async with serve(handler, "192.168.1.7", 9002) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())