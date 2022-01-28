from cgi import test
import requests
from mcstatus import MinecraftServer
import time


def send_heartbeat(monitor_url, log):
    _ = requests.get(monitor_url)
    if log:
        print('sent heartbeat')

def test_server(server_url, log, port):
    try:
        server = MinecraftServer(server_url, port)
        status = server.status()
        if log: 
            print(f"The server has {status.players.online} players and replied in {status.latency} ms")
        return True
    except TimeoutError:
        if log: 
            print('server down')
        return False

def loop(   server_url = 'minecraft.lostinthe.cloud', 
            port=25565,
            monitor_url = 'https://status.lostinthe.cloud/api/push/MVSv7gRI3F?msg=OK&ping=',
            delay = 60.0,
            log = False):
    starttime = time.time()
    while True:
        if test_server(server_url, log, port):
            send_heartbeat(monitor_url, log)
        time.sleep(delay - ((time.time() - starttime) % delay))

loop(delay=60, log=True)