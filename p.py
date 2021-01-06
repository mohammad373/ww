# ww

import os
import time
import socket
import requests
import sys
from colorama import Fore

def __target__():
    os.system("clear")
    print(Fore.RED + """
        ////////////////////
        ///////////////////
        //////////////////
        /////////////////
        ////////////////
        ///////////////
        //////////////
        /////////////
        ////////////
        ///////////
        //////////
        /////////
        ////////
        ///////
        //////
        ////
        ///
        //
        /""")

    time.sleep(1)
    target = input(Fore.BLUE + "\n[!] ~ Pleass Enter Your Domain ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "[-] ~ Error : Your Domain Is None ;(")
            time.sleep(0.4)
            sys.exit()
        except:
            sys.exit()
    if not "http://" in target or not "https://" in target:
        target = "http://" + target
    r3 = requests.get(target)
    if r3.status_code == 200:
        print(Fore.GREEN + "[+] ~ Your Domain Is Found ;)")
    else:
        try:
            time.sleep(1)
            print(Fore.RED + "[-] ~ Error Your Domain Is Not Found ;(")
            sys.exit()
        except:
            sys.exit()
    my_list = []
    print("")
    while True:
        i = input(Fore.GREEN + "Pleass Enter Your Text  ==>  ")
        if i.lower == "exit" or i == "" or i == "/":
            break
        else:
            my_list.append(i)
    for i1 in my_list:
        r1 = str(target) + "/" + str(i1)
        r2 = requests.get(r1)
        if r2.status_code == 200:
            print(Fore.GREEN + "[+] ~ " + Fore.GREEN + r1)
        if r2.status_code != 200:
            print(Fore.RED + "[-] ~ " + Fore.RED + r1)
__target__()
