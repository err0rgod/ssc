import socket




def check_ssh(ip="steminfinity.in", port=22, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            
            print("Success")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        print("Failure")
        return False


check_ssh()
