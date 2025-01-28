from queue import Queue
import socket
import threading

TARGET = '127.0.0.1'
QUEUE = Queue()
OPEN_PORTS = []
TIMEOUT = 1

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((TARGET, port))
        sock.close()
        return True
    except:
        return False
    
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            QUEUE.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            QUEUE.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 53, 80, 110, 443]
        for port in ports:
            QUEUE.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperated by a blank):")
        ports = list(map(int, ports.split()))
        for port in ports:
            QUEUE.put(port)
    elif mode == 5:
        ports = [
        20, 21, 22, 23, 25, 53, 80, 88, 110, 123, 139, 143, 
        161, 162, 389, 443, 445, 465, 500, 636, 993, 
        1433, 1434, 3306, 3389, 5060, 5061, 8080
        ]
        for port in ports:
            QUEUE.put(port)



def worker():
    while not QUEUE.empty():
        try:
            port = QUEUE.get_nowait()  # Incase the Queue is empty throw an excpetion (caused by conccurent calls)
        except Exception as e:
            break

        # Skip phantom ports caused by LINUX
        if 32768 <= port <= 60999:
            continue
        if portscan(port):
            print(f"Port {port} is open!")
            OPEN_PORTS.append(port)

def run_scanner(threads, mode):
    get_ports(mode)

    thread_list = []

    for i in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
    
    print("Open ports are:", OPEN_PORTS)

run_scanner(100,5)