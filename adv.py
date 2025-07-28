import socket
import argparse



parser = argparse.ArgumentParser(description="Advance SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter The target")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the user or a Wordlist to user names")
parser.add_argument("-p","--passwd",type=str,required=True,help="Enter the path to wordlist containing passwords")
