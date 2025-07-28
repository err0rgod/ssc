import socket
import argparse



#parser = argparse.ArgumentParser(description="Advance SSH Cracker")

#parser.add_argument("-t","--target",required=True,type=str,help="Enter The target")
#parser.add_argument("-u","--user",type=str,required=True,help="Enter the user or a Wordlist to user names")
#parser.add_argument("-p","--passwd",type=str,required=True,help="Enter the path to wordlist containing passwords")
#

#
#args = parser.parse_args()
#
#host = args.target
#user = args.user
#passwd = args.passwd
#


def check_ssh(ip="steminfinity.in", port=22, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            
            print("Success")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        print("Failure")
        return False


check_ssh()