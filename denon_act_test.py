import asyncio

from act import DenonACT
import httpx

client = httpx.AsyncClient()
loop = asyncio.get_event_loop()

device = DenonACT("192.168.1.41", lambda: client)
result = loop.run_until_complete(device.get_external_device_profile())
loop.run_until_complete(device.set_external_power_state("OFF", result))
print(result)

loop.run_until_complete(client.aclose())
loop.close()
